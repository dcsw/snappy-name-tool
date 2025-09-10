import re
import sys

def shorten_name(name):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_name = re.sub(r'[^a-zA-Z]', '', name).lower()
    
    # Create a mapping of first letters to numbers
    letter_to_number = {chr(i): str(i - 96) for i in range(97, 123)}
    
    # Shorten the name
    shortened_name = ''.join(letter_to_number.get(char, char) for char in cleaned_name)
    
    return shortened_name

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python name_shortener.py <name>")
        sys.exit(1)
    
    name = sys.argv[1]
    shortened = shorten_name(name)
    print(shortened)
