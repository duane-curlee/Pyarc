import os, sys
"""
This utility is like the Unix/Linux command du
"""
def du(the_folder):
    total_size = 0
    for root, dirs, files in os.walk(the_folder):
        for file in files:
            total_size = total_size + os.path.getsize(root + os.path.sep + file)
    return total_size

def human_readable(num_bytes):
    a_gig = 1073741824
    a_meg = 1048576
    a_kil = 1024

    if num_bytes >= a_gig:
        str_sizer = '{:.2f} GB'.format(num_bytes / a_gig)
    elif num_bytes >= a_meg:
        str_sizer = '{:.2f} MB'.format(num_bytes / a_meg)
    elif num_bytes >= a_kil:
        str_sizer = '{:.2f} KB'.format(num_bytes / a_kil)
    elif num_bytes == 1:
        str_sizer = '1 byte'
    elif num_bytes == 0:
        str_sizer = 'zero bytes'
    elif num_bytes < 0:
        str_sizer = 'negative number'
    else:
        str_sizer = '%d bytes' % num_bytes

    return str_sizer

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Total size of %s is: %s' % (os.getcwd(), human_readable(du(os.getcwd()))))
    else:
        for arg in sys.argv[1:]:
            if os.path.isdir(arg):
                print('Total size of %s is: %s' % (arg, human_readable(du(arg))))
            else:
                print('Folder not found: ' + arg + ' (skipping)')

