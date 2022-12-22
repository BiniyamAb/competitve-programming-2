class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def visit(i):
            visited.add(i)
            for room_key in rooms[i]:
                if room_key not in visited:
                    visit(room_key)
            
        visit(0)
        return len(visited) == len(rooms)
            
        