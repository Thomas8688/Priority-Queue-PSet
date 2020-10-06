class priQueue:
    def __init__(self, size):
        if isinstance(size, int):
            self.__size = size
        else:
            self.__size = 10
        self.__queue = ["-" for i in range(self.__size)]
        self.__headP = -1
        self.__tailP = -1

    def enqueue(self, item):
        if isinstance(item, list):
            if len(item) == 2:
                data, prio = item
                if isinstance(data, str) and isinstance(prio, int) and prio >= 0:
                    if self.isEmpty():
                        self.__headP = 0
                        self.__tailP = 0
                        self.__queue[self.__tailP] = item
                    elif not self.isFull():
                        index = self.findIndex(prio)
                        self.addItem(item, index)
                        self.__tailP += 1
                    else:
                        print("Queue Full")
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")

    def dequeue(self):
        if not self.isEmpty():
            item = self.__queue[self.__headP]
            self.__queue[self.__headP] = "-"
            item = item[0]
            print(item, "has been Dequeued\n")
            if self.__tailP == self.__headP:
                self.__tailP = -1
                self.__headP = -1
                print("Last item Dequeued: Queue Reset\n")
            else:
                self.__headP += 1
            return item
        else:
            print("Queue is Empty: No items to Dequeue\n")


    def isFull(self):
        if self.__tailP + 1 == self.__size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.__tailP == -1 and self.__headP == -1:
            return True
        else:
            return False

    def addItem(self, item, index):
        for i in range(self.__tailP+1, index, -1):
            self.__queue[i] = self.__queue[i-1]
        self.__queue[index] = item

    def findIndex(self, prio):
        prioList = []
        index = None
        for item in self.__queue:
            if item == "-":
                prioList.append("-")
            else:
                prioList.append(item[1])
        i = self.__tailP+1
        while i != self.__headP:
            if prioList[i-1] <= prio:
                index = i
                break
            i -= 1
        if not index:
            index = self.__headP
        return index

    def printList(self):
        print(self.__queue)


#TESTING
myQ = priQueue(5)
myQ.dequeue()
myQ.enqueue(["Tom", 1])
myQ.enqueue(["Jem", 2])
myQ.enqueue(["Jac", 3])
myQ.enqueue(["Dunc", 1])
myQ.dequeue()
myQ.enqueue(["Sal", 0])
myQ.enqueue(["Booc", 1])
myQ.dequeue()
myQ.enqueue(["Booc", 1])
myQ.dequeue()
myQ.enqueue(["Booc", 1])
myQ.dequeue()
myQ.enqueue(["Booc", 1])
myQ.dequeue()
myQ.enqueue(["Booc", 1])
myQ.dequeue()
