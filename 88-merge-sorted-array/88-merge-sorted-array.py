class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,len(nums1)): nums1[i] = "0"
        for i in range(len(nums2)):
            num = nums2[i]
            ind = len(nums1)-1
            for j in range(len(nums1)):
                if nums1[j] == "0" or num <= nums1[j]:
                    ind = j
                    break
            prev = num
            for k in range(ind,len(nums1)):
                prev, nums1[k] = nums1[k], prev
            
        
        
                
        