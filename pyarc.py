#!/usr/bin/python

import os, zipfile, datetime

os.chdir(os.path.expanduser('~'))
my_arcs = ('Notebooks', 'Code', 'Documents', 'Pictures', 'Videos', 'games')
exclusion_list = ('desktop.ini', 'Thumbs.db')
my_now = datetime.datetime.now()
my_fname = 'backup-' + my_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'

my_zip = zipfile.ZipFile(my_fname, 'w')

for arg in my_arcs:
    for root, dirs, files in os.walk(arg):
        for name in files:
            if name not in exclusion_list:
                my_zip.write(os.path.join(root, name), compress_type=zipfile.ZIP_DEFLATED)
        for name in dirs:
            my_zip.write(os.path.join(root, name) + os.path.sep, compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()
