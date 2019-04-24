#!/usr/bin/python

import sys, os, zipfile, datetime

something_found = False
skip_hidden_dirs = True
skip_empty_dirs = True
skip_pyarc_cli_files = True

my_now = datetime.datetime.now()
my_fname = 'pyarc-cli-' + my_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'

if len(sys.argv) < 2:
    print('Exiting, command-line folders are required. No folders archived.')
else:
    my_zip = zipfile.ZipFile(my_fname, 'w')

    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            something_found = True
            for root, dirs, files in os.walk(arg):
                if skip_hidden_dirs == True:
                    dirs[:]  = [d for d in dirs  if not d.startswith('.')]
                if skip_pyarc_cli_files == True:
                    files[:] = [f for f in files if not f.startswith('pyarc-cli-')]
                for name in files:
                    print('Archiving: ' + os.path.join(root, name))
                    my_zip.write(os.path.join(root, name), compress_type=zipfile.ZIP_DEFLATED)
                if skip_empty_dirs == False:
                    for name in dirs:
                        my_zip.write(os.path.join(root, name), compress_type=zipfile.ZIP_DEFLATED)
        elif os.path.isfile(arg):
            print('Skipping, not a folder: ' + arg)
        else:
            print('Skipping, folder not found: ' + arg)

    my_zip.close()

    if something_found == True:
        print('Folders archived into: ' + my_fname)
    else:
        os.remove(my_zip.filename)
        print('No folders found, no archive created.')

