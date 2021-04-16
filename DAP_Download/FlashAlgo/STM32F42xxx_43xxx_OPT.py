"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x03004601, 0x28200E00, 0x0940D302, 0xE0051D00, 0xD3022810, 0x1CC00900, 0x0880E000, 0xD50102C9,
        0x43082110, 0x48344770, 0x60814932, 0x60814933, 0x22F068C1, 0x60C14311, 0x06806940, 0x4831D406,
        0x6001492F, 0x60412106, 0x6081492F, 0x47702000, 0x69414829, 0x43112201, 0x20006141, 0x48264770,
        0x21F068C2, 0x60C2430A, 0x61824A28, 0x61424A28, 0x23026942, 0x6142431A, 0x061268C2, 0xD0040F12,
        0x430A68C2, 0x200160C2, 0x20004770, 0x20004770, 0xB5104770, 0xCA064818, 0x23F068C4, 0x60C4431C,
        0x40224C1A, 0x4A1B6182, 0x1C894011, 0x68C16141, 0xD4FC03C9, 0x060968C1, 0xD0040F09, 0x431968C1,
        0x200160C1, 0x2000BD10, 0xB570BD10, 0x68134E0A, 0x68524C10, 0x40236975, 0x42AB4025, 0x4B0BD106,
        0x401A69B4, 0x42A2401C, 0x1C40D001, 0x1840BD70, 0x0000BD70, 0x08192A3B, 0x40023C00, 0x4C5D6E7F,
        0x00005555, 0x40003000, 0x00000FFF, 0x0FFF0000, 0x0FFFAAEC, 0x0FFFFFFC, 0x00000000
    ],

    'pc_Init'            : 0x20000047,
    'pc_UnInit'          : 0x20000071,
    'pc_EraseSector'     : 0x200000AF,
    'pc_ProgramPage'     : 0x200000B3,
    'pc_Verify'          : 0x200000EB,
    'pc_EraseChip'       : 0x2000007F,
    'pc_BlankCheck'      : 0x12000001F,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x00000118,
    'rw_start'           : 0x00000118,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x0000011C,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x1FFFC000,
    'flash_size'         : 0x00000008,
    'flash_page_size'    : 0x00000008,
}
