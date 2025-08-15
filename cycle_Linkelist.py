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
pos = Node(input("Enter the position: "))

curr = head
head.next = Val1
Val1.next = Val2
Val2.next = Val3
Val3.next = pos

def Display(head):
    curr = head
    ele = []
    while curr:
        ele.append(str(curr.val))
        curr = curr.next
    
    print(" -> ".join(ele))

Display(head)

def CyclicLinkedlist(head):
    curr = head
    st = set() # This is hash set method to find the loop in the list 
    while curr:         # Since it is taking space it is O(n) space complexity
        if curr in st:
            return True
        st.add(curr)
        curr = curr.next
    return False

if CyclicLinkedlist(head):
    print('True')
else:
    print("False")

"""

This is Tortoise algorithm also called as Floyd's slow and fast algorithm

1) This has slow and fast val which will move at a diff speeed
2) slow moves one step at a time and fast moves two step at a time
3) By traversing through the linked list if slow and fast val becomes same then the list is a cyclic list
4) Since it is not storing any val it is O(1) spcae complexity and O(n) time complixity



def CyclyLinkedlist(head, pos):
    
    slow = fast = head              
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if slow == fast:
            return True
    return False

head = CyclyLinkedlist(head, pos = 1)
Display(head)

"""