class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = [[float("inf"),0]]
        for i in range(len(plantTime)):
            times.append([growTime[i], plantTime[i]])
        times.sort(reverse=True)
        times[0][0] = 0
        max_bloom_day = 0
        for i in range(1,len(times)):
            prev_plant_time = times[i-1][1] 
            times[i][1] += prev_plant_time
            grow_time, plant_time = times[i]
            bloom_day = plant_time + grow_time   
            max_bloom_day = max(max_bloom_day, bloom_day)
        
        return max_bloom_day