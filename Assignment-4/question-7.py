# Matrix 1: list of lists (3x4)
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Matrix 2: tuple of tuples (3x4)
matrix2 = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

# Function to calculate addition and subtraction
def matrix_operations(m1, m2):
    add = []
    sub = []

    for i in range(3):
        add_row = []
        sub_row = []
        for j in range(4):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        add.append(add_row)
        sub.append(sub_row)

    return add, sub


# Main program
addition, subtraction = matrix_operations(matrix1, matrix2)

print("Addition Matrix:")
for row in addition:
    print(row)

print("\nSubtraction Matrix:")
for row in subtraction:
    print(row)
