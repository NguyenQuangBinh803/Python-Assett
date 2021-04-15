class Dialog:
    def __init__(self):
        print("Init an dialog")
    
    def draw_windows(self):
        print("Menubar is being drew")

class FileDialog(Dialog):
    def __init__(self):
        super().__init()

    def draw_windows(self):
        print("This is FileDialog")

class MessageBox(Dialog):
    def __init__(self):
        super().__init()

    def draw_windows(self):
        print("This is MessageBox")



