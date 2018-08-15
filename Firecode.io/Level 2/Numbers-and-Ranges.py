# Given a sorted list and an input number as inputs, write a function to return a Range object,
# consisting of the indices of the first and last occurrences of the input number in the list.
#
# Note: The List can have duplicate numbers. The indices within the Range object should be zero based.
#
# Examples:
# Input List  : [1,2,5,5,8,8,10]
# Input Number : 8
# Output : [4,5]
#
# Input List  : [1,2,5,5,8,8,10]
# Input Number : 2
# Output : [1,1]
#
# My notes:
#   - This doesn't seem particularly hard, especially since it's ordered
#   - Just loop through the list until we find the input number
#   - Add it's index to a list
#   - Keep going until we don't find the number again, and make list[1] = i - 1
#   - We can keep track of whether or not we've found the number already with len(return_list)
#   - Apprently, we need to return as a Range
#   - Hindsight: We could do this faster with binary search for the input number

class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"

def find_range(input_list,input_number):
    # Instantiate the return list
    return_list = []
    # Loop through the list and enumerate
    for i, n in enumerate(input_list):
        # Loop until we hit our number and we haven't hit it yet
        if n == input_number and not return_list:
            # Add the index to the return list. Setting to [i, i] in case we're at the end of the list and/or don't find number again
            return_list = [i, i]
        # If we've already found our number but subsequent numbers don't match...
        elif return_list and n != input_number:
            # Append current index - 1 (which would be the index of our last matching number) to our list and break
            return_list[1] = i - 1
            break
    # Instantiate the return range with our lower and upper bounds
    return Range(return_list[0], return_list[1])