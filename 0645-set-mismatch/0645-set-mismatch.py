class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        for i in range(1,len(nums)+1):
            freq[i] += 1
            if freq[i] == 3:
                repeated = i
            if freq[i] == 1:
                missing = i
        
        return [repeated,missing]