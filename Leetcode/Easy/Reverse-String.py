# Write a function that takes a string as input and returns the string reversed.
#
# Example 1:
#
# Input: "hello"
# Output: "olleh"
# Example 2:
#
# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"

# My notes:
#   - Pretty simple, since it doesn't seem to need to account for edge cases

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]