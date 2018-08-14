# Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order.
# This method should return a list of redundant integers in ascending sorted order (as illustrated below).
#
# Examples:
# duplicate_items([1, 3, 4, 2, 1]) => [1]
#
# duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4]

# My Notes:
#     - Probably quickest to store in a hash table/dict
#     - We could loop through dict at end and then sort, but maybe there's a better way
#       - Once we find it is a duplicate, add it to a list? We'd have to binary search to add in order. That's O(n log n) either way

test_inputs = [                         # Expected Result
    [1, 3, 3, 4],                       # [3]
    [1, 5, 23, 2, 6, 3, 1, 8, 12, 3],   # [1, 3]
    [4],                                # []
    [4, 3, 1]                           # []
]


def duplicate_items(list_numbers):
    # Declare a dict and duplicate list
    number_dict = {}
    duplicate_list = []
    # Loop through all numbers
    for n in list_numbers:
        # Check if number exists in dict already
        if number_dict.get(n, None):
            # If it does, add it to duplicate list
            duplicate_list.append(n)
        else:
            # If it doesn't, add it to dict
            number_dict[n] = True
    # Return the sorted list
    return sorted(duplicate_list)


for numbers in test_inputs:
    print(duplicate_items(numbers))