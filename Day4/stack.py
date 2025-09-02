class Stack:
    def __init__(self, lst = []):
        self.lst = lst
    def isEmpty(self):
        return len(self.lst)
    def push(self, data):
        self.lst.append(data)
    def pop(self):
        if self.isEmpty():
            return self.lst.pop()
        else:
            print("stack is empty")
        
    def display(self):
        if self.isEmpty():
            return self.lst
        print("stack is empty")
        
    
obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
print(obj.pop())
print(obj.pop())
print(obj.display())

