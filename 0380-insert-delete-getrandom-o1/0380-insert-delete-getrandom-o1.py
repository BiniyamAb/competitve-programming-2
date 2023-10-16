class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.nums_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.nums_dict:
            return False
        else:
            self.nums.append(val)
            self.nums_dict[val] = len(self.nums) - 1
            return True      

    def remove(self, val: int) -> bool:
        if val in self.nums_dict:
            index = self.nums_dict[val]
            self.nums_dict[self.nums[-1]] = index
            self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
            self.nums.pop()          
            del self.nums_dict[val]
            return True
            
        else:
            return False
        
    def getRandom(self) -> int:
        random_index = random.randint(0,len(self.nums)-1)
        return self.nums[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()