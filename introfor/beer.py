#!/usr/bin/env python3

def count_input():
    count = 0
    while not 0 < count <= 100:
        try:
            count = int(input("How many bottles of beer are there?(from 1 and 100)\n> "))
        except:
            print("You must enter a whole number from 1 to 100")
    return count

def count_beer(count):
    for x in range(count, -1, -1):
        if x == 0:
            print("Party is over!! All the beer is gone")
        else:
            print(f"{x} bottles of beer on the wall!")
            print(f"{x} bottles of beer on the wall! {x} bottles of beer! You take one down, pass it around!")

def main():
    count = count_input()
    count_beer(count)
    
if __name__ == "__main__":
	main()
