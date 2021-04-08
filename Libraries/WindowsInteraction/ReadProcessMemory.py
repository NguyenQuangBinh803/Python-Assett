import ctypes, win32ui, win32process, win32api

if __name__ == "__main__":
    PROCESS_ALL_ACCESS = 0x1F0FFF
    HWND = win32ui.FindWindow(None, "Settings").GetSafeHwnd()
    print("Handle Windows: ", HWND)
    PID = win32process.GetWindowThreadProcessId(HWND)[1]
    print("Process ID: ", PID)
    PROCESS = win32api.OpenProcess(PROCESS_ALL_ACCESS, 0, PID).handle

    rPM = ctypes.windll.kernel32.ReadProcessMemory
    wPM = ctypes.windll.kernel32.WriteProcessMemory

    ADDRESS1 = 0x00E97074
    ADDRESS2 = ctypes.create_string_buffer(64)
    pi = ctypes.pointer(ADDRESS2)
    rPM(PROCESS, ADDRESS1, ADDRESS2, 64, 0)
    print("Read Memories: ", rPM)
    x = ctypes.windll.kernel32.GetLastError()
    print(x)
