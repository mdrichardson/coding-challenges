# Write a function that takes in a list of ints and uses
# the Bubble Sort algorithm to sort the list 'in place' in ascending order. The method should return the same, in-place sorted list.
# Note: Bubble sort is one of the most inefficient ways to sort a large list of integers. Nevertheless, it is an interview favorite.
# Bubble sort has a time complexity of O(n2). However, if the
# sample size is small, bubble sort provides a simple implementation of a classic sorting algorithm.
#
# Examples:
# bubble_sort([5, 4, 3]) -> [3, 4, 5]
#
# bubble_sort([3]) -> [3]
#
# bubble_sort([]) -> []
#
# [] -> [Empty] List

# My Notes:
# 1. Starts at start of list
# 2. If next item is smaller, they swap places and this continues until next item is no longer smaller
# 3. Starts over
# Needs to sort in place. So, for loop through each element
# After seeing solutions, this could be much simpler with two for loops

test_input = [1, 1, 2, 2, 1, 2]  # [1, 1, 1, 2, 2, 2]


def bubble_sort(a_list):
    # Loop through each element
    for n in range(len(a_list)):
        # Always need to start by comparing first two elements
        i = 0
        compare = 1
        # Get to the first swappable point. Don't execute if we can't
        while compare < len(a_list) and a_list[i] <= a_list[compare]:
            i += 1
            compare += 1
        # Try to swap until n is smaller than the comparison element. Also stop at the last element
        while compare < len(a_list) and a_list[i] > a_list[compare]:
            # If it is smaller, swap them and increase i so it's tracking the new place. Use a temp variable for the swap
            temp = a_list[i]
            a_list[i] = a_list[compare]
            a_list[compare] = temp
            # Increase i and compare so we're looking at the correct elements
            i += 1
            compare += 1
    return a_list







print(bubble_sort(test_input))