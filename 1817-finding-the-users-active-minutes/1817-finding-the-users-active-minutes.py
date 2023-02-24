class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uams = defaultdict(set)
        for user, minute in logs:
            uams[user].add(minute)
        
        answer = [0] * k
        for key, val in uams.items():
            answer[len(val)-1] += 1
        
        return answer
                
        