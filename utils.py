#!/usr/bin/python
import os
import fileinput
import sys

def search_and_replace(old, new):
    for root, dirs, files in os.walk('/home/'):
        for file in files:
            if file.endswith(".c"): #check only .c files
                print file
                for line in fileinput.input(os.path.abspath(os.path.join(root,
                    file)), inplace=True):
                    if old in line:
                        line = line.replace(old, new)
                        line = line.replace('log', 'log->log_level')
                    sys.stdout.write(line)

def main():
    replace_nginx_log('ngx_log_debug(', 'SE_DEBUG0(')

if __name__ == '__main__':
    main()
