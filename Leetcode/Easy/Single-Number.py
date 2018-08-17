# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

# My notes:
#   - Limitation to linear is fine. Limitation to extra memory is interesting...
#       - It would be easy to send each to a hash table, except that uses extra memory
#   - Let's just do it with the hash table and then see what the no-extra-memory answer would be

test_input = [2, 2, 1]  # 4


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Instantiate an empty dict
    seen_it = {}
    # Loop through everything
    for n in nums:
        # If we've seen it, set it to true
        if seen_it.get(n, None) is False:
            seen_it[n] = True
        else:
            # Otherwise, this is the first time, so set to False
            seen_it[n] = False
    # Loop through again and return the first key with a False value
    for n in nums:
        if not seen_it[n]:
            return n

print(singleNumber(test_input))