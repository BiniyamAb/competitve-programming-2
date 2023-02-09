class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = list(str(num))
        sorted_temp = sorted(temp, reverse=True)
        n = len(temp)
        
        i = 0
        while i < n and temp[i] == sorted_temp[i]: i += 1
        if i == n: return num
        
        ind = i
        for j in range(i+1,n):
            if temp[j] >= temp[ind]:
                ind = j
        
        temp[i], temp[ind] = temp[ind], temp[i]
        temp = int("".join(temp))
        
        return temp