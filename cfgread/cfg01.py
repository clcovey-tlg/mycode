#!/usr/bin/env python3
'''RZFeeser | Alta3 Research

Learning to read in files. This lab uses the following methods:

.read() - return the file's contents as a string
.readlines() - return the file's lines as a list
.seek() - move the cursor around an open file'''

def main():

    ######## EXPLORE READ ##########
    ## create file object in "r"ead mode
    configfile = open("vlanconfig.cfg", "r")

    ## display file to the screen - .read()
    print(configfile.read())

    # the "cursor" is now at the end of the file
    # we COULD close the file and reopen it to
    # move the cursor back to the top of the file

    ## close file
    #configfile.close()
    ## re-create file object to explore new method
    #configfile = open("vlanconfig.cfg", "r")

    # alternatively we can use the method `.seek`
    # this will move the cursor back to position 0,0
    # or the start of the file 
    configfile.seek(0, 0)

    
    ########## EXPLORE READLINES ##########
    ## make a list of file lines - .readlines()
    configlist = configfile.readlines()
    print(configlist)

    ## Iterate through configlist
    for x in configlist:
        print(x.strip())
        #print (x, end="") one solution to remove extra new lines

    ## Always close your file
    configfile.close()

if __name__ == "__main__":
    main()

