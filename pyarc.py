import tkinter as tk
from tkinter import filedialog
import os, zipfile, datetime

root = tk.Tk()
root.title('Pyarc version .1')
root.geometry('300x400')
exclusion_list = ('desktop.ini', 'Thumbs.db')
arc_folders = []
os.chdir(os.path.expanduser('~'))

def get_dir():
    global arc_folders
    folder_name =  filedialog.askdirectory()
    if len(folder_name) > 0:
        arc_folders.append(folder_name)
        btn_archive.config(state=tk.NORMAL)
        print('arc_folders is now: ')
        for i in arc_folders:
            print(i)

def archive_it():
    global arc_folders
    if len(arc_folders) > 0:
        the_now = datetime.datetime.now()
        zip_fname = 'backup-' + the_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'
        the_zip_file = zipfile.ZipFile(zip_fname, 'w')
        for arg in arc_folders:
            for root, dirs, files in os.walk(arg):
                for name in files:
                    if name not in exclusion_list:
                        the_zip_file.write(os.path.join(root, name), compress_type=zipfile.ZIP_DEFLATED)
                for name in dirs:
                    the_zip_file.write(os.path.join(root, name) + os.path.sep, compress_type=zipfile.ZIP_DEFLATED)
        the_zip_file.close()

    arc_folders = []
    btn_archive.config(state=tk.DISABLED)

frame_top = tk.Frame(root)
frame_top.pack(side = tk.TOP)
frame_bottom = tk.Frame(root)
frame_bottom.pack(side=tk.BOTTOM, fill = tk.X)

my_heading = tk.Label(frame_top, text="Select folders to archive")
my_heading.pack()

btn_close   = tk.Button(frame_bottom, text="Close",   width = 10, command=root.destroy)
btn_select  = tk.Button(frame_bottom, text="Select",  width = 10, command=get_dir)
btn_archive = tk.Button(frame_bottom, text="Archive", width = 10, command=archive_it, state=tk.DISABLED)
btn_close.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_select.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_archive.pack(side=tk.RIGHT, pady = 10, padx = 10)

root.mainloop()
