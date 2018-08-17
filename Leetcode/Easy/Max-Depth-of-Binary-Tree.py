# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# My notes:
#   - Should be able to just count each time we go down a node
#   - Would probably work best with recursion, add up the depth of each node

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Cover base case
        if not root:
            return 0
        # Instantiate some initial counters
        left_depth = 1
        right_depth = 1
        # Traverse the left, if it exists
        if root.left:
            left_depth += self.maxDepth(root.left)
        if root.right:
            right_depth += self.maxDepth(root.right)
        # Return max of left/right
        return max(left_depth, right_depth)