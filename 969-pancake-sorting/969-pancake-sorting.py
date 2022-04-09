class Solution:        
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l+1, r-1
                
        k_arr =[]
        for num in range(len(arr), 0, -1):
            ind = arr.index(num)
            if ind != 0:
                reverse(0, ind)
                k_arr.append(ind+1)
            reverse(0, num-1)
            k_arr.append(num)
            
        return k_arr
        
                
        