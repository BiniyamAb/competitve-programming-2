class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        N, M = len(grid), len(grid[0])
        inBound = lambda r, c: 0 <= r < N and 0 <= c < M
        visited = {(0,0): k}
        queue = deque([(0,0,k,0)])
        DIR = (1,0,-1,0,1)

        while queue:
            curr = queue.popleft()
            curr_r, curr_c, curr_k, curr_steps = curr
            if (curr_r,curr_c) == (N-1,M-1):
                return curr_steps
            for i in range(4):
                new_r, new_c = curr_r + DIR[i], curr_c + DIR[i+1]
                if inBound(new_r, new_c):
                    new_k = curr_k
                    new_steps = curr_steps + 1
                    if grid[new_r][new_c] == 1:
                        new_k -= 1
                    new_move = (new_r,new_c,new_k,new_steps)
                    if ((new_r,new_c) not in visited or new_k > visited[(new_r,new_c)]) and new_k >= 0:
                        queue.append(new_move)
                        visited[(new_r,new_c)] = new_k
        
        return -1
        
        
        