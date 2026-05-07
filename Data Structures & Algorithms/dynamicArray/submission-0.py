class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity #initialise the array to be filled with 0s first
        self.size = 0 #Set the size to be 0 initially

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        #After resizing or if there is still capacity, then add the element n to the back of the array
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        #Pop from the back of the arr
        self.size -= 1
        temp = self.arr[self.size]
        self.arr[self.size] = 0
        return temp

    def resize(self) -> None:
        #Double the current capcity of the arr
        self.capacity *= 2
        newArr = [0] * self.capacity
        for i in range(self.size):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity