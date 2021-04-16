"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B510, 0xD0022A01, 0xD1232A02, 0xBF00E000, 0x6800484F, 0x6070F440, 0xF8C44C4E, 0x484E0C18,
        0x60204C4E, 0x6020484E, 0x4C4F484E, 0x484F6020, 0xF8C44C48, 0x484E0C14, 0xF4106800, 0xD1081F80,
        0x5055F245, 0x60204C4B, 0x60602006, 0x70FFF640, 0xBF0060A0, 0x2000BF00, 0x4601BD10, 0xD0022901,
        0xD1102902, 0xBF00E000, 0x68004843, 0x0004F040, 0xF8C24A38, 0x46100C04, 0x0C04F8D0, 0x0001F040,
        0x0C04F8C2, 0xBF00BF00, 0x47702000, 0x493B2000, 0x60486008, 0x60C86088, 0xF64AE003, 0x493520AA,
        0x482B6008, 0xF0106800, 0xD1F60F01, 0x49334834, 0x48346008, 0x48346048, 0x60C86088, 0xF64AE003,
        0x492C20AA, 0x48226008, 0xF0106800, 0xD1F60F01, 0x6800481F, 0x6F70F410, 0x481DD009, 0xF4406800,
        0x491C6070, 0x0C18F8C1, 0x0001F04F, 0x20004770, 0x4601E7FC, 0x47702000, 0x20014603, 0xB5104770,
        0xF1014603, 0xF020000F, 0xE01D010F, 0x60186810, 0xF64AE003, 0x4C1720AA, 0x480D6020, 0xF0106800,
        0xD1F60F01, 0x6800480A, 0x6F70F410, 0x4808D009, 0xF4406800, 0x4C076070, 0x0C18F8C4, 0x0001F04F,
        0x1D1BBD10, 0x1F091D12, 0xD1DF2900, 0xE7F72000, 0x40023C18, 0x40023000, 0x89ABCDEF, 0x40023C0C,
        0x02030405, 0xFBEAD9C8, 0x40023C14, 0x24252627, 0x40023C1C, 0x40003000, 0x40023C04, 0x1FF80000,
        0xFF5500AA, 0xFF870078, 0xFFFF0000, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000007B,
    'pc_EraseSector'     : 0x20000113,
    'pc_ProgramPage'     : 0x2000011F,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x200000AD,
    'pc_BlankCheck'      : 0x20000119,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x0000018C,
    'rw_start'           : 0x0000018C,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x00000190,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x1FF80000,
    'flash_size'         : 0x00000010,
    'flash_page_size'    : 0x00000010,
}
