#!/usr/bin/python
import os
import fileinput
import sys

#This function searches for an 'old' string
#and replaces it with 'new' string in all .py
#files within the /home/ directory
def search_and_replace(old, new):
    for root, dirs, files in os.walk('/home/'):
        for file in files:
            if file.endswith(".py"): #check only .py files
                print file
                for line in fileinput.input(os.path.abspath(os.path.join(root,
                    file)), inplace=True):
                    if old in line:
                        line = line.replace(old, new)
                    sys.stdout.write(line)


