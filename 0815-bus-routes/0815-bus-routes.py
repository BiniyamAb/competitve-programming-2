class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        
        graph = defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                graph[stop].append(i)
                
        steps = 0
        queue = graph[source]
        visited = set()
        
        while queue:
            next_ = []
            for bus in queue:
                if bus not in visited:
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == target: return steps + 1
                        for second_bus in graph[stop]:
                            if second_bus not in visited:
                                next_.append(second_bus)
                                
            queue = next_
            steps += 1
            
        return -1