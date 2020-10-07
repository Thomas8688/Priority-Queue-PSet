#Class created to implement the priority queue data struct
class priQueue:
#Initialisation
    def __init__(self, size):
        print ("Creating Queue...")
#If the input for queue size is not an integer, the queue size will be set to a default 10
#Otherwise the queue size will be set to the users input
        if isinstance(size, int):
            self.__size = size
        else:
            self.__size = 10
            print("Invalid Queue Size: Set to Default (10)")
#Sets the queue to a list of size: self.__size with each piece of data being a null value "-
        self.__queue = ["-" for i in range(self.__size)]
#Sets the pointers to -1 (Indexing starts at 0, so this can indicate whether or not the queue is empty)
        self.__headP = -1
        self.__tailP = -1
        print ("Queue Created")

#Method used to enqueue an item
    def enqueue(self, item):
#Checks if the item passed to the method is a list
        if isinstance(item, list):
#Checks if the list is the correct length (2 Items)
            if len(item) == 2:
#Sets the first item in the list to the data value, and the second item to the item priority
                data, prio = item
#Checks that the data value is a string, and the priority is a number
                if isinstance(data, str) and isinstance(prio, int) and prio >= 0:
#If this is the first item being added to the queue, the head and tail pointers are both set to point to the first index
                    if self.isEmpty():
                        self.__headP = 0
                        self.__tailP = 0
#and the item is added into the first position
                        self.__queue[self.__tailP] = item
                        print(data, "Enqueued\n")
#Otherwise, if the queue is not empty OR full then the correct index value needs to be found so that the item can be inserted into the correct position in the queue
                    elif not self.isFull():
#Calls the findIndex method to find the correct index
                        index = self.findIndex(prio)
#Calls the addItem method so that the item is properly inserted
                        self.addItem(item, index)
#Tail pointer is moved one index up the queue
                        self.__tailP += 1
                        print(data, "Enqueued\n")
                    else:
                        print("Queue is full:", data, "can not be Enqueued\n")
                else:
                    print("Invalid Item: Not in the form [str, int]\n")
            else:
                print("Invalid Item: Not in the form [str, int]\n")
        else:
            print("Invalid Item: Not in the form [str, int]\n")

#Method used to Dequeue an item
    def dequeue(self):
#Checks if the queue is empty
        if not self.isEmpty():
#The item being dequeued is taken using the head pointer
            item = self.__queue[self.__headP]
#The item's position in the queue is reset to the null value "-"
            self.__queue[self.__headP] = "-"
#Sets the item to the first item in item
            item = item[0]
            print(item, "has been Dequeued\n")
#If this is the last item being dequeued, then the queue will reset (Allowing more values to be added again)
            if self.__tailP == self.__headP:
                self.__tailP = -1
                self.__headP = -1
                print("Last item Dequeued: Queue Reset\n")
#Otherwise the head pointer is moved to the next item in the queue
            else:
                self.__headP += 1
            return item
        else:
            print("Queue is Empty: No items to Dequeue\n")
#If the queue is empty, None is returned
            return None

#Method to check if the queue is full
    def isFull(self):
#Checks if the queue is full by seeing if the next index is equal to the maximum index value of the list
        if self.__tailP + 1 == self.__size:
            return True
        else:
            return False

#Method to check if the queue is empty
    def isEmpty(self):
#Checks if the queue is empty by seeeing if both pointers are defaulted (at -1)
        if self.__tailP == -1 and self.__headP == -1:
            return True
        else:
            return False

#Method used to find the point at which the item needs to be added to the queue
    def findIndex(self, prio):
        prioList = []
        index = None
#Adds the priorites of all items in the queue to a new list
        for item in self.__queue:
            if item == "-":
                prioList.append("-")
            else:
                prioList.append(item[1])
#Sets a counter to i, to be used in the while loop
        i = self.__tailP+1
#Loop starts at the tail pointer, and keeps looping until i is equal to the head pointer
        while i != self.__headP:
#If the item in the priority list is less than or equal to the priority of the new item, the index will be set to i (counter)
            if prioList[i-1] <= prio:
                index = i
#This immediately ends the while loop
                break
#Otherwise the next item in the priority list is checked (moving backwards) by decreasing the counter by one.
            i -= 1
#If no index has been set, then the new item is first priority and needs to be added to the front of the list, otherwise the index found is returned
        if not index:
            index = self.__headP
        return index

#Method to add an item in the correct position of the queue (depending on priority)
    def addItem(self, item, index):
#Takes the item of the queue at index, and shifts it AND all items afterwards one space backwards
#Loop starts at the end of the list and shifts the items one by one until the index value is reached
        for i in range(self.__tailP+1, index, -1):
            self.__queue[i] = self.__queue[i-1]
#Inserts the item in the now available slot in the queue
        self.__queue[index] = item

#Prints the Queue (USED FOR TESTING)
    def printList(self):
        print(self.__queue, "\n")


#TESTING
myQ = priQueue(5)
myQ.dequeue()
myQ.enqueue(["Tom", 1])
myQ.enqueue(["Jem", 2])
myQ.enqueue(["Jac", 3])
myQ.enqueue(["Dunc", 1])
myQ.dequeue()
myQ.enqueue(["Sal", 0])
myQ.dequeue()
#ERROR HANDLING TESTING
myQ2 = priQueue("Hello")
myQ3 = priQueue(2)
myQ3.dequeue()
myQ3.enqueue(["Booc", 1])
myQ3.enqueue(["G", 3])
myQ3.dequeue()
myQ3.enqueue(["Da", 2])
myQ3.enqueue(["Sal", 1])
myQ3.enqueue("Jo")
myQ3.enqueue([4,"Jo"])
myQ3.enqueue(["Jo", "Al", 4])
myQ3.dequeue()
