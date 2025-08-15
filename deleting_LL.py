# Deleting the linked list element / Node

class Node:
    def __init__(self, val, next = None):

        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty!")

        else:
            n = self.head
            while n:
                print(n.val, "-->", end = " ")
                n = n.next

    def add_begin(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node

        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = new_node

    def add_after(self, val, x):
        n = self.head
        while n:
            if x == n.val:
                break
            n = n.next
        if n is None:
            print("Node is not present in LL")

        else:
            new_node = Node(val)
            new_node.next = n.next
            n.next = new_node

    def delete_begining(self):
        if self.head is None:
            print("The list is empty")

        else:
            self.head = self.head.next

LL = LinkedList()

LL.add_begin(10)
LL.add_begin(20)
LL.delete_begining()
LL.display()