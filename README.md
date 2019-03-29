# pyarc
Python archiver, a script to create a backup zip file of your files and folders

Hello, world.

I am making a platform-independent Python archiver that will make a backup file (a zip file) in the fashion of cPanel's Backup program. It should drop the zip archive in your home folder. It will allow you to select your folders from your home folder and remember your choices. I plan to make it GUI-based, but it is only command line as of now.

The file name of the backup file should be in this format: backup-(date-time-stamp).zip where the date and time stamp will be in this format:

year-month-day-hour-minute-second

Year is 4-digit, all others are 2-digits. This way the zip file will show when the archive was created, yet the operating system will show when the archive was last modified.
