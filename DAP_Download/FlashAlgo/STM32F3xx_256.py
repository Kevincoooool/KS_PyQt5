"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x49364837, 0x49376041, 0x21006041, 0x68C16001, 0x43112214, 0x69C060C1, 0xD40605C0, 0x49324833,
        0x21066001, 0x49326041, 0x20006081, 0x482C4770, 0x22806901, 0x61014311, 0x47702000, 0x4828B510,
        0x24046901, 0x61014321, 0x22406901, 0x61014311, 0x4A264928, 0x6011E000, 0x07DB68C3, 0x6901D1FB,
        0x610143A1, 0xBD102000, 0x491DB510, 0x2402690A, 0x610A4322, 0x69086148, 0x43102240, 0x481D6108,
        0xE0004A1A, 0x68CB6010, 0xD1FB07DB, 0x43A06908, 0x20006108, 0xB570BD10, 0x08491C49, 0x26140049,
        0x23014D0F, 0x692CE016, 0x612C431C, 0x80048814, 0x07E468EC, 0x692CD1FC, 0x00640864, 0x68EC612C,
        0xD0044234, 0x433068E8, 0x200160E8, 0x1C80BD70, 0x1E891C92, 0xD1E62900, 0xBD702000, 0x45670123,
        0x40022000, 0xCDEF89AB, 0x00005555, 0x40003000, 0x00000FFF, 0x0000AAAA, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000004F,
    'pc_EraseSector'     : 0x20000089,
    'pc_ProgramPage'     : 0x200000B7,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x2000005D,
    'pc_BlankCheck'      : 0x12000001F,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20001000,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x000000F8,
    'rw_start'           : 0x000000F8,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x000000FC,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x08000000,
    'flash_size'         : 0x00040000,
    'flash_page_size'    : 0x00000400,
}
