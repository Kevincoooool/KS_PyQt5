"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B510, 0xD0022A01, 0xD1232A02, 0xBF00E000, 0x68004849, 0x6070F440, 0x60204C47, 0x4C464847,
        0x60203C0C, 0x60204846, 0x4C434846, 0x60201F24, 0x60204845, 0x1D004840, 0xF4106800, 0xD1081F80,
        0x5055F245, 0x60204C41, 0x60602006, 0x70FFF640, 0xBF0060A0, 0x2000BF00, 0x4601BD10, 0xD0022901,
        0xD10F2902, 0xBF00E000, 0x38144833, 0xF0406800, 0x4A310004, 0x60103A14, 0x68004610, 0x0001F040,
        0xBF006010, 0x2000BF00, 0x48314770, 0x60084931, 0x60484831, 0x60884831, 0x610860C8, 0x61886148,
        0xE00361C8, 0x20AAF64A, 0x60084928, 0x68004822, 0x0F01F010, 0x4820D1F6, 0xF4106800, 0xD0076F70,
        0x6800481D, 0x6070F440, 0x6008491B, 0x47702001, 0xE7FC2000, 0x20004601, 0x46034770, 0x47702001,
        0x4603B510, 0x001FF101, 0x011FF020, 0x6818E01F, 0x42A06814, 0x6810D001, 0xE0036018, 0x20AAF64A,
        0x60204C12, 0x6800480C, 0x0F01F010, 0x480AD1F6, 0xF4106800, 0xD0076F70, 0x68004807, 0x6070F440,
        0x60204C05, 0xBD102001, 0x1D121D1B, 0x29001F09, 0x2000D1DD, 0x0000E7F7, 0x40023C18, 0x89ABCDEF,
        0x02030405, 0xFBEAD9C8, 0x24252627, 0x40003000, 0xFF5500AA, 0x1FF80000, 0xFF870078, 0xFFFF0000,
        0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000007B,
    'pc_EraseSector'     : 0x200000F5,
    'pc_ProgramPage'     : 0x20000101,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x200000AB,
    'pc_BlankCheck'      : 0x200000FB,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x00000160,
    'rw_start'           : 0x00000160,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x00000164,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x1FF80000,
    'flash_size'         : 0x00000020,
    'flash_page_size'    : 0x00000020,
}