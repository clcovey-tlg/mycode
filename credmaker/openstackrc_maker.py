#!/usr/bin/env python3

# open a new file named "admin.rc", make it appendable
#outFile = open("admin.rc", "a")
#using with to avoid having to close the file
with open("admin.rc", "a") as outFile:

# ask a series of inputs from user to get values
# add user's answer to the end of the "export XYZ" line
# print the completed line to our opened file
    osAUTH = input("What is the OS_AUTH_URL? ")
    print("export OS_AUTH_URL=" + osAUTH, file=outFile)

    print("export OS_IDENTITY_API_VERSION=3", file=outFile)

# further inputs/prints function the same as described above
    osPROJ = input("What is the OS_PROJECT_NAME? ")
    print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

    osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
    print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

    osUSER = input("What is the OS_USERNAME? ")
    print("export OS_USERNAME=" + osUSER, file=outFile)

    osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
    print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

    osPASS = input("What is the OS_PASSWORD? ")
    print("export OS_PASSWORD=" + osPASS, file=outFile)

# ALWAYS close files when finished with them!
#outFile.close()

