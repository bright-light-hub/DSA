
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at_last(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp 
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = temp
        
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            

ob = linkedlist()
ob.insert_at_last(1)
ob.insert_at_last(2)
ob.insert_at_last(3)
ob.display()


