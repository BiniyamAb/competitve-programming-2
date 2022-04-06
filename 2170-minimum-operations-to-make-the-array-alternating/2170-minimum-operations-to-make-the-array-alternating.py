class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        evens, odds, evenLen, oddLen = {}, {}, 0, 0
        for i, num in enumerate(nums):
            if i%2 == 0:
                evens[num] = evens.get(num, 0) + 1
                evenLen+=1
            else:
                odds[num] = odds.get(num, 0) + 1
                oddLen+=1
        
        evenOrder = sorted(evens, key=evens.get)
        oddOrder = sorted(odds, key=odds.get)
        even = evenOrder.pop()
        odd = oddOrder.pop()
        
        if even != odd: pass
        elif not evenOrder and not oddOrder:
            return len(nums) - max(evens[even], odds[odd])
        elif not oddOrder:
            even = evenOrder.pop()
        elif not evenOrder:
            odd = oddOrder.pop()
        else:
            if evens[even] != odds[odd]:
                if evens[even]  + odds[oddOrder[-1]] > odds[odd] + evens[evenOrder[-1]]:
                    odd = oddOrder.pop()
                else:
                    even = evenOrder.pop()
            else:
                return len(nums) - evens[even] - max(evens[evenOrder.pop()], odds[oddOrder.pop()])   
                
        return evenLen - evens[even] + oddLen - odds[odd]
        
            
        