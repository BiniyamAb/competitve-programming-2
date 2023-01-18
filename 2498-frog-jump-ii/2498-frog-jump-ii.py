class Solution:
    def maxJump(self, stones: List[int]) -> int:
        cost = stones[-1] - stones[-2]
        for i in range(len(stones)-2):
            curr_cost =  stones[i+2] - stones[i]
            cost = max(cost, curr_cost)
        
        return cost
        