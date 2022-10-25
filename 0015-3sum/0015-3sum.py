class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            self.twoSum(nums, i+1,target,results)
            
        results = [list(result) for result in results]
        return results
        
    def twoSum(self, nums, start_index, target, results):
        differences = {}
        for i in range(start_index,len(nums)):
            if nums[i] in differences:
                sorted_triplet = tuple(sorted([nums[differences[nums[i]]],nums[i],nums[start_index-1]]))
                results.add(sorted_triplet)
                
            differences[target-nums[i]] = i
        