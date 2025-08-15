class soln:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

    
head = soln(input("Enter head: "))
A = soln(input("Enter val1: "))
B = soln(input("Enter val2: "))
C = soln(input("Enter val3: "))

head.next = A
A.next = B
B.next = C

curr = head

def Display(head):
    curr = head
    ele  = []
    while curr:
        ele.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(ele))

Display(head)

def reversed_LL(head):
    prev = None
    curr = head 

    while curr:
        nextsoln = curr.next
        curr.next = prev 

        prev = curr 
        curr = nextsoln 
    return prev

head = reversed_LL(head)

Display(head)





