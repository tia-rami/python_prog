# Write your solution here
def new_person(name: str, age: int):
    if age > 150 or age < 0:
        raise ValueError("Invalid parameter")
    if name == '' or len(name.split(' ')) < 2 or len(name) > 40:
        raise ValueError("Invalid parameter")

    return (name, age)


if __name__ == "__main__":
    person_info = new_person("tia", 29)
    print(person_info)
    