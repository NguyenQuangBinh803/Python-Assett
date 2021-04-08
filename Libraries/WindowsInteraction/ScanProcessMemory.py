from ctypes import *
from ctypes.wintypes import *

PROCESS_ID = 4696 # From TaskManager for Notepad.exe
PROCESS_HEADER_ADDR = 0x271A2170000 # From SysInternals VMMap utility

# read from addresses
STRLEN = 6500

PROCESS_VM_READ = 0x0010
if __name__ == "__main__":
    k32 = WinDLL('kernel32')
    k32.OpenProcess.argtypes = DWORD,BOOL,DWORD
    k32.OpenProcess.restype = HANDLE
    k32.ReadProcessMemory.argtypes = HANDLE,LPVOID,LPVOID,c_size_t,POINTER(c_size_t)
    k32.ReadProcessMemory.restype = BOOL

    process = k32.OpenProcess(PROCESS_VM_READ, 0, PROCESS_ID)
    buf = create_string_buffer(STRLEN)
    s = c_size_t()
    if k32.ReadProcessMemory(process, PROCESS_HEADER_ADDR, buf, STRLEN, byref(s)):
        print(s.value,buf.raw.decode("utf-8","ignore"))
