"""Program to find files and skip directories of a given directory"""
import os
entries = os.scandir('/home/admin1')                # setting directory to search files
for entry in entries:
    if entry.is_file():                         # only file names are printed
        print(entry.name)
