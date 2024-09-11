# Write your solution here
import string

def change_case(orig_string: str):
    new_string = ""
    for char in orig_string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()

    return new_string

def split_in_half(orig_string: str):
    string_part1 = orig_string[:len(orig_string) // 2]
    string_part2 = orig_string[(len(orig_string) // 2):]

    return (string_part1, string_part2)

def remove_special_characters(orig_string: str):
    new_string = ""
    list_special_character = []
    for char in orig_string:
        if char in string.ascii_letters or char in string.digits or char == " ":
            new_string += char
    
    return new_string

if __name__ == "__main__":
    print(split_in_half("abcd"))