
class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;

class slinkedlist:
    def __init__(self):
        self.head = None

    def add_in_begning(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

#driver code
ob = slinkedlist()

ob.add_in_begning(4)
ob.add_in_begning(3)
ob.add_in_begning(1)
ob.display()
