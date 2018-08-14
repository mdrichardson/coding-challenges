# Given an list containing 9 numbers ranging from 1 to 10, write a function to find the missing number.
# Assume you have 9 numbers between 1 to 10 and only one number is missing.
#
# Example:
# input_list: [1, 2, 4, 5, 6, 7, 8, 9, 10]
# find_missing_number(input_list) => 3

# My Notes:
#   - Since the list is ordered, this is pretty easy

inputs = [
    [1, 2, 3, 4, 5, 6, 7, 8, 10], # 9
    [1, 2, 4, 5, 6, 7, 8, 9, 10]  # 3
]


def find_missing_number(list_numbers):
    for n in range(0, len(list_numbers)):
        if list_numbers[n] != n + 1:
            return n + 1


for test in inputs:
    print(find_missing_number(test))