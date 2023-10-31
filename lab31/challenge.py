#!/usr/bin/env python3
import random

def main():
    #create two lists
    wordbank= ["indentation", "spaces"]
    tlgstudents = ["Bert", "Angel", "Chandan", "Chris", "Gen", "Jojo", "Joseph", "Robert", "Sar", "Zack"]

    # append int (4) to wordbank
    wordbank.append(4)

    # prompt user for input of an int between 0 and max class size
    num = input(f"Please enter a number between 0 and {len(tlgstudents)- 1}:\n>")
    
    # convert num input into an int
    # num = int(num)
    
    # Verified input is a int
    if num.isdigit():
        num = int(num)
        # slice student off of tlgstudents based upon num entered
        student_name = tlgstudents.pop(num)
        # print statement based upon student_name and last entry of wordbank
        print(f"{student_name} always uses {wordbank[-1]} spaces to indent.")
    else:
        print("Input was not a digit")

    #determines random student
    student_name2 = random.choice(tlgstudents)

    # prints statement based on random student
    print("This is a random student")
    print(f"{student_name2} always uses {wordbank[-1]} spaces to indent")

if __name__ == "__main__":
	main()
