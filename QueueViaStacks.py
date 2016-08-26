from LokiStack import Stack


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, element):
        self.s1.push(element)

    def dequeue(self):
        if self.s2.isEmpty():
            if self.s1.isEmpty():
                print("Empty Queue!")
                return
            else:
                while not self.s1.isEmpty():
                    self.s2.push(self.s1.pop())
        return self.s2.pop()


myQ = MyQueue()
myQ.enqueue(1)
myQ.enqueue(2)
print(myQ.dequeue())
myQ.enqueue(3)
print(myQ.dequeue())
myQ.enqueue(4)
print(myQ.dequeue())
myQ.enqueue(5)
print(myQ.dequeue())
print(myQ.dequeue())
print(myQ.dequeue())

