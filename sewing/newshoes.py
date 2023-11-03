#!/usr/bin/python3
"""A basic threading example | rzfeeser@alta3.com"""

# Make a thread that simulates a NASA count down
# Wait 1 second at the bottom of each loop

## Python standard library
import threading

## py standard library
import time

def groundcontrol():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

print("Orion, you are primed for launch. Count down begins...")

## Create a thread object (target is the function to call)
mythread = threading.Thread(target=groundcontrol)

## begin the thread
mythread.start()

print("Oh no, I forgot socks!")

# Wait until the threads finish before moving on.
mythread.join()

## Ask the user to press any key to exit.
input("Press Enter to exit.")
exit()

