# Write a function to find the total number of leaf nodes in a binary tree. A node is described as a leaf node if it doesn't have any children. If there are no leaf nodes, return 0.
#
# Example:
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7
#   / \
#  8   9
# ==> no. of leaves = 5
# class TreeNode:
#     def __init__(self, data,left_child = None, right_child = None):
#         self.data = data
#         self.left_child = left_child
#         self.right_child = right_child

# My Notes:
#   - We should be able to just traverse the tree, stop when we find a node without children and add that to a counter

class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def number_of_leaves(self, root):
        # Check base case
        if not root:
            return 0
        # Instantiate a counter
        counter = 0
        # Check if it doesn't have children
        if not root.left_child and not root.right_child:
            return 1
        # Otherwise, keep traversing
        else:
            # Get all left-side leaves
            if root.left_child:
                counter += self.number_of_leaves(root.left_child)
            if root.right_child:
                counter += self.number_of_leaves(root.right_child)
        return counter