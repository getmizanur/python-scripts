__author__ = 'Mizanur Rahman <getmizanur@gmail.com>'

import os
import sys
import re

def grep(pattern, file_path):
    try:
        handler = open(file_path)
        lines = handler.readlines()
        handler.close()

        pat = re.compile(pattern)
        for line in lines:
            if pat.search(line):
                print file_path + ' : ' + line

    except IOError as e:
        print "Could not open the file. Moving to next one"

try:
    count = len(sys.argv)
    if count < 3:
        raise ValueError("Invalid number of arguments")
except ValueError as e:
    print str(e)
    exit()

regex = sys.argv[1]
files = sys.argv[2:]

for file in files:
    if(os.path.isdir(file)):
        for path, dirlist, filelist in os.walk(file):
            for name in filelist:
                grep(regex, os.path.join(path, name))
    else:
        grep(regex, file)



