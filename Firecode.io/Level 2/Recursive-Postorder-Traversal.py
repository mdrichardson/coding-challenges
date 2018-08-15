# Given a binary tree, implement a method to populate the list post_ordered_list with the data of the nodes traversed in postorder, recursively.
#
# Example:
#      1
#     / \
#    2   3     ==> 4526731
#   / \ / \
#  4  5 6  7

# My Notes:
#   - Post-order: Left, right, root
#   - Should be mostly like pre-order, we just need to append in a different order
#   - Traverse all the way down the left first
#   - Then traverse all the way down the right
#   - Append each time we're done traversing

post_ordered_list = []


class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def postorder(self):
        # Traverse all the left children
        if self.get_left_child():
            self.get_left_child().postorder()
        # Traverse all the right children
        if self.get_right_child():
            self.get_right_child().postorder()
        post_ordered_list.append(self.get_root_val())

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data