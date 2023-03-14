class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(nums: List[int], p1, p2, turn):
            
            if len(nums) == 1:
                if turn == 1:
                    p1 += nums[0]
                else:
                    p2 += nums[0]
                    
                return p1 >= p2
                        
            else:
                if turn == 1:
                    canP1Win = helper(nums[1:], p1 + nums[0], p2, 2)
                    if canP1Win: return True
                    
                    canP1Win = helper(nums[:-1], p1 + nums[-1], p2, 2)
                    if canP1Win: return True
                    
                    return False
                
                if turn == 2:
                    canP1Win = helper(nums[1:], p1, p2 + nums[0], 1)
                    if not canP1Win: return False
                    
                    canP1Win = helper(nums[:-1], p1, p2 + nums[-1], 1)
                    if not canP1Win: return False
                    
                    return True
               
        canP1Win = helper(nums, 0, 0, 1)
        return canP1Win