
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at_last(self,data):
        temp = Node(data)
        current = self.head
        if self.head == None:
            self.head = temp 
            return
        while current.next is not None:
            current = current.next
        current.next = temp
        
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def reverse(self):
        pre = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = pre
            pre = current
            current = next
        self.head = pre
    
ob = linkedlist()
ob.insert_at_last(1)
ob.insert_at_last(2)
ob.insert_at_last(3)
ob.insert_at_last(4)
ob.insert_at_last(1)
ob.display()
ob.reverse()
ob.display()

