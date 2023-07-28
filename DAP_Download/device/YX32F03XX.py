import time

import jlink
from pyocd.coresight import dap

from . import globalvar
from .flash_dap import Flash_DAP
from .flash_jlink import Flash_JLINK

class YX32F03(object):
    CHIP_CORE = 'Cortex-M0'

    PAGE_SIZE = 512 * 1
    SECT_SIZE = 512 * 1
    CHIP_SIZE = 1024 * 32

    def __init__(self, dap):
        super(YX32F03, self).__init__()
        if globalvar.get_value('dap_or_jlink'):
            self.dap = dap
            self.flash = Flash_DAP(self.dap, YX32F03_flash_algo)
        else:
            self.jlink = dap
            self.flash = Flash_JLINK(self.jlink, YX32F03_flash_algo)

    def sect_erase(self, addr, size):

        globalvar.set_value('flag', 1)
        globalvar.set_value('info', '开始擦除')
        time_start = int(round(time.time() * 1000))
        self.flash.Init(0, 0, 1)
        for i in range( addr// self.SECT_SIZE, (addr + size + (self.SECT_SIZE - 1)) // self.SECT_SIZE):
            self.flash.EraseSector(self.SECT_SIZE * i)
            progress = (int)(self.SECT_SIZE * i / size*100 )
            globalvar.set_value('progress', progress)

        time_finish = int(round(time.time() * 1000))
        self.flash.UnInit(1)
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', '擦除成功')
        time.sleep(0.1)
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "擦除耗时：" + str((time_finish - time_start) / 1000) + "  S")

    def chip_write(self, addr, data):

        globalvar.set_value('flag', 1)
        globalvar.set_value('info', '开始擦除')
        time_start = int(round(time.time() * 1000))
        self.sect_erase(addr, len(data))
        time_finish = int(round(time.time() * 1000))
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "擦除成功")
        time.sleep(0.1)
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "擦除耗时：" + str((time_finish - time_start) / 1000) + "  S")
        self.flash.Init(0, 0, 2)
        time_start = int(round(time.time() * 1000))
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "烧录中...")
        flash_start = globalvar.get_value('addr')
        for i in range(len(data) // self.PAGE_SIZE):
            self.flash.ProgramPage(flash_start + addr + self.PAGE_SIZE * i,
                                   data[self.PAGE_SIZE * i: self.PAGE_SIZE * (i + 1)])
            progress = (int)(self.PAGE_SIZE * i / len(data) * 100)
            globalvar.set_value('progress', progress)
        if progress < 100:
            globalvar.set_value('progress', 100)
        time_finish = int(round(time.time() * 1000))
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "烧录完成！！")
        time.sleep(0.01)
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "耗时：" + str((time_finish - time_start) / 1000) + "  S")
        time.sleep(0.01)
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "烧录速度：" + str(len(data) / (time_finish - time_start)) + "  KB/s")

        self.flash.UnInit(2)

    def chip_read(self, addr, size, buff):
        flash_start = globalvar.get_value('addr')
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "读取中...")
        if globalvar.get_value('dap_or_jlink'):
            data = self.dap.read_memory_block8(flash_start + addr, size)
            buff.extend(data)
        else:
            c_char_Array = self.jlink.read_mem(flash_start + addr, size)
            buff.extend(list(bytes(c_char_Array)))
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "读取完成！请选择文件夹保存bin文件")


YX32F03_flash_algo = {
    'load_address' : 0x10000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B530, 0x2100460C, 0x4D342002, 0x20246028, 0x62A84D33, 0x60282002, 0x4D322001, 0xBF0060E8,
        0x1C49E000, 0x42814830, 0x2000D3FB, 0x4601BD30, 0x47702000, 0xE00E2100, 0x6081482A, 0x4A292004,
        0xBF006010, 0x68004827, 0x320122FF, 0xD1F94210, 0x31FF31FF, 0x20013102, 0x428103C0, 0x2000DBEC,
        0x46014770, 0x6081481F, 0x4B1E2004, 0x46186018, 0x68026802, 0x481BBF00, 0x23FF6800, 0x42183301,
        0x2000D1F9, 0xB5F04770, 0x46144603, 0x2200E022, 0xE00E2500, 0x1C647826, 0x463700D0, 0x433D4087,
        0x29001E49, 0x1C52D001, 0x2204E000, 0xD1002A04, 0x2A04E001, 0xBF00D1EE, 0x6083480A, 0x20026045,
        0x60384F08, 0x4807BF00, 0x27FF6800, 0x42383701, 0x1D1BD1F9, 0xD1DA2900, 0xBDF02000, 0x40004000,
        0x40048000, 0x50060000, 0x00002710, 0x00000000
    ],

    'pc_Init'            : 0x10000001,
    'pc_UnInit'          : 0x1000002F,
    'pc_EraseSector'     : 0x10000063,
    'pc_ProgramPage'     : 0x10000087,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x10000035,
    'pc_BlankCheck'      : 0x12000001F,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x10000400,
    'begin_data'         : 0x10000800,
    'begin_stack'        : 0x10000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x000000EC,
    'rw_start'           : 0x000000EC,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x000000F0,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x00000000,
    'flash_size'         : 0x00008000,
    'flash_page_size'    : 0x00000200,
}
