# Write a function to insert a node at the end of a Singly Linked-List.
#
# Examples:
# LinkedList: 1->2 , Head = 1
#
# insertAtEnd(1) ==> 1->2->1
#
# insertAtEnd(2) ==> 1->2->2
#
# insertAtEnd(3) ==> 1->2->3

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

    # method for inserting a new node at the end of a Linked List
    def insertAtEnd(self, data):
        # Instantiate a node with the data
        n = Node()
        n.setData(data)
        # Check if head exists and if it doesn't set data as the head
        if not self.head:
            self.setHead(n)
        # If there's already a head, we need to set the last node in the list's next pointer to the new node
        else:
            # Find the last node in the list
            start = self.head
            while start.getNext() != None:
                start = start.getNext()
            # Set the last node's next pointer to the new node
            start.setNext(n)


node3 = Node().setData(3)
node5 = Node().setData(5)

l = SinglyLinkedList()

nodes = [node3, node5]

for n in nodes:
    l.insertAtEnd(n)