# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

# My Notes:
#   I could count frequency in a hash table
#       Create an array all [False] with lengths same as string
#       When hash table indicates repeat, change that index to True
#       Then loop through the array and return the first False...Is that the fastest? I would think so...
#       No...that will only change the last one found to be a duplicate
#       Let's just loop the hash table at the end. We just have to store the first index along with the freq

test = "loveleetcode"

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    # Create the hash table and array
    freq = {}
    # Populate the freq dict and list
    for i, c in enumerate(s):
        if freq.get(c, None):
            freq[c][1] += 1
        else:
            freq[c] = [i, 1]
    # Loop through the list and return the i of the first non-repeat
    min_index = len(s)
    for k, v in freq.items():
        if v[1] == 1 and v[0] < min_index:
            min_index = v[0]
    return min_index if min_index != len(s) else -1

print(firstUniqChar(test))