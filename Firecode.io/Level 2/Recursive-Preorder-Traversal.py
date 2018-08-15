# Given a binary tree, write a function to recursively traverse it in the preorder manner.
# Mark a node as visited by adding its data to the list - pre_ordered_list(defined globally at the top of the editor).

# Example:
#
#      1
#     / \
#    2   3     ==> 1245367
#   / \ / \
#  4  5 6  7

# My Notes:
#   - Pre-order: Root, left, right.

pre_ordered_list = []


class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder(self):
        # Define base case
        if not self.get_left_child():
            pre_ordered_list.append(self.get_root_val())
        else:
            # Append self
            pre_ordered_list.append(self.get_root_val())
            # Get left children
            self.get_left_child().preorder()
            # Get right children, but pass if there aren't any
            try:
                self.get_right_child().preorder()
            except AttributeError:
                pass


    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data