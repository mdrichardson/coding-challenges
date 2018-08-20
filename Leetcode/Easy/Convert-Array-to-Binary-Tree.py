# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
#  of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
# Definition for a binary tree node.
# My Notes:
#   The tree is pre-sorted, so we need to set the root as len(nums) / 2
#   Longer tree example:
#           10                                              3
#       8       12      Input=[7,8,9,10,11,12,14]          1  2    Input=[1,2,3]
#     7  9     11  14
#
#   It looks like we'll have to build this recursively from the bottom, up
#       In above, len(nums) / 2 gives us a root of 10, then we split the list and do len(split)/2 to get 8 and 12
#       if len(split) == 2, the new node is the larger of the two and the other is its left child, so return the node
#       if len(split) == 1, we return the node
#       if len(split) == 0, we just return
#       Define the tree, set the value
#       Recursive function would look something like:
#       if nums:
#           if len(nums) == 2:
#               the new node is the larger of the two and the other is its left child, None is the right, then return node
#           elif len(nums) == 1:
#               return node
#           otherwise, define each side of the root as the appropriate side of the list
#       return the tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            i = len(nums)//2
            root = TreeNode(nums[i])
            if len(nums) == 2:
                root = TreeNode(max(nums))
                root.left = TreeNode(min(nums))
                root.right = None
                return root
            if len(nums) == 1:
                return root
            root.left = self.sortedArrayToBST(nums[:i])
            root.right = self.sortedArrayToBST(nums[i+1:])
            return root
        else:
            return