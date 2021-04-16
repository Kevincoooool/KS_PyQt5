"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B510, 0xD0022A01, 0xD11D2A02, 0xBF00E000, 0x68004844, 0x6070F440, 0x60204C42, 0x4C414842,
        0x60203C0C, 0x60204841, 0x1D00483E, 0xF4106800, 0xD1081F80, 0x5055F245, 0x60204C3D, 0x60602006,
        0x70FFF640, 0xBF0060A0, 0x2000BF00, 0x4601BD10, 0xD0022901, 0xD10A2902, 0xBF00E000, 0x38144831,
        0xF0406800, 0x4A2F0001, 0x60103A14, 0xBF00BF00, 0x47702000, 0xF44F4601, 0xF1017280, 0xF02000FF,
        0xE00301FF, 0x20AAF64A, 0x60184B29, 0x68004825, 0x0F01F010, 0xE00DD1F6, 0x60082000, 0xF64AE003,
        0x4B2320AA, 0x481F6018, 0xF0106800, 0xD1F60F01, 0x1F121D09, 0xD1EF2A00, 0x47702000, 0x20014603,
        0xB5304770, 0xF44F4603, 0xF1017480, 0xF02000FF, 0xE00301FF, 0x20AAF64A, 0x60284D15, 0x68004811,
        0x0F01F010, 0xE017D1F6, 0x3814480E, 0xF4206800, 0x4D0C7080, 0x60283D14, 0x60186810, 0xF64AE003,
        0x4D0B20AA, 0x48076028, 0xF0106800, 0xD1F60F01, 0x1D121D1B, 0x1F241F09, 0x2C00B109, 0x2000D1E4,
        0x0000BD30, 0x40023C18, 0x89ABCDEF, 0x02030405, 0x40003000, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000006F,
    'pc_EraseSector'     : 0x20000095,
    'pc_ProgramPage'     : 0x200000E3,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x12000001F,
    'pc_BlankCheck'      : 0x200000DD,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x00000134,
    'rw_start'           : 0x00000134,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x00000138,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x08080000,
    'flash_size'         : 0x00003000,
    'flash_page_size'    : 0x00000100,
}
