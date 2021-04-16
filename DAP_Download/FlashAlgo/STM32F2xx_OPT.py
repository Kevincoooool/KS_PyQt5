"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x0E000300, 0xD3022820, 0x1D000940, 0x28104770, 0x0900D302, 0x47701CC0, 0x47700880, 0x49284829,
        0x49296081, 0x68C16081, 0x431122F0, 0x694060C1, 0xD4060680, 0x49254826, 0x21066001, 0x49256041,
        0x20006081, 0x481F4770, 0x22016941, 0x61414311, 0x47702000, 0x68C2481B, 0x430A21F0, 0x4A1E60C2,
        0x69426142, 0x431A2302, 0x68C26142, 0x0F120612, 0x68C2D004, 0x60C2430A, 0x47702001, 0x47702000,
        0x47702000, 0x88108911, 0x09090509, 0x00800880, 0x480C4301, 0x22F068C3, 0x60C34313, 0x43192302,
        0x68C16141, 0xD4FC03C9, 0x060968C1, 0xD0040F09, 0x431168C1, 0x200160C1, 0x20004770, 0x00004770,
        0x08192A3B, 0x40023C00, 0x4C5D6E7F, 0x00005555, 0x40003000, 0x00000FFF, 0x0FFFAAEC, 0x00000000
    ],

    'pc_Init'            : 0x2000003D,
    'pc_UnInit'          : 0x20000067,
    'pc_EraseSector'     : 0x200000A1,
    'pc_ProgramPage'     : 0x200000A5,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x20000075,
    'pc_BlankCheck'      : 0x12000001F,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x000000DC,
    'rw_start'           : 0x000000DC,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x000000E0,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x1FFFC000,
    'flash_size'         : 0x00000010,
    'flash_page_size'    : 0x00000010,
}
