class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        # if tickets[k] == 1: n = k+1
        for i in range(n):
            if i > k:
                time += min(tickets[i], tickets[k] - 1)
            else:
                time += min(tickets[i],tickets[k])
        
        return time
        