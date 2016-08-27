class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, ele):
        self.items.append(ele)

    def dequeue(self):
        if self.size() == 0:
            print('Empty Queue!')
            return
        return self.items.remove(0)

    def peek(self):
        if self.size() == 0:
            print('Empty Queue!')
            return
        return self.items[0]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)