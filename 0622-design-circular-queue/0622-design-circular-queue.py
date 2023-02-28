class MyCircularQueue:

    def __init__(self, k: int):
        self.start = 0
        self.size = 0
        self.buffer = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buffer[(self.start+self.size) % len(self.buffer)] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start+1) % len(self.buffer)
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.buffer[self.start]
        

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.buffer[(self.start+self.size-1) % len(self.buffer)]


    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.buffer)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()