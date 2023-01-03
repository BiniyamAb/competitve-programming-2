class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        
        k -= 1
        curr = 0
        while len(friends) > 1:
            curr = (curr + k) % len(friends)
            friends.pop(curr)
        
        return friends[0]
            
            