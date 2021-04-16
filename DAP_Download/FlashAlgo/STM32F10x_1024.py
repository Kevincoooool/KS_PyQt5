"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B510, 0x04C00CD8, 0x444C4C80, 0x20006020, 0x60204C7F, 0x6060487F, 0x6060487F, 0x6460487D,
        0x6460487D, 0x69C04620, 0x0F04F010, 0xF245D108, 0x4C7A5055, 0x20066020, 0xF6406060, 0x60A070FF,
        0xBD102000, 0x48724601, 0xF0406900, 0x4A700080, 0x46106110, 0xF0406D00, 0x65100080, 0x47702000,
        0x6900486B, 0x0004F040, 0x61084969, 0x69004608, 0x0040F040, 0xE0036108, 0x20AAF64A, 0x60084967,
        0x68C04863, 0x0F01F010, 0x4861D1F6, 0xF0206900, 0x495F0004, 0x46086108, 0xF0406D00, 0x65080004,
        0x6D004608, 0x0040F040, 0xE0036508, 0x20AAF64A, 0x6008495A, 0x6CC04856, 0x0F01F010, 0x4854D1F6,
        0xF0206D00, 0x49520004, 0x20006508, 0x46014770, 0x4448484E, 0xF5006800, 0x42812000, 0x484CD21C,
        0xF0406900, 0x4A4A0002, 0x46106110, 0x69006141, 0x0040F040, 0xE0036110, 0x20AAF64A, 0x60104A47,
        0x68C04843, 0x0F01F010, 0x4841D1F6, 0xF0206900, 0x4A3F0002, 0xE01B6110, 0x6D00483D, 0x0002F040,
        0x65104A3B, 0x65414610, 0xF0406D00, 0x65100040, 0xF64AE003, 0x4A3920AA, 0x48356010, 0xF0106CC0,
        0xD1F60F01, 0x6D004832, 0x0002F020, 0x65104A30, 0x47702000, 0x4603B510, 0xF0201C48, 0x482B0101,
        0x68004448, 0x2000F500, 0xD2264283, 0x4828E022, 0xF0406900, 0x4C260001, 0x88106120, 0xBF008018,
        0x68C04823, 0x0F01F010, 0x4821D1FA, 0xF0206900, 0x4C1F0001, 0x46206120, 0xF01068C0, 0xD0060F14,
        0x68C04620, 0x0014F040, 0x200160E0, 0x1C9BBD10, 0x1E891C92, 0xD1DA2900, 0xE022E025, 0x6D004814,
        0x0001F040, 0x65204C12, 0x80188810, 0x4810BF00, 0xF0106CC0, 0xD1FA0F01, 0x6D00480D, 0x0001F020,
        0x65204C0B, 0x6CC04620, 0x0F14F010, 0x4620D006, 0xF0406CC0, 0x64E00014, 0xE7D72001, 0x1C921C9B,
        0x29001E89, 0x2000D1DA, 0x0000E7D0, 0x00000004, 0x40022000, 0x45670123, 0xCDEF89AB, 0x40003000,
        0x00000000, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x20000065,
    'pc_EraseSector'     : 0x200000EF,
    'pc_ProgramPage'     : 0x20000175,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x20000081,
    'pc_BlankCheck'      : 0x12000001F,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20001000,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x00000220,
    'rw_start'           : 0x00000220,
    'rw_size'            : 0x00000008,
    'zi_start'           : 0x00000228,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x08000000,
    'flash_size'         : 0x00100000,
    'flash_page_size'    : 0x00000400,
}
