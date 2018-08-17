# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# My notes:
#   In-place makes this a little difficult, as well as trying to minimize operations
#       Otherwise, we could just bubble sort them down...might be best anyway
#           But maybe we can move them straight to the end and then shift everything? It's an array, so it wouldn't really save operations
#           We could maybe just remove all zeroes, count all of them, then add them at the end
#               Let's do this one

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Instantiate a list that keeps track of what we need to remove
        zeroes = []
        for i, num in enumerate(nums):
            if num == 0:
                zeroes.append(i)
        # Keep a counter so we pop the right index
        i = 0
        for z in zeroes:
            nums.pop(z - i)
            i += 1
            nums.append(0)