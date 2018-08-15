# Write a function to insert a node at the front of a Singly Linked-List
#
# Examples:
# LinkedList: 1->2 , Head = 1
#
# insert_at_front(1) ==> 1->1->2
#
# insert_at_front(2) ==> 2->1->2
#
# insert_at_front(3) ==> 3->1->2
# My Notes:
#   - We should be able to just create a new node...set the new node's next to the current head and the list's head to the new node

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


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # Method for inserting a new node at the start of a Linked List
    def insert_at_front(self, data):
        # Instantiate a new node
        node = Node()
        # Give the node it's data
        node.setData(data)
        # Set the node's next to the current head
        node.setNext(self.head)
        # Set the list's head to the new node
        self.setHead(node)