class solution:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    

head = solution(input())
A = solution(input())
B = solution(input())
C = solution(input())

head.next = A
A.next = B
B.next = C

curr = head

#Traverse a list
while curr:
    print(curr)
    curr = curr.next

# To display this linked list

def Display(head):
    curr = head
    ele = []
    while curr:
        ele.append(str(curr.val))
        curr = curr.next 
    print(" -> ".join(ele))

Display(head)
print("")

class Doubly_Linkedlist:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next 
        self.prev = prev

    def __str__(self):
        return str(self.val)
    

#traverse

head = tail = Doubly_Linkedlist(1)      # Head and tail of the doubly linked list is set to 1
print(head)
print(tail)

def display(head):
    curr = head
    ele = []
    while curr:
        ele.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(ele))
display(head)

def insert_at_begining(head,tail, val):
    new_node = Doubly_Linkedlist(val, next = head)      # Inserting at the front i.e making a new value as head
    head.prev = new_node
    return new_node, tail

head , tail = insert_at_begining(head,tail, A)
display(head)


def insert_at_end(head, tail, val):
    new_node = Doubly_Linkedlist(val, prev = tail)      # Inserting at the end  
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, C)
display(head)


