# Write your solution here
import string

def separate_characters(my_string: str):
    ascii_char = ""
    symbol_char = ""
    any_other_char = ""

    for char in my_string:
        if char in string.ascii_letters:
            ascii_char += char
        elif char in string.punctuation:
            symbol_char += char
        else:
            any_other_char += char

    return (ascii_char, symbol_char,any_other_char)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0]) 
    print(parts[1]) 
    print(parts[2]) 

