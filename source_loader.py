import tkinter as tk
from tkinter import filedialog
import os

class SourceLoader:
    def __init__(self, binary_size, title = 'source file'):
        self.file_object = tk.Tk()
        self.initial_dir = os.getcwd()
        self.window_title = title
    def load_binary(self):
        self.file_object.filename = tk.filedialog.askopenfilename(initialdir = self.initial_dir, \
            title = self.window_title, filetypes = (("binary files","*.bin"), ("all files","*.*")))
        print (self.file_object.filename)
        return self.file_object.filename