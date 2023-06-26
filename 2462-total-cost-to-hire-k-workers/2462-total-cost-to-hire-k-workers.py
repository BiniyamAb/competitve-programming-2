class Solution:
    def totalCost(self, cst, k, c):
        
        n, res = len(cst), 0
        pairs  = [(t, i) for i, t in enumerate(cst)]
        l, r   = min(c,n//2), max(n-c,n//2)
        pq     = pairs[:l] + pairs[r:]
        heapify(pq)

        for _ in range(k):
            cost, i = heappop(pq)
            if i < l  : i, l = l, l+1
            if i >= r : i, r = r-1, r-1                
            if l <= r : heappush(pq, pairs[i]) 
            res += cost
        
        return res