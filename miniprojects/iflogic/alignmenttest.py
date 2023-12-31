#!/usr/bin/env python3

# import needed modules
import json
import os
import time
import textwrap

# method to read questions from questions.txt file
def read_questions():
    """
    Read questions from the 'questions.txt' file and reconstructs them into a dictionary.

    Returns:
    Dict: Dictionary containing questions and answer choices.
    """
    file_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(file_dir)
    
    with open("questions.txt","r") as file:
        data = file.read()
    
    questions = json.loads(data)
    return questions

def read_descriptions():
    """
    Read alignment descriptions from the 'alignment_descriptions.txt' file and reconstructs
    them into a dictionary.

    Returns:
    Dict: Dictionary containing alignment descriptions.
    """
    file_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(file_dir)
    
    with open("alignment_descriptions.txt","r") as file:
        data = file.read()
    
    descriptions = json.loads(data)
    return descriptions

def test(questions):
    """
    Ask questions and record/return responses.

    Args:
    questions (Dict): Dictionary containing questions and answer choices.

    Returns:
    list: List of responses for scoring.
    """
    os.system("clear")
    print("""
This test will determine the alignment of your D&D character.
Please base your responses on how your character would respond.
These choices might not necessarily align with your personal beliefs\n""")
    input("Please press enter to continue with the test.")

    responses = []

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

        while response not in ("a","b","c","d"):
            response = input("Please choose A, B, C, or D\n> ").lower()       
        
        responses.append(response)
        i += 1
    return responses

def score_responses(responses):
    """
    Score the responses and return a dictionary with scores for morality and ethics.

    Args:
    responses (list): List of responses for scoring.

    Returns:
    Dict: Dictionary containing scores for morality and ethics.
    """
    os.system("clear")
    print("Calculating results. Please wait...")
    time.sleep(3)

    #initializes morality (good vs evil) and ethic (law vs chaos) as 0
    law = 0
    chaos = 0
    good = 0
    evil = 0

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
    """
    Analyze the results and determine the character's alignment.

    Args:
    results (Dict): Dictionary containing scores for morality and ethics.

    Returns:
    str: Character's alignment.
    """
    morality = results['good'] - results['evil']
    ethics = results['law'] - results['chaos']

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
    

def display_alignment(alignment, descriptions):
    """
    Display the character's alignment along with a description.

    Args:
    alignment (str): Character's alignment.
    descriptions (Dict): Dictionary containing alignment descriptions.

    Returns:
    None
    """
    os.system("clear")
    print(f"\x1B[4mYour characters alignment is {alignment}\x1B[0m")

    wrapper = textwrap.TextWrapper(width=50)
    descrip = wrapper.fill(text=descriptions[alignment])
    print(descrip)

def take_test():
    """
    Perform the alignment test, analyze results, and display the character's alignment.

    Returns:
    str: Character's alignment.
    """
    questions = read_questions()
    descriptions = read_descriptions()
    responses = test(questions)
    results = score_responses(responses)
    alignment = analyze_results(results)
    display_alignment(alignment, descriptions)

    return alignment

def main():
    """
    Main function to execute the alignment test.

    Returns:
    None
    """
    alignment = take_test()
    print(alignment)

if __name__ == "__main__":
	main()
