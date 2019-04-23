#!/usr/bin/python

import sys, os, zipfile, datetime

my_now = datetime.datetime.now()
my_fname = 'pyarc-cli-' + my_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'
something_found = False

if len(sys.argv) < 2:
    print('Exiting, command-line folders are required. No folders archived.')
else:
    my_zip = zipfile.ZipFile(my_fname, 'w')

    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            something_found = True
            for root, dirs, files in os.walk(arg):
                dirs[:]  = [d for d in dirs  if not d.startswith('.')]
                files[:] = [f for f in files if not f.startswith('pyarc-cli-')]
                for name in files:
                    print('Archiving: ' + os.path.join(root, name))
                    my_zip.write(os.path.join(root, name), compress_type=zipfile.ZIP_DEFLATED)
        else:
            print('Skipping, folder not found: ' + arg)

    my_zip.close()

    if something_found == True:
        print('Folders archived into: ' + my_fname)
    else:
        os.remove(my_zip.filename)
        print('No folders found, no archive created.')

