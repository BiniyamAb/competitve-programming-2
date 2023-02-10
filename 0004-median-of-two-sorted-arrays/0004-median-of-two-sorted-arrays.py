class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        
        if len(num) % 2:
            return num[len(num) // 2]
        else:
            return (num[len(num) // 2] + num[len(num) // 2 - 1]) / 2