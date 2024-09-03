# Write your solution here
def transpose(matrix: list):
    new_matrix = []
    i = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            new_matrix.append(matrix[col][row])

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(new_matrix[i], end = " ")
            i += 1
        print()


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    transpose(matrix)
    print(matrix)