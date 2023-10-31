#!/usr/bin/env python3

def main():
    # initial creation of two lists
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    print(proto)
    
    # appends "dns" to each list
    proto.append("dns") # this line will add "dns" to the end of our list
    protoa.append("dns") # this line will add "dns" to the end of our list
    print(proto)

    # creates a third list
    proto2 = [ 22, 80, 443, 53 ] # a list of common ports
    
    # extends thrid list to first list, basically combining lists
    proto.extend(proto2) # pass proto2 as an argument to the extend method
    print(proto)

    # appends third list to end of second list. This adds the list inside the list
    protoa.append(proto2) # pass proto2 as an argument to the append method
    print(protoa)
    
    # using list.count() to cound the number of times ssh appears in proto. expecting 1
    print(proto.count("ssh"))

    # using pop to remove first entry from proto and return it to a variable
    result = proto.pop(0)
    print(result)

    # prints how many times ssh now appears in proto
    print(proto.count("ssh"))

if __name__ == "__main__":
	main()
