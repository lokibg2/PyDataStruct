from LokiStack import Stack
import sys
# Min Stack - O(1)


class MinStack(Stack):
    def __init__(self):
        super(MinStack, self).__init__()
        self.s2 = Stack()

    def min(self):
        if self.s2.isEmpty():
            return sys.maxsize
        return self.s2.peek()

    def push(self, item):
        if item <= self.min():
            self.s2.push(item)
        super(MinStack, self).push(item)

    def pop(self):
        temp = super(MinStack, self).pop()
        if temp == self.min():
            self.s2.pop()
        return temp


s = MinStack()
s.push(75)
s.push(134)
s.push(12)
s.push(1344)
s.push(1234)
s.push(1)
s.pop()
print(s.min())
