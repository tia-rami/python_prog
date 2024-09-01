# Write your solution here
i = 1
list_to_change = []

while True:
    print("The list is now", list_to_change)
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == 'x':
        break
    if choice == 'd':
        list_to_change.append(i)
        i += 1
    elif  choice == 'r':
        list_to_change.pop(-1)
        i -= 1

print("Bye!")

