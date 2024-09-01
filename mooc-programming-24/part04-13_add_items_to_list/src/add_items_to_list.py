# Write your solution here
items_number  = int(input("How maby items: "))
item_list = []
i = 0
while i < items_number:
    items = int(input(f"Item {i}: " ))
    item_list.append(items)
    i += 1

print(item_list)
