"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0x8F4FF3BF, 0x02004770, 0x283F0D00, 0x0980D302, 0x47701D00, 0x477008C0, 0x49444845, 0x49456041,
        0x21006041, 0x68C16001, 0x431122F0, 0x694060C1, 0xD4060680, 0x49404841, 0x21066001, 0x49406041,
        0x20006081, 0x483A4770, 0x05426901, 0x61014311, 0x47702000, 0x4836B510, 0x24046901, 0x61014321,
        0x03A26901, 0x61014311, 0x4A344936, 0x6011E000, 0x03DB68C3, 0x6901D4FB, 0x610143A1, 0xBD102000,
        0xF7FFB530, 0x492AFFC0, 0x23F068CA, 0x60CA431A, 0x610C2402, 0x06C0690A, 0x43020E00, 0x6908610A,
        0x431003E2, 0x48276108, 0xE0004A24, 0x68CD6010, 0xD4FB03ED, 0x43A06908, 0x68C86108, 0x0F000600,
        0x68C8D003, 0x60C84318, 0xBD302001, 0x4D18B5F0, 0x08891CC9, 0x008968EB, 0x433B27F0, 0x230060EB,
        0x4C18612B, 0x692BE01D, 0x43334E17, 0x6813612B, 0xF3BF6003, 0x4B118F4F, 0x601CE000, 0x03F668EE,
        0x692BD4FB, 0x005B085B, 0x68EB612B, 0x0F1B061B, 0x68E8D004, 0x60E84338, 0xBDF02001, 0x1F091D00,
        0x29001D12, 0x2000D1DF, 0x0000BDF0, 0x45670123, 0x40023C00, 0xCDEF89AB, 0x00005555, 0x40003000,
        0x00000FFF, 0x0000AAAA, 0x00000201, 0x00000000
    ],

    'pc_Init'            : 0x20000039,
    'pc_UnInit'          : 0x20000067,
    'pc_EraseSector'     : 0x200000A1,
    'pc_ProgramPage'     : 0x200000ED,
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
    'ro_size'            : 0x0000014C,
    'rw_start'           : 0x0000014C,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x00000150,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x08000000,
    'flash_size'         : 0x00200000,
    'flash_page_size'    : 0x00000200,
}