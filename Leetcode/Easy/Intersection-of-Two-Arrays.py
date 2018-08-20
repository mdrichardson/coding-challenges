# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# My notes:
#   Maybe it would be faster to reduce each to a set, then compare so we have a list of common numbers?
#   We could start with each element in the shorter list, search for it and if we find it, search for i+1 until it stops...
#   We could binary search if it were sorted...that would make it a bit faster, but not in this case, unsorted
#   What if we hashed all of the numbers in the longer one first, so that we can skip searching if it isn't there anyway?
#       That would be a little faster....we could store each index of the occurrence. I think this is best
#   1. Find the longer of the two lists
#   2. Hash all of the values in the list and append the index of its occurrence to the key
#   3. Loop through the smaller list
#       If the value exists in the longer list, then search from those indexes onwards until they no longer match
#           Append these to a result list as it goes
#   Instructions weren't totally clear. Apparently, order is irrelevant for both lists as well as the result
#       The solution for the above problem is commented out. The solution for the order-doesn't-matter-solution is the one not commented
#   For this one, we just need a single hash table. Go through the shortest. +1 for each occurrence.
#       Go through the second list. -1 for each occurrence and add to a result list while value in hash > 0
#       Well, longer/shorter shouldn't matter in this case, since we loop through both twice anyway
#           Although building the hash table with shorter will save space


def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if len(nums1) > len(nums2):
        longer = nums1
        shorter = nums2
    else:
        longer = nums2
        shorter = nums1
    freq = {}
    for n in shorter:
        freq[n] = freq.get(n, 0) + 1
    result = []
    for n in longer:
        if freq.get(n, None) and freq[n] > 0:
            result.append(n)
            freq[n] -= 1
    return result


# SOLUTION FOR IF THE ORDER MATTERS IN THE LISTS

# def intersect(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     if len(nums1) > len(nums2):
#         longer = nums1
#         shorter = nums2
#     else:
#         longer = nums2
#         shorter = nums1
#     longer_values = {}
#     for i, n in enumerate(longer):
#         if longer_values.get(n, None):
#             longer_values[n].append(i)
#         else:
#             longer_values[n] = [i]
#     result = []
#     best = []
#     for i, n in enumerate(shorter):
#         if longer_values.get(n):
#             indices = longer_values[n]
#             for index in indices:
#                 while i < len(shorter) and index < len(longer) and shorter[i] == longer[index]:
#                     result.append(shorter[i])
#                     i += 1
#                     index += 1
#                 if len(result) > len(best):
#                     best = result
#                 else:
#                     result = []
#     return best