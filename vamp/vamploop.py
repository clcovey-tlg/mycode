#!/usr/bin/env python3
def vamp_line():
    line_count = 0

    with open("dracula.txt", "r") as drac_txt:
        #print(drac_txt.read())
        with open("vampytimes.txt", "a") as vamp:
            for line in drac_txt:
                if "vampire" in line.lower():
                    print(line)
                    #vamp.write(line)
                    line_count += 1
      
    print(f"vampire appears on {line_count} lines")

def vamp_word(search_word):
    word_count = 0
    with open("dracula.txt", "r") as drac_txt:
        for line in drac_txt:
            for word in line.split(" "):
                if "vampire" in word.lower():
                    word_count +=1
                
    print(f"vampire appears {word_count} times") 

def main():
    vamp_line()
    vamp_word("vampire")

if __name__ == "__main__":
	main()
