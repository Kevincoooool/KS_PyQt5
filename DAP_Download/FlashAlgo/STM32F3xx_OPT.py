"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4A4A484B, 0x494B6042, 0x60826041, 0x21006081, 0x68C16001, 0x43112214, 0x69C060C1, 0xD40605C0,
        0x49454846, 0x21066001, 0x49456041, 0x20006081, 0x483F4770, 0x15426901, 0x61014391, 0x22806901,
        0x61014311, 0x47702000, 0x4839B570, 0x231468C1, 0x60C14319, 0x24206901, 0x61014321, 0x22406901,
        0x61014311, 0x4A354937, 0x6011E000, 0x07ED68C5, 0x6905D1FB, 0x610543A5, 0x24106905, 0x61054325,
        0x4E314D2D, 0x80353555, 0x6011E000, 0x07ED68C5, 0x6901D1FB, 0x610143A1, 0x421968C1, 0x68C1D004,
        0x60C14319, 0xBD702001, 0xBD702000, 0x4820B510, 0x24206901, 0x61014321, 0x22406901, 0x61014311,
        0x4A1E4920, 0x6011E000, 0x07DB68C3, 0x6901D1FB, 0x610143A1, 0xBD102000, 0x47702001, 0x1C49B5F0,
        0x00490849, 0x26104D12, 0xE01A4B16, 0x4334692C, 0x8814612C, 0x4C118004, 0x6023E000, 0x07FF68EF,
        0x692CD1FB, 0x612C43B4, 0x271468EC, 0xD005423C, 0x201468E9, 0x60E94301, 0xBDF02001, 0x1C921C80,
        0x29001E89, 0x2000D1E2, 0x0000BDF0, 0x45670123, 0x40022000, 0xCDEF89AB, 0x00005555, 0x40003000,
        0x00000FFF, 0x0000AAAA, 0x1FFFF800, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x20000053,
    'pc_EraseSector'     : 0x200000CD,
    'pc_ProgramPage'     : 0x200000FD,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x20000069,
    'pc_BlankCheck'      : 0x200000F9,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x0000014C,
    'rw_start'           : 0x0000014C,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x00000150,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x1FFFF800,
    'flash_size'         : 0x00000010,
    'flash_page_size'    : 0x00000010,
}
