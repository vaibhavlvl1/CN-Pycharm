"""
 Code : Max Priority Queue
Send Feedback
Implement the class for Max Priority Queue which includes following functions -
1. getSize -
Return the size of priority queue i.e. number of elements present in the priority queue.
2. isEmpty -
Check if priority queue is empty or not. Return true or false accordingly.
3. insert -
Given an element, insert that element in the priority queue at the correct position.
4. getMax -
Return the maximum element present in the priority queue without deleting. Return -Infinity if priority queue is empty.
5. removeMax -
Delete and return the maximum element present in the priority queue. Return -Infinity if priority queue is empty.
Note : main function is given for your reference which we are using internally to test the class.

"""


class PQNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class MaxPriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize == 0

    def getMax(self):
        return self.pq[0].value

    def insert(self, value, priority):
        newNode = PQNode(value, priority)
        self.pq.append(newNode)
        self.heapifyUp()

    def heapifyUp(self):
        childIndex = self.getSize() - 1

        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2

            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def removeMax(self):
        if self.isEmpty():
            return None

        temp = self.pq[0]

        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()

        self.heapifyDown()

        return temp.value

    def heapifyDown(self):
        parentIndex = 0

        while parentIndex * 2 + 2 < self.getSize():
            LchildIndex = (parentIndex * 2) + 1
            RchildIndex = (parentIndex * 2) + 2

            if self.pq[LchildIndex].priority > self.pq[RchildIndex].priority:
                maxIndex = LchildIndex
            else:
                maxIndex = RchildIndex

            if self.pq[parentIndex].priority < self.pq[maxIndex].priority:
                self.pq[parentIndex], self.pq[maxIndex] = self.pq[maxIndex], self.pq[parentIndex]
                parentIndex = maxIndex
            else:
                break


MaxPQ = MaxPriorityQueue()

Input = [int(x) for x in input().split()]
choice = Input[0]
i = 1
while choice != -1:
    if choice == 1:
        priority = Input[i]
        value = Input[i]
        i += 1
        MaxPQ.insert(value, priority)
    elif choice == 2:
        print(MaxPQ.getMax())
    elif choice == 3:
        print(MaxPQ.removeMax())

    elif choice == 4:
        print(MaxPQ.getSize())
    elif choice == 5:
        if MaxPQ.isEmpty():
            print("true")
        else:
            print("false")
        break
    else:
        pass
    choice = Input[i]
    i += 1
