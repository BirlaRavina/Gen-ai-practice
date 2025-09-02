class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class Linkedlist(Node):
    def __init__(self, head= None):
        self.head = head
    def addFirst(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def printValues(self):
        if self.head == None:
            return "list is empty"
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    def addLast(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode


obj = Linkedlist()
obj.addFirst(30)
obj.addFirst(20)
obj.addFirst(10)
# obj.printValues()
obj.addLast(40)
obj.addLast(50)
obj.printValues()