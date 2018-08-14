# You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel. Flip it in-place along its vertical axis.
#
# Example:
# Input image :
# 1 0
# 1 0
#
# Modified to :
# 0 1
# 0 1
# My Notes:
#   - Needs to occur in-place, so no other data structures
#   - Only flipped along vertical axis, so just need to swap along each row
#   - I could use something like .reverse() or [::-1], but it's probably better practice to do more manually

test_inputs = [                     # Expected Results:
    [[1]],                          # [[1]]
    [[1,0,1],[1,0,1]],              # [[1, 0, 1], [1, 0, 1]]
    [[1,0]],                        # [[0, 1]]
    [[1,2,3],[4,5,6],[7,8,9]],      # [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    [[1,0,0],[0,0,1]]               # [[0, 0, 1], [1, 0, 0]]
]


def flip_vertical_axis(matrix):
    # Base case: If length of row is <= 1, we don't have to do anything
    if len(matrix[0]) <= 1:
        return matrix
    # Loop over each row
    for row in matrix:
        # We're going to look at first and last index, then move inwards while start is < end
        start = 0
        end = len(row) - 1
        while start < end:
            # Create temp variables for each swap
            start_value = row[start]
            end_value = row[end]
            # Replace each index with the temp variable
            row[start] = end_value
            row[end] = start_value
            # Increase start, decrease end
            start += 1
            end -= 1


for matrix in test_inputs:
    flip_vertical_axis(matrix)