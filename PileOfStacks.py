from LokiStack import Stack


class PileOfStacks:
    def __init__(self, sizePerStack):
        self.stackList = []
        self.stackInd = 0
        self.sizePerStack = sizePerStack
        self.createStack()

    def createStack(self):
        self.stackList.append(Stack())

    def removeStack(self):
        self.stackList.pop()

    def push(self, ele):
        if len(self.stackList) == 0:
            self.createStack()

        if self.stackList[self.stackInd].size() == self.sizePerStack:
            self.createStack()
            self.stackInd += 1
        self.stackList[self.stackInd].push(ele)

    def pop(self):
        x = self.stackList[self.stackInd].pop()
        if self.stackList[self.stackInd].isEmpty():
            self.removeStack()
            if self.stackInd != 0:
                self.stackInd -= 1
        return x


pos = PileOfStacks(3)

pos.push(1)
pos.push(2)
pos.pop()
pos.push(3)
pos.push(4)
pos.push(5)
pos.push(6)

pos.push(7)
pos.push(8)
pos.push(9)
pos.push(10)
pos.pop()
pos.pop()
pos.pop()

for i in pos.stackList:
    print(i.items)

