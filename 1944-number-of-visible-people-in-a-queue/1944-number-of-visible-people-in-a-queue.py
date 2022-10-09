class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = [0] * len(heights)
        stack = []
        for i in range(len(heights)):
            height = heights[i]
            while stack and height > heights[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] += 1

            if stack: 
                result[stack[-1]] += 1
            stack.append(i)

        return result
        