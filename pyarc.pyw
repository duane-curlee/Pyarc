import tkinter as tk
import os
import zipfile
from datetime import datetime
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pyarc version 0.5')
        self.geometry('400x300')
        self.minsize(400, 300)
        self.exclusion_list = ('desktop.ini', 'Thumbs.db')
        self.arc_folders = []
        self.home_folder = os.path.expanduser('~')
        self.settings_file = os.path.join(self.home_folder, 'pyarc-settings.txt')

        self.frame_top = tk.Frame(self)
        self.frame_bot = tk.Frame(self)

        self.the_head = tk.Label(self.frame_top,
            text="Folders to archive:",
            background="grey63",
            fg="white",
            font=("Helvetica", 10, "bold"))
        self.the_hint = tk.Label(self.frame_top,
            text="No folders added yet\n\
            (Click the 'Add' button below to get started.)")
        self.the_busy = tk.Label(self.frame_top,
            text="Archiving...\n\
            (Please wait)")

        self.btn_close   = tk.Button(self.frame_bot, text="Close",   width = 10, command=self.destroy, state=tk.NORMAL)
        self.btn_clear   = tk.Button(self.frame_bot, text="Clear",   width = 10, command=self.clear,   state=tk.NORMAL)
        self.btn_add     = tk.Button(self.frame_bot, text="Add",     width = 10, command=self.add,     state=tk.NORMAL)
        self.btn_archive = tk.Button(self.frame_bot, text="Archive", width = 10, command=self.archive, state=tk.NORMAL)

        self.frame_top.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.frame_bot.pack(side = tk.BOTTOM, fill = tk.X)

        self.the_head.pack(side=tk.TOP, fill=tk.X)

        if os.path.isfile(self.settings_file):
            with open(self.settings_file, 'r') as f:
                for i in f.readlines():
                    self.add_new_entry(i.strip())
        else:
            self.the_hint.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            self.btn_archive.config(state=tk.DISABLED)
            self.btn_clear.config(state=tk.DISABLED)

        self.btn_close.pack(side=tk.RIGHT, pady = 10, padx = 10)
        self.btn_clear.pack(side=tk.RIGHT, pady = 10, padx = 10)
        self.btn_add.pack(side=tk.RIGHT, pady = 10, padx = 10)
        self.btn_archive.pack(side=tk.RIGHT, pady = 10, padx = 10)

    def popup_showinfo(self, the_string):
        showinfo("Just FYI", the_string)

    def add_new_entry(self, the_new_arc):
        self.arc_folders.append(the_new_arc)
        new_arc = tk.Label(self.frame_top, text=the_new_arc)
        new_arc.pack(side=tk.TOP, fill=tk.X)
        self.the_hint.pack_forget()
        self.btn_archive.config(state=tk.NORMAL)
        self.btn_clear.config(state=tk.NORMAL)

    def clear(self):
        self.arc_folders = []
        for widget in self.frame_top.winfo_children():
            widget.pack_forget()
        self.the_head.pack(side=tk.TOP, fill=tk.X)
        self.the_hint.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.btn_archive.config(state=tk.DISABLED)
        self.btn_clear.config(state=tk.DISABLED)
        if os.path.isfile(self.settings_file):
            os.remove(self.settings_file)

    def add(self):
        folder_name =  askdirectory(title = 'Your home folder', initialdir = self.home_folder)
        if len(folder_name) > 0:
            folder_name = "/".join(folder_name.strip("/").split('/')[3:])
            if folder_name in self.arc_folders:
                self.popup_showinfo("This folder is already in the archive list")
            else:
                self.add_new_entry(folder_name)
                with open(self.settings_file, 'a+') as f:
                    f.write(folder_name + '\n')

    def archive(self):
        self.config(cursor="wait")
        self.btn_close.config(state=tk.DISABLED)
        self.btn_add.config(state=tk.DISABLED)
        self.btn_archive.config(state=tk.DISABLED)
        self.btn_clear.config(state=tk.DISABLED)
        self.update()

        os.chdir(self.home_folder)
        the_now = datetime.now()
        the_fname = 'pyarc-' + the_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'
        zip_fname = os.path.join(self.home_folder, the_fname)
        the_zip_file = zipfile.ZipFile(zip_fname, 'w')

        for arg in self.arc_folders:
            for the_root, dirs, files in os.walk(arg):
                for name in files:
                    if name not in self.exclusion_list:
                        the_zip_file.write(os.path.join(the_root, name),
                            compress_type = zipfile.ZIP_DEFLATED)

        self.config(cursor="")
        self.btn_close.config(state=tk.NORMAL)
        self.btn_add.config(state=tk.NORMAL)
        self.btn_archive.config(state=tk.NORMAL)
        self.btn_clear.config(state=tk.NORMAL)
        self.update()

        the_zip_file.close()
        the_end = datetime.now()
        self.popup_showinfo("Archive complete")


if __name__ == '__main__':
    root = Root()
    root.mainloop()
