#!/usr/bin/env python3

# import needed modules
import json

# reads questions from questions.txt file
def read_questions():
    # determines file path
    file_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(file_dir)
    
    # reads data from the file
    with open('questions.txt') as file:
        data = file.read()

    # reconstructs data into a dictionary
    questions = json.loads(data)


def main():
    read_questions()
    print(questions)

if __name__ == "__main__":
	main()
