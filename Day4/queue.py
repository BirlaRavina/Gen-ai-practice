class Queue:
    def __init__(self, que = []):
        self.que = que
    def isEmpty(self):
        return len(self.que)
    def insert(self, data):
        self.que.insert(0, data)
    def delete(self):
        if self.isEmpty():
            return self.que.pop()
        else:
            return 'queue is underflow'
    def display(self):
        if self.isEmpty():
            return self.que
        else:
            return 'queue is empty'

obj = Queue()
obj.insert(50)
obj.insert(40)
obj.insert(30)
obj.insert(20)
obj.insert(10)
print(obj.display())
print(obj.delete())
print(obj.display())



# deque usning collections
from collections import deque
que = deque([1,2 ,3 ,4])
que.appendleft(50)
que.append(60)
print(que)
que.popleft()
que.pop()
print(que)
print(type(que))