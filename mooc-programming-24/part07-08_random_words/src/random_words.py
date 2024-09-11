# Write your solution here
from random import sample

def words(n: int, beginning: str):
    matching = []
    with open("words.txt") as my_file:
        for line in my_file:
            line = line.strip()
            if line.startswith(beginning.lower()):
                matching.append(line)

    if len(matching) < n:
        raise ValueError("Not enough words in the list")
    else:
        for i in range(n):
            list_to_return = sample(matching, n)
            return list_to_return

if __name__ == "__main__":
    all_matching_word = words(3, "abigail")
    print(all_matching_word)


            
    

