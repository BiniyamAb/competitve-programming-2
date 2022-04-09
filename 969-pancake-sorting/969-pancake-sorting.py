class Solution:
    def reverse(self, l, r, arr):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l+1, r-1
        
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k_arr =[]
        for num in range(len(arr), 0, -1):
            ind = arr.index(num)
            if ind != 0:
                self.reverse(0, ind, arr)
                k_arr.append(ind+1)
            self.reverse(0, num-1, arr)
            k_arr.append(num)
            
        return k_arr
        
                
        