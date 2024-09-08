# Write your solution here
def read_input(text: str, debut: int, last: int):
    while True:
        try:
            number = int(input(text))
            if number >= debut and number <= last:
                return number
            print(f"You must type in an integer between {debut} and {last}")
        except ValueError:
            print(f"You must type in an integer between {debut} and {last}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
