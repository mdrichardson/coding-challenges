# Given a singly linked list, write a method to perform In-place reversal.
#
# Example:
# 1->2->3 ==> 3->2->1

class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

# My notes:
#   - We should be able to change the next value of each until we get to the end, pushing the new head down as we go
#   - [a][->b]   [b][->c]    [c]   =>   [c][->b]    [b][->a]    [a]
#   - Initialize a variable that stores the previous element (None for the first)
#   - Initialize a variable for storing the current position, starting with the head
#   - Loop through until we're at the end (last node.next = None)
#       - Temp store the next node
#       - Set the current node's next to the previous
#       - Set the previous node as the current
#       - Set the current node as the next
#   - Once out of the loop, set the new head as the previous element

class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def reverse(self):
        # Initialize a variable that stores the previous element (None for the first)
        prev = None
        # Initialize a variable for storing the current position, starting with the head
        current = self.head
        # Loop through until we're at the end (current node.next = None)
        while current != None:
            # Temp store the next node
            nxt = current.getNext()
            # Set the current node's next to the previous
            current.setNext(prev)
            # Set the previous node as the current
            prev = current
            # Set the current node as the next
            current = nxt
        # Once out of the loop, set the new head as the previous element
        self.head = prev











