# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row_number = sudoku[row_no]
    for element in row_number:
        index = row_number.index(element)
        if element == 0:
            continue 
        else:
            for i in range(index +1, len(row_number)):
                if element == row_number[i]:
                    return False
    return True

if __name__ == "__main__":

    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))