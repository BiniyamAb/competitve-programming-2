class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp_arr= []
        pointer = 0       
        for i in range(len(arr)):
            if arr[i] == 0:
                temp_arr.append(0)
            if temp_arr:
                temp_arr.append(arr[i])
                arr[i] = temp_arr[pointer]
                pointer += 1
            
        
        
                
                
        