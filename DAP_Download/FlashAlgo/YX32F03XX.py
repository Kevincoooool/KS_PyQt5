"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x4603B530, 0x2100460C, 0x4D342002, 0x20246028, 0x62A84D33, 0x60282002, 0x4D322001, 0xBF0060E8,
        0x1C49E000, 0x42814830, 0x2000D3FB, 0x4601BD30, 0x47702000, 0xE00E2100, 0x6081482A, 0x4A292004,
        0xBF006010, 0x68004827, 0x320122FF, 0xD1F94210, 0x31FF31FF, 0x20013102, 0x428103C0, 0x2000DBEC,
        0x46014770, 0x6081481F, 0x4B1E2004, 0x46186018, 0x68026802, 0x481BBF00, 0x23FF6800, 0x42183301,
        0x2000D1F9, 0xB5F04770, 0x46144603, 0x2200E022, 0xE00E2500, 0x1C647826, 0x463700D0, 0x433D4087,
        0x29001E49, 0x1C52D001, 0x2204E000, 0xD1002A04, 0x2A04E001, 0xBF00D1EE, 0x6083480A, 0x20026045,
        0x60384F08, 0x4807BF00, 0x27FF6800, 0x42383701, 0x1D1BD1F9, 0xD1DA2900, 0xBDF02000, 0x40004000,
        0x40048000, 0x50060000, 0x00002710, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000004F,
    'pc_EraseSector'     : 0x20000083,
    'pc_ProgramPage'     : 0x200000A7,
    'pc_Verify'          : 0x12000001F,
    'pc_EraseChip'       : 0x20000055,
    'pc_BlankCheck'      : 0x12000001F,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20000C00,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x000000EC,
    'rw_start'           : 0x000000EC,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x000000F0,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x00000000,
    'flash_size'         : 0x00008000,
    'flash_page_size'    : 0x00000200,
}
