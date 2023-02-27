class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = [0] * 101
        for birth, death in logs:
            for i in range(birth, death):
                count[i-1950] += 1
        
        ind = 0
        max_population = count[0]
        for i in range(1,len(count)):
            if count[i] > max_population:
                ind = i
                max_population = count[i]
        
        return ind + 1950