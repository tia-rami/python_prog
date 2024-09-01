# Write your solution here
list_of_value = []
ordered_list = []
while True:
    new_item = int(input("New item: "))

    if new_item == 0:
        break

    list_of_value.append(new_item)
    ordered_list = sorted(list_of_value)

    print("The list now:", list_of_value)
    print("The list in order:", ordered_list)

print("Bye!")