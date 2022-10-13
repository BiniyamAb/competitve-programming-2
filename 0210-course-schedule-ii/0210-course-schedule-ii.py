from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1
            
        todo = []
        for index, count in enumerate(incoming):
            if count == 0:
                todo.append(index)
                
        answer = []
        colors = [0] * numCourses
        for current_root_node in todo:
            cycle_found = self.hasCycle(current_root_node, colors, graph, answer)
            if cycle_found:
                return []
        
        answer.reverse()
        if len(answer) != numCourses: return []
        return answer
    
    def hasCycle(self, current_node, colors, graph, answer):
        # No cycle
        if colors[current_node] == 2:
            return False
        
        # Cycle found
        if colors[current_node] == 1:
            return True
        
        # Mark it as gray, half dirty
        colors[current_node] = 1
        
        for neighbor in graph[current_node]:
            cycle_found = self.hasCycle(neighbor, colors, graph, answer)
            if cycle_found:
                return True
        
        # Color it black, which is safe
        colors[current_node] = 2
        answer.append(current_node)
        return False