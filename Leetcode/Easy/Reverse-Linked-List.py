# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# My notes:
#   [1][->2]  [2][->3]  [3]  =>  [3][->2]  [2][->1]  [1]
#   Let's focus on iteratively, first
#   Create a node, prev = None
#   Set current to self.head, current = 1->2
#   Set nxt to current.nxt, nxt = 2->3
#   Set current.next to prev, 1->None
#   Set prev to current, prev = 1->None
#   Set current to nxt, current = 2->3
#   Set nxt to current.next, nxt = 3->None
#   Set current.next to prev, 2->1
#   Set prev to current, prev = 2->1
#   Set current to nxt, current = 3->None
#   Set nxt to current.next, nxt = None
#   Set current.next to prev, 3->2
#   Stop when nxt = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Catch an empty list
        if not head:
            return head
        #   Create a node, prev = None
        prev = None
        #   Set current to self.head
        current = head
        #   Set nxt to current.next
        nxt = current.next
        # Loop until nxt = None
        while nxt:
            #   Set current.next to prev
            current.next = prev
            #   Set prev to current
            prev = current
            #   Set current to nxt
            current = nxt
            #   Set nxt to current.next
            nxt = current.next
        # Set the last current.next to prev and return
        current.next = prev
        return current
