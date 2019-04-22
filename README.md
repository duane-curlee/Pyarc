# pyarc
Python archiver, a Python script to create a backup zip file of your
selected folders.

A platform-independent GUI-based Python archiver tool that will make
a backup file (a zip file) in the fashion of cPanel's Backup program.
It will drop the zip archive in your home folder. It will allow you
to select your folders starting from your home folder.

The file name of the backup file should be in this format:

backup-(date-time-stamp).zip

## pyarc-cli
Python Archiver, command line interface, a Python script to create a backup
zip file of your folders of choice.

This is a platform-independent Python archiver tool that will make a backup
file (a zip file) in the fashion of cPanel's Backup program. It will drop
the zip archive in your current working directory. It will allow you to
select your folders on the command line and include them into the
archive, keeping the relative paths within the archive.

The file name of the backup file should be in this format:

pyarc-cli-(date-time-stamp).zip

## date and time stamp

The date and time stamp will be in this format:

year-month-day-hour-minute-second

Year is 4-digit, all others are 2-digits. This way, the zip file will
show when the archive was created, yet the operating system's date and
time stamp will show when the archive was last modified.
