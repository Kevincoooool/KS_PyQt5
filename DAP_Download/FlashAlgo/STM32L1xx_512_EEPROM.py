"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B510, 0xD0022A01, 0xD11D2A02, 0xBF00E000, 0x68004846, 0x6070F440, 0x60204C44, 0x4C434844,
        0x60203C0C, 0x60204843, 0x1D004840, 0xF4006800, 0xB9401080, 0x5055F245, 0x60204C3F, 0x60602006,
        0x70FFF640, 0xBF0060A0, 0x2000BF00, 0x4601BD10, 0xD0022901, 0xD10A2902, 0xBF00E000, 0x38144833,
        0xF0406800, 0x4A310001, 0x60103A14, 0xBF00BF00, 0x47702000, 0xF44F4601, 0xF1017280, 0xF02000FF,
        0xE00301FF, 0x20AAF64A, 0x60184B2B, 0x68004827, 0x0001F000, 0xD1F52800, 0x2000E00E, 0xE0036008,
        0x20AAF64A, 0x60184B24, 0x68004820, 0x0001F000, 0xD1F52800, 0x1F121D09, 0xD1EE2A00, 0x47702000,
        0x20014603, 0xB5304770, 0xF44F4603, 0xF1017480, 0xF02000FF, 0xE00301FF, 0x20AAF64A, 0x60284D16,
        0x68004812, 0x0001F000, 0xD1F52800, 0x480FE018, 0x68003814, 0x7080F420, 0x3D144D0C, 0x68106028,
        0xE0036018, 0x20AAF64A, 0x60284D0B, 0x68004807, 0x0001F000, 0xD1F52800, 0x1D121D1B, 0x1F241F09,
        0x2C00B109, 0x2000D1E3, 0x0000BD30, 0x40023C18, 0x89ABCDEF, 0x02030405, 0x40003000, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000006F,
    'pc_EraseSector'     : 0x20000095,
    'pc_ProgramPage'     : 0x200000E7,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x12000001F,
    'pc_BlankCheck'      : 0x200000E1,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x0000013C,
    'rw_start'           : 0x0000013C,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x00000140,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x08080000,
    'flash_size'         : 0x00004000,
    'flash_page_size'    : 0x00000100,
}
