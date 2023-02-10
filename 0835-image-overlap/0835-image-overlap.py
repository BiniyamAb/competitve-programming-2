class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        count = [0] * (2*len(img1)-1)**2
        for i, row in enumerate(img1):
            for j, v in enumerate(row):
                if not v:
                    continue
                for i2, row2 in enumerate(img2):
                    for j2, v2 in enumerate(row2):
                        if not v2:
                            continue
                        count[(len(img1)-1+i-i2)*(2*len(img1)-1) +
                              len(img1)-1+j-j2] += 1
        return max(count)