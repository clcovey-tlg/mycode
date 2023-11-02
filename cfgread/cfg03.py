#!/usr/bin/env python3

# prompt for file name
file_name = input("Enter the file name to process:\n>")

## create file object in "r"ead mode
with open(file_name, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(f"Lines - {len(configlist)}")
