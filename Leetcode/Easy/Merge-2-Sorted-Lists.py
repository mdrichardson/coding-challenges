# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# My notes:
#   I'm pretty sure I can do this quicker with the zip() function, but let's try doing it without
#   I think the best approach would be merging one list into the other vs sort of comparing each
#   Take the first node of list 2, iterate through list 1 until we can merge, then splice it.
#       To avoid iterating through from the start, we can store a start node in a variable and change the start node after each splice
#   To splice, we point the before node to the new node and the new node to the after node...might be easiest to make it a separate function
#   To search, we'll need to keep track of both the before and after nodes
#       Once after==None, we just add any remaining nodes on
#       Also need to keep track of list 2's next node
#   Loop through list 2 until l2 == None
#       Loop through list 2 until current2 <= current1. Probably better to just loop while they're
#           If that happens, splice the nodes
#           Start the search from the next in each list
#   If we ever get to the end of list1, add all the list2 nodes and then return list 1's start
#   That's how it should be done iteratively, but I'd prefer something recursive
#       Base case would be if either list is empty, then you just return the non-empty
#       Check for which val is smaller, and send it through again with by making the smaller one's next = to the merge without its next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


