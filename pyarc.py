import tkinter as tk
from tkinter import filedialog
import os, zipfile, datetime

exclusion_list = ('desktop.ini', 'Thumbs.db')
arc_folders = []
os.chdir(os.path.expanduser('~'))

if os.path.isfile('.pyarc.txt'):
    f = open('.pyarc.txt', 'r')
    f1 = f.readline()
    for x in f1:
        arc_folders.append(x)

def get_dir():
    global arc_folders
    folder_name =  filedialog.askdirectory(title = 'Your home folder', initialdir=os.path.expanduser('~'))
    if len(folder_name) > 0:
        print(folder_name)
        folder_name = "/".join(folder_name.strip("/").split('/')[3:])
        print(folder_name)
        arc_folders.append(folder_name)
        btn_archive.config(state=tk.NORMAL)
        the_hint.pack_forget()
        new_arc = tk.Label(frame_top, text=folder_name)
        new_arc.pack(side=tk.TOP, fill=tk.X)

# How to strip off the begining of path names in Windows
# "\\".join(folder_name.strip("\\").split('\\')[1:])
# in Linux or Unix, use / instead of \\
# https://stackoverflow.com/questions/26724275/removing-the-first-folder-in-a-path

def clear_it():
    arc_folders = []
    for widget in frame_top.winfo_children():
        widget.pack_forget()
    the_heading.pack(side=tk.TOP, fill=tk.X)
    btn_archive.config(state=tk.DISABLED)

def archive_it():
    global arc_folders
    if len(arc_folders) > 0:
        the_now = datetime.datetime.now()
        zip_fname = 'pyarc-' + the_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'
        the_zip_file = zipfile.ZipFile(zip_fname, 'w')
        for arg in arc_folders:
            for root, dirs, files in os.walk(arg):
                for name in files:
                    if name not in exclusion_list:
                        the_zip_file.write(os.path.join(root, name), compress_type=zipfile.ZIP_DEFLATED)
        the_zip_file.close()

root = tk.Tk()
root.title('Pyarc version 0.2')
root.geometry('400x300')
root.minsize(400, 300)

frame_top = tk.Frame(root)
frame_top.pack(side = tk.TOP, fill=tk.X)
frame_bottom = tk.Frame(root)
frame_bottom.pack(side=tk.BOTTOM, fill = tk.X)

the_heading = tk.Label(frame_top, text="Folders to archive:", background="grey63")
the_hint = tk.Label(frame_top, text="(No folders selected yet)\nClick the 'Select' button below to add folders.")
the_heading.pack(side=tk.TOP, fill=tk.X)
the_hint.pack(side=tk.TOP, fill=tk.X)

btn_close   = tk.Button(frame_bottom, text="Close",   width = 10, command=root.destroy)
btn_select  = tk.Button(frame_bottom, text="Select",  width = 10, command=get_dir)
btn_archive = tk.Button(frame_bottom, text="Archive", width = 10, command=archive_it, state=tk.DISABLED)
btn_close.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_select.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_archive.pack(side=tk.RIGHT, pady = 10, padx = 10)

root.mainloop()
