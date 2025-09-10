#!/usr/bin/python
import re
import sys

def shorten_name(name):
    # Take the first letter in lowercase
    first_letter = name[0].lower()
    
    # Count all non-whitespace characters remaining
    non_whitespace_count = len(re.sub(r'\s+', '', name)) - 2
    if non_whitespace_count < 0:
        non_whitespace_count = 0
    
    # Get the last letter in lowercase
    last_letter = name[-1].lower()
    
    # Shorten the name
    shortened_name = first_letter + str(non_whitespace_count) + last_letter
    
    return shortened_name

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python name_shortener.py <name>")
        sys.exit(1)
    
    name = sys.argv[1]
    shortened = shorten_name(name)
    print(shortened)
