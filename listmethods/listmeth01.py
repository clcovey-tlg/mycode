#!/usr/bin/env python3

def main():
    # list created and printed
    proto = ["ssh", "http", "https"]
    print(proto)
    print(proto[1])
    proto.extend("dns")
    print(proto)

if __name__ == "__main__":
	main()
