# Write your solution here
import json

def print_persons(file_name: str):
    with open(file_name) as my_file:
        data = my_file.read()
    persons = json.loads(data)

    for person in persons:
        name = person["name"]
        age = person["age"]
        hobbies = ", ".join(person["hobbies"])
        print(f"{name} {age} years ({hobbies})")

if __name__ == "__main__":
    print_persons("file4.json")