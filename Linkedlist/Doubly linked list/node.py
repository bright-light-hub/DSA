
class Node:
    def __init__(self, data):
        self.pre = None
        self.data = data
        self.next = None




# Create three nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link the nodes together
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2