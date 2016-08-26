from LokiStack import Stack


class SortStack:
    def __init__(self):
        self.mainStack = Stack()
        self.tempStack = Stack()
        self.mainStack.push(1)
        self.mainStack.push(2)
        self.mainStack.push(3)
        self.mainStack.push(4)
        self.mainStack.push(5)
        self.mainStack.push(6)

    def sort(self):
        while not self.mainStack.isEmpty():
            temp = self.mainStack.pop()
            while not self.tempStack.isEmpty() and self.tempStack.peek() > temp:
                self.mainStack.push(self.tempStack.pop())
            self.tempStack.push(temp)
            print(self.tempStack.items)

        while not self.tempStack.isEmpty():
            self.mainStack.push(self.tempStack.pop())


mySortStack = SortStack()
print(mySortStack.mainStack.items)
mySortStack.sort()
print(mySortStack.mainStack.items)
