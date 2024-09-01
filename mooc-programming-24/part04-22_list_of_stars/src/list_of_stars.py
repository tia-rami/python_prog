# Write your solution here
def list_of_stars(numbers_list: list):
    i = 0
    while i < len(numbers_list):
        print("*" * numbers_list[i])
        i += 1

if __name__ == '__main__':
    list_of_stars([3, 7, 1, 1, 2])