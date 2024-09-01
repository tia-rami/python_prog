# Write your solution here
def anagrams(string_one, string_two):
    return False if sorted(string_one) != sorted(string_two) else True

if __name__ == '__main__':
    print(anagrams("tabby", "batty"))