#!/usr/bin/env python3

# import needed modules
import json
import os
import time

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
    # displays a message to user
    os.system("clear")
    print("""
This test will determine the alignment of your D&D character.
Please base your responses on how your character would respond.
These choices might not necessarily align with your personal beliefs\n""")
    input("Please press enter to continue with the test.")

    # creates an empty list to store responses
    responses = []

    # iterates through questions and records responses 
    keys = list(questions)
    i = 0
    while i < len(questions):
        os.system("clear")
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
        responses.append(response)
        i += 1
    # returns a list of resposes for scoring
    return responses

def score_responses(responses):
    # display a message to user and pauses for 3 seconds
    os.system("clear")
    print("Calculating results. Please wait...")
    time.sleep(3)

    #initializes morality (good vs evil) and ethic (law vs chaos) as 0
    law = 0
    chaos = 0
    good = 0
    evil = 0

    #scores responses
    i = 0
    while i < len(responses):
        if i == 2 or i == 6:
            match responses[i]:
                case "a":
                    law += 1
                    good += 1
                case "b":
                    chaos += 1
                    good += 1
                case "c":
                    law += 1
                    evil += 1
                case "d":
                    chaos += 1
                    evil += 1
        else:
            match responses[i]:
                case "a":
                    law += 1
                case "b":
                    good += 1
                case "c":
                    chaos += 1
                case "d":
                    evil += 1
        i += 1

    # add results to a dictonary for analysis
    results = {
        "law": law,
        "good": good,
        "chaos": chaos,
        "evil": evil
    }

    # returns results
    return results
    

def analyze_results(results):
    # determines scores for morality and ethics
    morality = results['good'] - results['evil']
    ethics = results['law'] - results['chaos']
    print(f"***This is for testing\n***{results}")
    print(f"***Morality - {morality}, Ethics - {ethics}")

    # assigns a alignment based upon scores
    alignment = ""
    # determines ethical beliefs
    if ethics > 1:
        alignment += "Lawful "
    elif ethics < -1:
        alignment += "Chaotic"
    else:
        alignment += "Neutral "

    # determines moral beliefs
    if morality > 1:
        alignment += "Good"
    elif morality < -1:
        alignment += "Evil"
    else:
        alignment += "Neutral"

    # changes value of alignment is fully Neutral
    if alignment == "Neutral Neutral":
        alignment = "True Neutral"
    
    return alignment
    

def display_alignment(alignment):
    # os.system("clear")
    print(f"Your characters alignment is {alignment}")
    print("Placeholder for alignment info. Info will be read from a text file")

def main():
    questions = read_questions()
    responses = test(questions)
    results = score_responses(responses)
    alignment = analyze_results(results)
    display_alignment(alignment)

if __name__ == "__main__":
	main()
