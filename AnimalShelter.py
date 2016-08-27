from LokiQ import Queue


class Animal():
    def __init__(self, name, no):
        self.name = name
        self.regNo = no


class Dog(Animal):
    def __init__(self, name, no):
        super(Dog, self).__init__(name,no)


class Cat(Animal):
    def __init__(self, name, no):
        super(Cat, self).__init__(name,no)


class AnimalShelter():
    def __init__(self):
        self.dogQ = Queue()
        self.catQ = Queue()

    def enqueue(self, animal):
        if type(animal) is Cat:
            self.catQ.enqueue(animal)
        elif type(animal) is Dog:
            self.dogQ.enqueue(animal)
        else:
            print("Unknown Animal")

    def dequeueCat(self):
        if self.catQ.size() == 0:
            print('No Cats Left')
        else:
            return self.catQ.dequeue()

    def dequeueDog(self):
        if self.dogQ.size() == 0:
            print('No Dogs Left')
        else:
            return self.dogQ.dequeue()

    def dequeueAny(self):
        if self.dogQ.isEmpty() and self.catQ.isEmpty():
            print("No Animals Left")
        elif self.dogQ.isEmpty() :
            return self.catQ.dequeue()
        elif self.catQ.isEmpty():
            return self.dogQ.dequeue()

        if self.dogQ.peek().regNo < self.catQ.peek().regNo:
            return self.dogQ.dequeue()
        return self.catQ.dequeue()

