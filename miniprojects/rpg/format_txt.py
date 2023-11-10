#!/usr/bin/env python3

def underline(txt):
	"""
    Adds an underline effect to the input text.

    Parameters:
    - txt (str): The text to be underlined.

    Returns:
    - str: The input text with an underline effect.
    """
	return f"\x1B[4m{txt}\x1B[0m"

def make_red(txt):
	"""
    Changes the color of the input text to red.

    Parameters:
    - txt (str): The text to be colored red.

    Returns:
    - str: The input text with red color.
    """
	return f"\033[1;31;40m{txt}\033[0m"

def make_green(txt):
	"""
    Changes the color of the input text to green.

    Parameters:
    - txt (str): The text to be colored green.

    Returns:
    - str: The input text with green color.
    """
	return f"\033[1;32;40m{txt}\033[0m"

def make_blue(txt):
	"""
    Changes the color of the input text to blue.

    Parameters:
    - txt (str): The text to be colored blue.

    Returns:
    - str: The input text with blue color.
    """
	return f"\033[1;34;40m{txt}\033[0m"


def main():
	"""
    Test function to demonstrate the usage of the formatting functions.
    """
	print(underline("testy testy"))
	print(make_blue("blue"))
	print(make_green("green"))
	print(make_red("red"))

if __name__ == "__main__":
	main()