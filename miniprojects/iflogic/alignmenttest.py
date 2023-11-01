#!/usr/bin/env python3

# import needed modules
import json
import os

# method to read questions from questions.txt file
def read_questions():
    # determines file path
    file_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(file_dir)
    
    # reads data from the file
    with open("questions.txt","r") as file:
        data = file.read()
    
    # reconstructs data into a dictionary
    questions = json.loads(data)
    return questions

# method to ask questions and record/return responses
def test(questions):
    # creates an empty dictionary to store responses
    responses = {}

    # iterates through questions and records responses 
    keys = list(questions)
    i = 0
    while i < len(questions):
        response = ""
        print(f"Question {i + 1}: {questions[keys[i]]['question']}")
        print(f"\tA) {questions[keys[i]]['a']}")
        print(f"\tB) {questions[keys[i]]['b']}")
        print(f"\tC) {questions[keys[i]]['c']}")
        print(f"\tD) {questions[keys[i]]['d']}")

        # ensure response is a valid choice
        while response not in ("a","b","c","d"):
            response = input("Please choose A, B, C, or D\n> ").lower()       
        
        # stores response
        responses[i] = response
        i += 1
    # returns a dictionary of resposes for analysis
    return responses

def main():
    os.system("clear")
    questions = read_questions()
    responses = test(questions)
    print(responses)

if __name__ == "__main__":
	main()
