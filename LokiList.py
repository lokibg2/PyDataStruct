class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.last = head

    def getHead(self):
        return self.head

    def getLast(self):
        return self.last

    def setLast(self, newLast):
        self.last = newLast

    def isEmpty(self):
        return self.head is None

    def add(self, ele):
        tempNode = Node(ele)
        tempNode.setNext(self.head)
        self.head = tempNode
        if self.size() == 1:
            self.last = tempNode

    def size(self):
        curr = self.head
        count = 0
        while curr is not None:
            curr = curr.getNext()
            count += 1
        return count

    def search(self, key, index=False):
        curr = self.head
        count = -1
        while curr is not None:
            count += 1
            if curr.getData() == key:
                if index:
                    return count
                return curr
            curr = curr.getNext()

        if index:
            return -1
        return None

    def remove(self, key):
        if self.head is None:
            return

        if self.head.getData() == key:
            self.head = self.head.getNext()
            return

        prev = self.head
        while prev.getNext() is not None:
            if prev.getNext().getData() == key:
                break
            else:
                prev = prev.getNext()

        if prev.getNext().getNext() is None:
            self.setLast(prev)
        prev.setNext(prev.getNext().getNext())

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.getData(), end=" ")
            curr = curr.getNext()
        print('')

    def revTraverse(self, curr):
        if curr is not None:
            self.revTraverse(curr.getNext())
            print(curr.getData(), end=" ")
        else:
            print('')

    def append(self, ele):
        last = self.getLast()
        if last is None:
            self.add(ele)
        else:
            node = Node(ele)
            self.getLast().setNext(node)
            self.setLast(node)

    def pop(self):
        self.remove(self.getLast().getData())

    def insert(self, ele, after):
        if after == self.getLast().getData():
            self.append(ele)
        else:
            prev = self.search(after)
            node = Node(ele)
            node.setNext(prev.getNext())
            prev.setNext(node)


myList = LinkedList()
myList.append(100)
myList.append(200)
myList.append(300)
myList.append(400)
myList.traverse()
print(myList.getHead().getData())
myList.add(50)
myList.traverse()
myList.pop()
myList.insert(10, 300)
myList.insert(10, 200)
myList.insert(10, 100)
myList.insert(10, 10)
myList.traverse()
