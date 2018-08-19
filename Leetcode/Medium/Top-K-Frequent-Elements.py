# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 <= k <= number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# My notes:
#   Has to be better than nlogn? That shouldn't be difficult. can't we just use a hash table, then loop through it at the end?
#       First pass is O(n). 2nd pass is O(3n) since it has to compare to our current best two...that's still O(n)
#   Is there a better way? I guess if k = n, that would take n**2...so we need to find something else
#   We could add them to a hash table, then add them to an array where the index is frequency and value is the key
#   Then we grab the last k items in the array
#   We might have to handle if there's some of the same frequency...
#       Let's just make it a list of lists, then


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # Handle small list
    if len(nums) < 2:
        return nums
    freq = {}
    # Each num can occur at most, len(nums), so make an array that long so we can add our nums at the index
    ordered = [[] for x in range(0, len(nums))]
    # Create the freq dict
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    for n, f in freq.items():
        ordered[f - 1].append(n)
    # Loop through ordered, backwards and return k items
    result = []
    for x in ordered[::-1]:
        if k > 0:
            for n in x:
                result.append(n)
                k -= 1
        else:
            break
    return result

print(topKFrequent([1,1,2,3], 1))