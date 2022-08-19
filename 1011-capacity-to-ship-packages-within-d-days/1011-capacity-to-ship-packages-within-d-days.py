class Solution:
    def findMaxAndSum(self,weights):
        total_weight = 0
        max_weight = 0
        for weight in weights:
            total_weight += weight
            max_weight = max(max_weight,weight)
        
        return [max_weight,total_weight]
    
    def possibleCapacity(self,weights,capacity,days):
        sum_so_far = 0
        day_count = 1
        for weight in weights:
            sum_so_far += weight
            if sum_so_far > capacity:
                day_count += 1
                sum_so_far = weight
            if day_count > days: 
                return False
        
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = self.findMaxAndSum(weights)
        answer = -1
        while left <= right:
            mid = left + (right - left) // 2
            valid_capacity = self.possibleCapacity(weights,mid,days)
            if valid_capacity:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
            
    