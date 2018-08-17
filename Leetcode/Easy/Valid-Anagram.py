# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# My notes:
#   Pretty easy. Create a dict of each char in s, add 1 each time it occurs
#   Loop through t and -1 from dict each time char occurs.
#   If it ever needs to -1 and its already at 0, return false
#   We'll also need a way to tell that all characters have been used...just check the lengths are the same
#   For unicode, it should be the same, we'd just group them together, hash them the same, and need to do some math for length comparison



def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # Check to see lengths are equal
    if len(s) != len(t):
        return False
    # Instantiate dict
    count = {}
    # Loop through all chars in s
    for c in s:
        # Check to see if c is in there already
        if count.get(c, None):
            # It's not there, so add it with a value of 1
            count[c] = 1
        else:
            # It's there, so increase the count
            count[c] += 1
    print(count)
    # Loop through t
    for c in t:
        # Return false if there's too many of c in t or if c not in count
        if not count.get(c, None) or count[c] == 0:
            return False
        else:
            count[c] -= 1
        print(count)
    return True