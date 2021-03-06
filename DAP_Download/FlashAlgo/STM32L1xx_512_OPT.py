"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B510, 0xD0022A01, 0xD1232A02, 0xBF00E000, 0x6800485F, 0x6070F440, 0x60204C5D, 0x4C5C485D,
        0x60203C0C, 0x6020485C, 0x4C59485C, 0x60201F24, 0x6020485B, 0x1D004856, 0xF4006800, 0xB9401080,
        0x5055F245, 0x60204C57, 0x60602006, 0x70FFF640, 0xBF0060A0, 0x2000BF00, 0x4601BD10, 0xD0022901,
        0xD10F2902, 0xBF00E000, 0x38144849, 0xF0406800, 0x4A470004, 0x60103A14, 0x68004610, 0x0001F040,
        0xBF006010, 0x2000BF00, 0x48474770, 0x60084947, 0x60484847, 0x60884847, 0x610860C8, 0x61886148,
        0x494261C8, 0x60083180, 0xF8C14940, 0xE0030084, 0x20AAF64A, 0x6008493B, 0x68004835, 0x0001F000,
        0xD1F52800, 0x68004832, 0x6070F400, 0x4830B138, 0xF4406800, 0x492E6070, 0x20016008, 0x20004770,
        0x4601E7FC, 0x47702000, 0x20014603, 0xB5304770, 0x24004603, 0xE0252128, 0x68155918, 0xD00142A8,
        0x51186810, 0xF64AE003, 0x4D2620AA, 0x48206028, 0xF0006800, 0x28000001, 0x481DD1F5, 0xF4006800,
        0xB1386070, 0x6800481A, 0x6070F440, 0x60284D18, 0xBD302001, 0x1D121D1B, 0x481C1F09, 0x42833020,
        0x2460D100, 0xD1D72900, 0xE7F22000, 0x4603B530, 0x21282400, 0x5918E018, 0x42A86815, 0x4618D001,
        0xE003BD30, 0x20AAF64A, 0x60284D0E, 0x68004808, 0x0001F000, 0xD1F52800, 0x1D121D1B, 0x480B1F09,
        0x42833020, 0x2460D100, 0xD1E42900, 0xE7E71858, 0x40023C18, 0x89ABCDEF, 0x02030405, 0xFBEAD9C8,
        0x24252627, 0x40003000, 0xFF5500AA, 0x1FF80000, 0xFF870078, 0xFFFF0000, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000007B,
    'pc_EraseSector'     : 0x20000103,
    'pc_ProgramPage'     : 0x2000010F,
    'pc_Verify'          : 0x2000016D,
    'pc_EraseChip'       : 0x200000AB,
    'pc_BlankCheck'      : 0x20000109,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x000001B8,
    'rw_start'           : 0x000001B8,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x000001BC,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x1FF80000,
    'flash_size'         : 0x00000028,
    'flash_page_size'    : 0x00000028,
}
