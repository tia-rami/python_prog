# Write your solution here
def print_result():
    while True:
        print("1 -  add an entry, 2 - read entries, 0 - quit")
        function = int(input("Function: "))

        if function == 0:
            break
        if function == 1:
            add_entry()
        elif function == 2:
            read_entries()
        
def add_entry():
    with open("diary.txt", "a") as my_file:
        message = input("Diary entry: ")
        my_file.write(f"{message}\n")
        print("Diary saved")
    print()

def read_entries():
    print("Entries:")
    with open("diary.txt") as my_file:
        for line in my_file:
            print(line, end="")

def main():
    print_result()
    print("Bye now!")
    

main()