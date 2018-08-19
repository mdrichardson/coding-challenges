# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# My notes:
#   Recursive isn't trivial for me yet :(
#   In-order: Left, root, right.
#   We need to traverse all the way down the left. When we can't return the left, go back to it's parent, return it, and return it's right
#   We need to return a list....if this has to be recursive we'd have to make a separate list for left, itself, and right then return them, added/joined

# To do this iteratively, we could use a stack
#       5
#   3       7       Stack needs to go 5-3-1-pop1-pop3-2-pop2-pop5-7-pop7-9-pop9 => [5] [53] [531] [53] [5] [52] [5] [] [7] [] [9] []
#  1 2        9     Final list needs to be 1-3-2-5-7-9
#
#   So....it goes...root to stack; has left child, so 3 to stack; has left child so 1 to stack;
#       1 has no left children, so 1 from stack to return; 3 has no other left children, so 3 from stack to return;
#       3 has right child so 2 to stack; 2 has no left children, so 2 from stack to return; 5 has no other left children, so 5 from stack to return
#       5 has right child, so 7 to stack; 7 has no left children, so 7 from stack to return; 7 has right child so 9 to stack; then 9 to return
#       Once a root's left child has been added to stack, we need to set its left child to None
#       Maybe something like while root.left, append it, and set the root as root.left. that gives us 5 3 1
#       Once we break from that, we pop until we get a root.right.
#       When we get a root.right, it just starts the root.left search again

#   I got pretty close on this one. Recursive works fine. Iterative works, except for the root = stack[*] part. It needs to equal the previous root, not the previous
#       root's value. I'm done working on this one, though

# ITERATIVE
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Instantiate a stack -- we're going to use this without the collections library by using a list
        stack = [7]
        return_list = [1, 3, 2, 5]
        # Keep track of when we're done
        done = False
        # Loop until we're done
        while not done:
            # Loop through all the left children. Handle if already looked for    # root = 9
            while root.left:
                if root.val == stack[-1]:
                    del stack[-1]
                    return_list.append(root.val)
                    break
                stack.append(root)
                root = root.left
                # This should go until there are no more left
            # Let's pop and move up until there is a right child
            while not root.right:
                # Append if it was from the right
                if stack[-1] != root.val:
                    stack.append(root)
                del stack[-1]
                return_list.append(root.val)
                # Try to change root. If we can't that means we can break out
                try:
                    root = stack[-1]
                except:
                    done = True
                    break
                # This should go until we find a right child
            # If we have a right child but not left, we can add ourselves straight to the return stack
            if root.right and not root.left:
                return_list.append(root.val)
            # Now that we have a right child, we append it and set it to the new root and start over
            root = root.right
        # Return the return_list
        return return_list




# RECURSIVE

class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            # Get a list of the left side
            left_side = self.inorderTraversal(root.left)
            # Get a list of the right side
            right_side = self.inorderTraversal(root.right)
            # Return each node's left-self-right values
            return (left_side + [root.val] + right_side)
        # If there's no root, return nothing
        else:
            return []



