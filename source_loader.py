import tkinter as tk
import os.path

class SourceLoader:
    def __init__(self, binary_size, title = 'source file'):
        super.__init__()
        self.file_object = tk.Tk()
        self.initial_dir = os.path.curdir()
        self.window_title = title
    def load_binary(self):
        self.file_object.filename = tk.filedialog.askopenfilename(self.initial_dir, self.window_title, file_types = (("binary files","*.bin"), ("all files","*.*")))
        print (file_object.filename)