#!/usr/bin/env python3

# imports standard libraries
import shutil
import os

def main():
    # changes dir to working directory
    os.chdir('/home/student/mycode/')
    
    # moves the file to a new location
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompts user for a new name for kerrigan.obj
    xname = input('What is the new name for kerrigan.obj? ')

    # changes name by moving file into the same location with a new name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ = "__main__":
    main()

