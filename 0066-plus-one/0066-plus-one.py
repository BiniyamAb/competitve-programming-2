class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            num = digits[i] + 1
            digits[i] = num
            if num != 10:
                break
            digits[i] = 0
            
            i -= 1
        if digits[0] == 0: digits.insert(0,1)
        
        return digits