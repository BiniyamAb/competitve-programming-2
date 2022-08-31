from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for ith_node in range(numCourses):
            incoming[ith_node]
        
        for a, b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1
            
        todo = deque([])
        for index, count in incoming.items():
            if count == 0:
                todo.append(index)
        
        answer = []
        while todo:
            current_node = todo.popleft()
            answer.append(current_node)
            for neighbor in graph[current_node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    todo.append(neighbor)
        
        course_length = len(answer)
        if course_length != numCourses:
            return []
        
        return answer