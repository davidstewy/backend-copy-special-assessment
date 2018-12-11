#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import argparse

"""Copy Special exercise
"""


def get_special_paths(directory):
    file_list = os.listdir(directory)
    absol_path_list = []
    for file in file_list:
        special_pattern = re.findall(r'__\w+__', file)
        if special_pattern:
            absol_path_list.append(os.path.abspath(file))
    return absol_path_list


def copy_to(paths, directory):
    for path in paths:
        shutil.copy(path, directory)


def zip_to(paths, zip_path):
    print ("Command I'm going to do:\nzip -j "+zip_path)
    for path in paths:
        filezip = 'zip -j {} {}'.format(zip_path, path)
        os.system(filezip)
        print (path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory to search')
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    todir = args.todir
    tozip = args.tozip
    from_dir = args.from_dir

    if not from_dir:
        print 'This only works if you provide a directory to search'
        parser.print_usage()
        sys.exit(1)

    special_paths = get_special_paths(from_dir)

    if todir:
        copy_to(special_paths, todir)
    elif tozip:
        zip_to(special_paths, tozip)
    else:
        for path in special_paths:
            print path


if __name__ == "__main__":
    main()
