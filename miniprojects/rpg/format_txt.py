#!/usr/bin/env python3

def underline(txt):
	return f"\x1B[4m{txt}\x1B[0m"

def make_red(txt):
	return f"\033[1;31;40m{txt}\033[0m"

def make_green(txt):
	return f"\033[1;32;40m{txt}\033[0m"

def make_blue(txt):
	return f"\033[1;34;40m{txt}\033[0m"


def main():
	print(underline("testy testy"))
	print(make_blue("blue"))
	print(make_green("green"))
	print(make_red("red"))

if __name__ == "__main__":
	main()