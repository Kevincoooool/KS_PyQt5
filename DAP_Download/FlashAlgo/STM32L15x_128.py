"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B510, 0xD0022A01, 0xD1242A02, 0xBF00E000, 0x6800487C, 0x6070F440, 0xF8C44C7B, 0x487B0C18,
        0x60204C7B, 0x6020487B, 0xF104487B, 0x60200404, 0x4C75487A, 0x0C10F8C4, 0x68004879, 0x1F80F410,
        0xF245D108, 0x4C775055, 0x20066020, 0xF6406060, 0x60A070FF, 0xBF00BF00, 0xBD102000, 0x29014601,
        0x2902D002, 0xE000D110, 0x486FBF00, 0xF0406800, 0x4A650002, 0x0C04F8C2, 0xF8D04610, 0xF0400C04,
        0xF8C20001, 0xBF000C04, 0x2000BF00, 0x46014770, 0x68004865, 0x7000F440, 0xF8C24A5B, 0x46100C04,
        0x0C04F8D0, 0x0008F040, 0x0C04F8C2, 0x0000F04F, 0xE0036008, 0x20AAF64A, 0x60104A5A, 0x68004851,
        0x0F01F010, 0x4858D1F6, 0xF4206800, 0x4A4E7000, 0x0C04F8C2, 0xF8D04610, 0xF0200C04, 0xF8C20008,
        0xF04F0C04, 0x47700000, 0x20014603, 0xB5304770, 0x24804603, 0x00FFF101, 0x01FFF020, 0x6800484A,
        0x6080F440, 0xF8C54D40, 0x46280C04, 0x0C04F8D0, 0x0008F040, 0x0C04F8C5, 0xE005BF00, 0x60186810,
        0x1D121D1B, 0x1F241F09, 0x2C00B109, 0xE003D1F6, 0x20AAF64A, 0x60284D3B, 0x68004832, 0x0F01F010,
        0x4830D1F6, 0xF4106800, 0xD0096F70, 0x6800482D, 0x6070F440, 0xF8C54D2C, 0xF04F0C18, 0xBD300001,
        0x68004831, 0x6080F420, 0xF8C54D27, 0x46280C04, 0x0C04F8D0, 0x0008F020, 0x0C04F8C5, 0xF8D04628,
        0xF4400C04, 0xF8C56080, 0x46280C04, 0x0C04F8D0, 0x0008F040, 0x0C04F8C5, 0x0480F04F, 0x6810E005,
        0x1D1B6018, 0x1F091D12, 0xB1091F24, 0xD1F62C00, 0xF64AE003, 0x4D1B20AA, 0x48126028, 0xF0106800,
        0xD1F60F01, 0x6800480F, 0x6F70F410, 0x480DD009, 0xF4406800, 0x4D0C6070, 0x0C18F8C5, 0x0001F04F,
        0x4811E7BD, 0xF4206800, 0x4D076080, 0x0C04F8C5, 0xF8D04628, 0xF0200C04, 0xF8C50008, 0xF04F0C04,
        0xE7AC0000, 0x40023C18, 0x40023000, 0x89ABCDEF, 0x40023C0C, 0x02030405, 0x8C9DAEBF, 0x13141516,
        0x40023C1C, 0x40003000, 0x40023C04, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000007D,
    'pc_EraseSector'     : 0x200000AF,
    'pc_ProgramPage'     : 0x2000010F,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x12000001F,
    'pc_BlankCheck'      : 0x20000109,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x0000022C,
    'rw_start'           : 0x0000022C,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x00000230,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x08000000,
    'flash_size'         : 0x00020000,
    'flash_page_size'    : 0x00000100,
}