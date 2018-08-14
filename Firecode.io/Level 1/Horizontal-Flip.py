# You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel. Flip it in-place along its horizontal axis.
#
# Example:
#
# Input image :
#               1 1
#               0 0
# Modified to :
#               0 0
#               1 1

# My Notes:
#   - Needs to be done in-place again
#   - let's do this more by hand for the practice
#   - Needs to switch row with its pair

test_inputs = [                 # Expected Results
    [[1,0,0],[0,0,1]],          # [[0, 0, 1], [1, 0, 0]]
    [[1,2,3],[4,5,6],[7,8,9]],  # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    [[1,0],[1,0]],              # [[1, 0], [1, 0]]
    [[1]],                      # [[1]]
    [[1,0,1],[1,0,1]]           # [[1, 0, 1], [1, 0, 1]]
]

def flip_horizontal_axis(matrix):
    # Let's instantiate a couple varables to keep track of a row with its pair
    i = 0
    pair = len(matrix) - 1
    # While loop until i and pair meet
    while i < pair:
        # Set a temp row holder to matrix[i] so we can in-place swap
        temp_row = matrix[i]
        # Now swap the rows
        matrix[i] = matrix[pair]
        matrix[pair] = temp_row
        # Change our positions
        i += 1
        pair -= 1
    return matrix


for matrix in test_inputs:
    print(flip_horizontal_axis(matrix))