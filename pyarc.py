import tkinter as tk
import os, zipfile, datetime
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo

exclusion_list = ('desktop.ini', 'Thumbs.db')
arc_folders = []
settings_file = '.pyarc.txt'
os.chdir(os.path.expanduser('~'))

def popup_showinfo(the_string):
    showinfo("Just FYI", the_string)

def get_dir():
    global arc_folders
    folder_name =  askdirectory(title = 'Your home folder', initialdir=os.path.expanduser('~'))
    if len(folder_name) > 0:
        folder_name = "/".join(folder_name.strip("/").split('/')[3:])
        if folder_name in arc_folders:
            popup_showinfo("This folder is already in the archive list")
        else:
            add_new_arc(folder_name)
            f = open(settings_file, 'a+')
            f.write(folder_name + '\n')
            f.close()

def clear_all():
    global arc_folders
    arc_folders = []
    for widget in frame_top.winfo_children():
        widget.pack_forget()
    the_head.pack(side=tk.TOP, fill=tk.X)
    the_hint.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    btn_archive.config(state=tk.DISABLED)
    btn_clear.config(state=tk.DISABLED)
    if os.path.isfile(settings_file):
        os.remove(settings_file)

def archive_it():
    global arc_folders, root, btn_close, btn_select, btn_archive, btn_clear, exclusion_list
    root.config(cursor="wait")
    btn_close.config(state=tk.DISABLED)
    btn_select.config(state=tk.DISABLED)
    btn_archive.config(state=tk.DISABLED)
    btn_clear.config(state=tk.DISABLED)
    root.update()
    if len(arc_folders) > 0:
        the_now = datetime.datetime.now()
        zip_fname = 'pyarc-' + the_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'
        the_zip_file = zipfile.ZipFile(zip_fname, 'w')
        for arg in arc_folders:
            for the_root, dirs, files in os.walk(arg):
                for name in files:
                    if name not in exclusion_list:
                        the_zip_file.write(os.path.join(the_root, name), compress_type=zipfile.ZIP_DEFLATED)
        the_zip_file.close()
        popup_showinfo("Archive complete")
    root.config(cursor="")
    btn_close.config(state=tk.NORMAL)
    btn_select.config(state=tk.NORMAL)
    btn_archive.config(state=tk.NORMAL)
    btn_clear.config(state=tk.NORMAL)
    root.update()

root = tk.Tk()
root.title('Pyarc version 0.4')
root.geometry('400x300')
root.minsize(400, 300)

frame_top = tk.Frame(root)
frame_bottom = tk.Frame(root)

frame_top.pack(side = tk.TOP, fill=tk.BOTH, expand=True)
frame_bottom.pack(side=tk.BOTTOM, fill = tk.X)

the_head = tk.Label(frame_top, text="Folders to archive:", background="grey63", fg="white", font=("Helvetica", 10, "bold"))
the_hint = tk.Label(frame_top, text="(No folders selected yet)\nClick the 'Select' button below to add folders.")

the_head.pack(side=tk.TOP, fill=tk.X)
the_hint.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

btn_close   = tk.Button(frame_bottom, text="Close",   width = 10, command=root.destroy)
btn_select  = tk.Button(frame_bottom, text="Select",  width = 10, command=get_dir)
btn_archive = tk.Button(frame_bottom, text="Archive", width = 10, command=archive_it, state=tk.DISABLED)
btn_clear   = tk.Button(frame_bottom, text="Clear",   width = 10, command=clear_all, state=tk.DISABLED)

btn_close.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_select.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_archive.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_clear.pack(side=tk.RIGHT, pady = 10, padx = 10)

def add_new_arc(the_new_arc):
    global arc_folders
    arc_folders.append(the_new_arc)
    the_hint.pack_forget()
    new_arc = tk.Label(frame_top, text=the_new_arc)
    new_arc.pack(side=tk.TOP, fill=tk.X)
    btn_archive.config(state=tk.NORMAL)
    btn_clear.config(state=tk.NORMAL)

if os.path.isfile(settings_file):
    with open(settings_file, 'r') as f:
        for i in f.readlines():
            add_new_arc(i.strip())

root.mainloop()
