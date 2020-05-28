# About pyarc.py
This Python script, pyarc.py, or Python Archiver, is a tkinter-based GUI
program for creating zipped backup files of your choosen files and/or folders.

This script is intended to be a platform-independent GUI-based backup tool
that will make a zip file in the fashion of cPanel's Backup program. It
allows you to choose your folders, but they must be in your home folder, and
will save your choices for the next time you run Pyarc into this file:

```~/pyarc-settings.txt```

Right now, this utility is still under construction, new updates will be
posted here. It has only been tested to work on Windows.

After you press the 'Archive' button, Pyarc will then make and drop a zip
archive in your home folder. The filename of the backup file will be in this
format:

```~/Backup-(date-time-stamp).zip```

## About the date and time stamp

The date and time stamp will be in this format:

year-month-day-hour-minute-second

sample: backup-2020-05-25-14-07-38.zip

Which is May 25, 2020, at 2:07pm and 38 seconds.

Year is always 4-digit, all others are 2-digits. This way, the zip file will
show when the archive was created, yet the operating system's date and time
stamp will change and show when the archive was last modified. Also this
format allows the backup files to be sorted based on age.
