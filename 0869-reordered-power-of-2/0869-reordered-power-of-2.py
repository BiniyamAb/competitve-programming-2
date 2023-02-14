class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        for i in range(30):
            temp = str(1 << i)
            if count == Counter(temp):
                return True
            
        return False