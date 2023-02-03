class Solution:    
    def __init__(self, w: List[int]):
        num, arr = 0, []
        for i in w:
            num += i
            arr.append(num)
            
        self.left = arr
        self.max = num

    def pickIndex(self) -> int:
        n = randrange(self.max)
        return bisect_right(self.left, n)
    
    
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()