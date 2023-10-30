#~/usr/bin/env python3

def main():
    # prompt user for input of name
    name = input("What is your name?\n>")

    # prompts user for day of the week
    day_of_week = input("What is the day of the week?\n>")
    
    # prints messages to user
    print(f"Hello, {name}! Happy {day_of_week}")

if __name__ == "__main__":
    main()
