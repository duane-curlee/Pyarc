#!/usr/bin/python

import sys
import os
import zipfile
import datetime

something_found = False
skip_dot_dirs = True
skip_empty_dirs = True
skip_pyarc_cli_files = True

if len(sys.argv) < 2:
    print('Exiting, command-line files or folders are required.',
          'No folders archived.')
    sys.exit(1)

my_now = datetime.datetime.now()
my_fname = 'pyarc-cli-' + my_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'
my_zip = zipfile.ZipFile(my_fname, 'w')

for arg in sys.argv[1:]:
    if os.path.isdir(arg):
        something_found = True
        for root, dirs, files in os.walk(arg):
            if skip_dot_dirs is True:
                dirs[:] = [d for d in dirs if not d.startswith('.')]
            if skip_pyarc_cli_files is True:
                files[:] = [f for f in files if not f.startswith('pyarc-cli-')]
            for name in files:
                arc_name = os.path.join(root, name)
                print('Archiving: ' + arc_name)
                my_zip.write(arc_name, compress_type=zipfile.ZIP_DEFLATED)
            if skip_empty_dirs is False:
                for name in dirs:
                    my_zip.write(os.path.join(root, name),
                                 compress_type=zipfile.ZIP_DEFLATED)
    elif os.path.isfile(arg):
        something_found = True
        print('Archiving: ' + arg)
        my_zip.write(arg, compress_type=zipfile.ZIP_DEFLATED)
    else:
        print('Skipping, file or folder not found: ' + arg)

my_zip.close()

if something_found is True:
    print('Folders archived into: ' + my_fname)
else:
    os.remove(my_zip.filename)
    print('No folders found, no archive created.')
    sys.exit(2)
