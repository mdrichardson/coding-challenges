# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:
#
# Input: "A"
# Output: 1
# Example 2:
#
# Input: "AB"
# Output: 28
# Example 3:
#
# Input: "ZY"
# Output: 701

# My notes:
#   Need to create a hash of capital letters and appropriate index
#   If len(s) > 1, we multiply the first by 26 * dict[char] and add 1

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Let's make it easy so we don't have to type out the whole dict
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        column_to_value = {}
        for i, char in enumerate(alphabet):
            column_to_value[char] = i + 1
        # Fomula is basically, find value of first character. For next, multiply what you have by 26 and add the current character
        total = 0
        for i, c in enumerate(s):
            total = (total * 26) + column_to_value[c]
        return total