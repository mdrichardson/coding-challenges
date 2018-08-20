# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# My notes:
#   For [0,1,2,4]...
#   It starts at 0, so we can create an array of len(nums) + 1 filled with False; [False, False, False, False]
#   For each value in nums, we push that value to the index of the new array... [True, True, True, False, True]
#   Loop through the array at the end and find the first False value and return it
#   ...in hindsight, this could be done quicker just using math, since it's in order, starting at 0

def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    present = [False for x in range(0, len(nums) + 1)]
    for n in nums:
        present[n] = True
    for i, p in enumerate(present):
        if not p:
            return i
