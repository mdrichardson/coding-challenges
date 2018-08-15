# You are given a square 2D image matrix (List of Lists) where each integer represents a pixel.
# Write a method transpose_matrix to transform the matrix into its Transpose - in-place.
# The transpose of a matrix is a matrix which is formed by turning all the rows of the source matrix into columns and vice-versa.
#
# Example:
# Input image :
# 1 0
# 1 0
#
# Modified to:
# 1 1
# 0 0
# My Notes:
#   - Getting this to work in-place might be a little difficult. I guess we could store a whole row at a time

#  0  1  2       0  3  6
#  3  4  5   =>  1  4  7     [0][0] stays [0][0], [0][1] becomes [1][0], [1][2] becomes [2][1]
#  6  7  8       2  5  8

test_inputs = [
    [[1, 0], [0, 0]],                   # [[1, 0], [0, 0]]
    [[1, 0, 1], [1, 0, 1], [1, 0, 1]],  # [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
    [[1]],                              # [[1]]
    [[1,2,3], [4,5,6], [7,8,9]]         # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
]

def transpose_matrix(matrix):
    # Loop through all of the rows and all of the columns. It's square so we can use range
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix)):
            # Skip all the ones that won't change and stop so we don't switch everything back
            if row < column:
                # Instantiate a temp so we can swap
                temp = matrix[row][column]
                # Make the swap
                matrix[row][column] = matrix[column][row]
                matrix[column][row] = temp
    return matrix


for matrix in test_inputs:
    print(transpose_matrix(matrix))