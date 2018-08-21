# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# My notes:
#   This seems a little bit like a fibonacci one, but instead of keeping the last two results, we'd want the entire last row
#   I think we still have to default the first two rows, [1],[1,1]
#   After that, 2 is at index 1...need index 0 and 1 of the above rows, so that's n and n-1
#   Each row will have as many items as its row numbers, if 1-indexed
#   First and last elements are always 1
#   Pretty sure I can do this with recursion.
#   So, we'd first define a dict with {1: [1]. 2: [1, 1]
#   Base case: if n is in dict, just return the n
#   Otherwise, let's build an array of len(n) and set the first and last numbers at 1
#   Then, we recursively get the n-1 row
#   Then we loop through our row from 1 to n-1 and set the value to prevRow[n] + prevRow[n-1]
#   Then we add that row to the dict and append it to a result
#   Issue is that we need to return a list at the end, not a dict
#       Let's use an array and add items at numRows - 1

tests = [1, 2, 5]

class Solution:

    def __init__(self):
        self.rows = [[1], [1, 1]]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [self.rows]
        if numRows == 1:
            return [self.rows[0]]
        if numRows > 2:
            prevRow = self.generate(numRows - 1)[-1]
            row = [None for x in range(0, numRows)]
            for i in range(0, numRows):
                if i == 0 or i == numRows - 1:
                    row[i] = 1
                else:
                    row[i] = prevRow[i] + prevRow[i-1]
            self.rows.append(row)
        return self.rows

s = Solution()
for t in tests:
    print(s.generate(t))