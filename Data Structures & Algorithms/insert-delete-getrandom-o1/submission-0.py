import random 

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.arr.append(val)
            self.map[val] = len(self.arr) - 1
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            remove_index = self.map[val]
            last = len(self.arr) - 1

            self.arr[remove_index] = self.arr[last]
            self.map[self.arr[last]] = remove_index

            self.arr.pop()
            del self.map[val]

            return True
 

    def getRandom(self) -> int:
        return random.choice(self.arr)





# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()