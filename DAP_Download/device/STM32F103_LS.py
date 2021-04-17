import time

from device import globalvar

FLASH_KR = 0x40022004
FLASH_SR = 0x4002200C
FLASH_CR = 0x40022010
FLASH_AR = 0x40022014

FLASH_KR_KEY1 = 0X45670123
FLASH_KR_KEY2 = 0XCDEF89AB

FLASH_SR_BUSY   = (1 << 0)

FLASH_CR_PWRITE = (1 << 0)  #Page  Write
FLASH_CR_SERASE = (1 << 1)  #Sect  Erase
FLASH_CR_CERASE = (1 << 2)  #Chip  Erase
FLASH_CR_ESTART = (1 << 6)  #Erase Start
FLASH_CR_LOCK   = (1 << 7)


class STM32F103C8(object):
    CHIP_CORE = 'Cortex-M3'

    PAGE_SIZE = 1024 * 1
    SECT_SIZE = 1024 * 1
    CHIP_SIZE = 1024 * 64

    def __init__(self, dap):
        super(STM32F103C8, self).__init__()
        
        self.dap = dap

    def unlock(self):
        self.dap.write32(FLASH_KR, FLASH_KR_KEY1)
        self.dap.write32(FLASH_KR, FLASH_KR_KEY2)

    def lock(self):
        self.dap.write32(FLASH_CR, self.dap.read32(FLASH_CR) | FLASH_CR_LOCK)

    def wait_ready(self):
        while self.dap.read32(FLASH_SR) & FLASH_SR_BUSY:
            time.sleep(0.001)
    
    def sect_erase(self, addr, size):
        self.unlock()
        self.dap.write32(FLASH_CR, self.dap.read32(FLASH_CR) | FLASH_CR_SERASE)
        for i in range(0, (size + self.SECT_SIZE - 1) // self.SECT_SIZE):
            self.dap.write32(FLASH_AR, 0x08000000 + addr + self.SECT_SIZE * i)
            self.dap.write32(FLASH_CR, self.dap.read32(FLASH_CR) | FLASH_CR_ESTART)
            self.wait_ready()
        self.dap.write32(FLASH_CR, self.dap.read32(FLASH_CR) &~FLASH_CR_SERASE)
        self.lock()

    def page_write(self, addr, data):

        self.unlock()
        self.dap.write32(FLASH_CR, self.dap.read32(FLASH_CR) | FLASH_CR_PWRITE)
        for i in range(self.PAGE_SIZE//2):
            self.dap.write16(addr + i*2, data[i*2] | (data[i*2+1] << 8))

        self.wait_ready()
        self.dap.write32(FLASH_CR, self.dap.read32(FLASH_CR) &~FLASH_CR_PWRITE)
        self.lock()


    
    def chip_write(self, addr, data):
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', '开始擦除')
        self.sect_erase(addr, len(data))
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "擦除成功")
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "烧录中...")
        for i in range(0, len(data)//self.PAGE_SIZE):
            self.page_write(0x08000000 + addr + self.PAGE_SIZE * i, data[self.PAGE_SIZE*i : self.PAGE_SIZE*(i+1)])
            progress = (int)(self.PAGE_SIZE * i / len(data) * 100)
            globalvar.set_value('progress', progress)
        globalvar.set_value('flag', 1)
        globalvar.set_value('info', "烧录完成！！")
    def chip_read(self, addr, size, buff):
        data = self.dap.read_memory_block8(addr, size)

        buff.extend(data)


class STM32F103RC(STM32F103C8):
    PAGE_SIZE = 1024 * 2
    SECT_SIZE = 1024 * 2
    CHIP_SIZE = 1024 * 256
