#!/usr/bin/python3
"""A basic threading example | rzfeeser@alta3.com"""

# Make a thread that simulates a NASA count down
# Wait 1 second at the bottom of each loop

## Python standard library
import threading

## py standard library
import time

def groundcontrol(x):
    for i in range(x, -1, -1):
        print(i)
        time.sleep(1)

def orion():
    print("I forgot my socks.")
    time.sleep(1)
    print("Can we stop this ride?")
    time.sleep(2)
    print("No? Alright. Ugh. I forgot to close the garage too.")
    time.sleep(1)
    print("To infinity, and beyond!")

print("Orion, you are primed for launch. Count down begins...")

countdown = 10

## Create a thread object (target is the function to call)
mythread = threading.Thread(target=groundcontrol, args=(countdown, ))

astrothread = threading.Thread(target=orion)

## begin the threads
mythread.start()
astrothread.start()

# Wait until the threads finish before moving on.
mythread.join()
astrothread.join()

## Ask the user to press any key to exit.
input("Press Enter to exit.")
exit()

