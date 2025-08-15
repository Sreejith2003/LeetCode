class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    

head = Node(input("Enter head: "))
Val1 = Node(input("Enter val1: "))
Val2 = Node(input("Enter val2: "))
Val3 = Node(input("Enter val3: "))

curr = head
head.next = Val1
Val1.next = Val2
Val2.next = Val3


# Displaying the linked list
def Display(head):
    curr = head
    ele = []
    while curr:
        ele.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(ele))

Display(head)

def delete(head):
    curr = head
    prev = None
    dup = dict()

    while curr:
        if curr.val in dup:
            prev.next = curr.next
            curr = None
        else:
            print("No value")
head = delete(head)
Display(head)