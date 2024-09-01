# Write your solution here
word_list = []
i = 0
while True:
    word = input("Word: ")

    if word in word_list:
        break
    
    word_list.append(word)
    i += 1

print("You typed in", i, "different words")
