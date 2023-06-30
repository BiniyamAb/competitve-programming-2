class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        
        nums1_only = nums1[:m]
        i = j = k = 0
        
        while i < len(nums1_only) or j < len(nums2):
            
            if not i < len(nums1_only):
                nums1[k] = nums2[j]
                j += 1
            
            elif not j < len(nums2):
                nums1[k] = nums1_only[i]
                i += 1
            
            else:
                if nums1_only[i] <= nums2[j]:
                    nums1[k] = nums1_only[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
                    
            k += 1
                
        