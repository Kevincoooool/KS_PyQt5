#! python3
import os
import sys
import collections
import configparser
import threading
import time

from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QThread, QByteArray
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QProgressBar

from pyocd.probe import aggregator
from pyocd.coresight import dap, ap, cortex_m

import device
from device import globalvar

'''
from MCUProg_UI import Ui_MCUProg
class MCUProg(QWidget, Ui_MCUProg):
    def __init__(self, parent=None):
        super(MCUProg, self).__init__(parent)
        
        self.setupUi(self)
'''


class Worker(QThread):
    progressBarValue = pyqtSignal(int)  # 更新进度条
    InfoValue = pyqtSignal(str)  # 更新进度条
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        for i in range(1000000):
            time.sleep(0.001)
            self.progressBarValue.emit(globalvar.get_value('progress'))  # 发送进度条的值 信号
            flag_get = globalvar.get_value('flag')
            if flag_get == 1:
                print(flag_get)
                info_get = globalvar.get_value('info')
                print(info_get)
                globalvar.set_value('flag', 0)
                self.InfoValue.emit(info_get)
                # time.sleep(1)



class MCUProg(QWidget):
    def __init__(self, parent=None):
        super(MCUProg, self).__init__(parent)

        uic.loadUi('MCUProg.ui', self)
        self.progressBar.setVisible(True)
        globalvar._init()

        self.initSetting()
        self.daplink = None

        self.tmrDAP = QtCore.QTimer()
        self.tmrDAP.setInterval(1000)
        self.tmrDAP.timeout.connect(self.on_tmrDAP_timeout)
        self.tmrDAP.start()

        self.thread_progress = Worker()
        self.thread_progress.progressBarValue.connect(self.copy_file)
        self.thread_progress.InfoValue.connect(self.Info_tip)
        self.thread_progress.start()



    def copy_file(self, i):
        self.progressBar.setValue(i)

    def Info_tip(self, str_):
        self.mytextBrowser.append(str_)

    def initSetting(self):
        if not os.path.exists('setting.ini'):
            open('setting.ini', 'w', encoding='utf-8')

        self.conf = configparser.ConfigParser()
        self.conf.read('setting.ini', encoding='utf-8')

        if not self.conf.has_section('globals'):
            self.conf.add_section('globals')
            self.conf.set('globals', 'mcu', 'STM32F103C8')
            self.conf.set('globals', 'addr', '0 K')
            self.conf.set('globals', 'size', '64 K')
            self.conf.set('globals', 'hexpath', '[]')

        self.cmbMCU.addItems(device.Devices.keys())
        self.cmbMCU.setCurrentIndex(self.cmbMCU.findText(self.conf.get('globals', 'mcu')))

        self.cmbHEX.addItems(eval(self.conf.get('globals', 'hexpath')))

    @pyqtSlot()
    def on_btnErase_clicked(self):
        self.mytextBrowser.clear()
        self.dap = self.openDAP()
        self.dev = device.Devices[self.cmbMCU.currentText()](self.dap)
        self.setEnabled(False)
        self.dev.sect_erase(self.addr, self.size)
        QMessageBox.information(self, '擦除完成', '        芯片擦除完成        ', QMessageBox.Yes)
        self.dap.reset()
        self.daplink.close()
        self.setEnabled(True)

    @pyqtSlot()
    def on_btnWrite_clicked(self):
        self.mytextBrowser.clear()
        self.progressBar.setVisible(True)
        if self.cmbHEX.currentText().endswith('.hex'):
            data = parseHex(self.cmbHEX.currentText())
        else:
            data = open(self.cmbHEX.currentText(), 'rb').read()

        self.dap = self.openDAP()
        self.dev = device.Devices[self.cmbMCU.currentText()](self.dap)

        self.setEnabled(False)
        if len(data) % self.dev.PAGE_SIZE:
            data += b'\xFF' * (self.dev.PAGE_SIZE - len(data) % self.dev.PAGE_SIZE)

        self.threadWrite = ThreadAsync(self.dev.chip_write, self.addr, data)
        self.threadWrite.taskFinished.connect(self.on_btnWrite_finished)
        self.threadWrite.start()





    def on_btnWrite_finished(self):

        self.progressBar.setVisible(True)
        self.dap.reset()
        self.daplink.close()
        self.setEnabled(True)

        self.btnWrite.setEnabled(True)
        self.progressBar.setValue(100)

        QMessageBox.information(self, '烧写完成', '        程序烧写完成        ', QMessageBox.Yes)

    @pyqtSlot()
    def on_btnRead_clicked(self):
        self.mytextBrowser.clear()
        self.dap = self.openDAP()
        self.dev = device.Devices[self.cmbMCU.currentText()](self.dap)

        self.setEnabled(False)
        self.buff = []  # bytes 无法 extend，因此用 list
        self.threadRead = ThreadAsync(self.dev.chip_read, self.addr, self.size, self.buff)
        self.threadRead.taskFinished.connect(self.on_btnRead_finished)
        self.threadRead.start()

    def on_btnRead_finished(self):
        binpath, filter = QFileDialog.getSaveFileName(caption='将读取到的数据保存到文件', filter='程序文件 (*.bin)')
        if binpath:
            with open(binpath, 'wb') as f:
                f.write(bytes(self.buff))

        self.dap.reset()
        self.daplink.close()

        self.setEnabled(True)

    def openDAP(self):
        self.daplink = self.daplinks[self.cmbDAP.currentText()]
        self.daplink.open()

        _dp = dap.DebugPort(self.daplink, None)
        _dp.init()
        _dp.power_up_debug()

        _ap = ap.AHB_AP(_dp, 0)
        _ap.init()

        return cortex_m.CortexM(None, _ap)

    def on_tmrDAP_timeout(self):
        ''' 自动检测 DAPLink 的热插拔 '''
        if self.isEnabled():
            daplinks = aggregator.DebugProbeAggregator.get_all_connected_probes()

            if len(daplinks) != self.cmbDAP.count():
                self.cmbDAP.clear()
                for daplink in daplinks:
                    self.cmbDAP.addItem(daplink.product_name)

                self.daplinks = collections.OrderedDict([(daplink.product_name, daplink) for daplink in daplinks])

                if self.daplink and self.daplink.product_name in self.daplinks:
                    self.cmbDAP.setCurrentIndex(self.daplinks.keys().index(self.daplink.product_name))

    @property
    def addr(self):
        return int(self.cmbAddr.currentText().split()[0]) * 1024

    @property
    def size(self):
        return int(self.cmbSize.currentText().split()[0]) * 1024

    @pyqtSlot(str)
    def on_cmbMCU_currentIndexChanged(self, str):
        dev = device.Devices[self.cmbMCU.currentText()]

        self.cmbAddr.clear()
        self.cmbSize.clear()
        for i in range(dev.CHIP_SIZE // dev.SECT_SIZE):
            if (dev.SECT_SIZE * i) % 1024 == 0:
                self.cmbAddr.addItem('%d K' % (dev.SECT_SIZE * i // 1024))
            if (dev.SECT_SIZE * (i + 1)) % 1024 == 0:
                self.cmbSize.addItem('%d K' % (dev.SECT_SIZE * (i + 1) // 1024))

        self.cmbAddr.setCurrentIndex(self.cmbAddr.findText(self.conf.get('globals', 'addr')))
        self.cmbSize.setCurrentIndex(self.cmbSize.findText(self.conf.get('globals', 'size')))

    @pyqtSlot()
    def on_btnHEX_clicked(self):
        hexpath, filter = QFileDialog.getOpenFileName(caption='程序文件路径', filter='程序文件 (*.bin *.hex)',
                                                      directory=self.cmbHEX.currentText(), )
        if hexpath:
            self.cmbHEX.insertItem(0, hexpath)
            self.cmbHEX.setCurrentIndex(0)

    def closeEvent(self, evt):
        self.conf.set('globals', 'mcu', self.cmbMCU.currentText())
        self.conf.set('globals', 'addr', self.cmbAddr.currentText())
        self.conf.set('globals', 'size', self.cmbSize.currentText())

        hexpath = [self.cmbHEX.currentText()] + [self.cmbHEX.itemText(i) for i in range(self.cmbHEX.count())]
        self.conf.set('globals', 'hexpath', repr(list(collections.OrderedDict.fromkeys(hexpath))))  # 保留顺序去重

        self.conf.write(open('setting.ini', 'w', encoding='utf-8'))


class ThreadAsync(QThread):
    taskFinished = pyqtSignal()

    def __init__(self, func, *args):
        super(ThreadAsync, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)
        self.taskFinished.emit()


def parseHex(file):
    ''' 解析 .hex 文件，提取出程序代码，没有值的地方填充0xFF '''
    data = ''
    currentAddr = 0
    extSegAddr = 0  # 扩展段地址
    for line in open(file, 'rb').readlines():
        line = line.strip()
        if len(line) == 0: continue

        len_ = int(line[1:3], 16)
        addr = int(line[3:7], 16) + extSegAddr
        type = int(line[7:9], 16)
        if type == 0x00:
            if currentAddr != addr:
                if currentAddr != 0:
                    data += '\xFF' * (addr - currentAddr)
                currentAddr = addr
            for i in range(len_):
                data += chr(int(line[9 + 2 * i:11 + 2 * i], 16))
            currentAddr += len_
        elif type == 0x02:
            extSegAddr = int(line[9:9 + 4], 16) * 16
        elif type == 0x04:
            extSegAddr = int(line[9:9 + 4], 16) * 65536

    return data.encode('latin')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mcu = MCUProg()
    mcu.show()
    app.exec()
