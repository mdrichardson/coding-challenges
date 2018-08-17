# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Given linked list -- head = [4,5,1,9], which looks like following:
#
#     4 -> 5 -> 1 -> 9
# Example 1:
#
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list
#              should become 4 -> 1 -> 9 after calling your function.
# Example 2:
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list
#              should become 4 -> 5 -> 9 after calling your function.
# Note:
#
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# My notes:
#   We'll definitely need to go through our list until we reach our node, ID'd by node.val
#   We should be able to move through, keeping a prev variable tracking the last node
#   When we hit our value, set the value of prev.next to our_value.next
#   Is it that simple?
#   [1][->2]  [2][->3]  [3][->4]  [4]   .....delete 3
#   Copy the current element to prev, prev = 1->2
#   Copy the current element to current, current = 1->2
#   Create a variable for the current value, value = 1
#   Loop through until current.val == to_delete, value == 3
#       At each loop, prev = current, value = current.val and current = current.next; prev = 1->2, value = 1, current = 2->3; prev = 2->3, value = 2, current = 3->4
#           prev = 3->4, value = 3, current = 4->None; break
#   Once we're out, set prev.next to current.next, 3->4 would become 3->None
#       We need to start the loop by checking current.val and break once we're there
#   Looks like we can also cut out the variable initiation and start with the loop, too
#   Oh, WTF?! We're only given the node we need to delete? How do we do that without being able to ID the previous node?!
#       Can we just set its value to its next? No....it would still return an object
#       So...the node is stored in memory. How do we point its own memory address to the it's next node?
#       Can we just set the node to equal the next node and point to the next node's next node?
#   Yes! What a weird question. It still doesn't change the address, and it's really deleting the next one, but it works, I guess

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next
        node.next =  node.next.next