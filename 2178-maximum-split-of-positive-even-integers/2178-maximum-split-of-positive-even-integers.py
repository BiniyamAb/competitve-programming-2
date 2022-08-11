class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0: return []
        nums = set()
        even, sum = 2, 0
        while sum <= finalSum:
            sum+=even
            nums.add(even)
            even+=2

        nums.remove(sum-finalSum)
        return list(nums)
            
        