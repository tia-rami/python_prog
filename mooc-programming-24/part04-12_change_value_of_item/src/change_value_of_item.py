# Write your solution here
list_to_change = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: ")) 

    if index == -1:
        break
    value = int(input("New value: ")) 

    list_to_change[index] = value
    print(list_to_change)
