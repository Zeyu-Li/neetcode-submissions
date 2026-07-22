class DynamicArray:
    arr: List[int] = []
    capacity: int = 0
    size: int = 0
    def __init__(self, capacity: int):
        self.arr = [0 for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # old_cap = self.capacity
        # self.capacity *= 2
        # self.arr += [0] * old_cap
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity 
        
        # Copy elements to new_arr
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
