class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.points = []
        
    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points.append(point)
        self.freq[point] += 1 

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        
        for a, b in self.points:
            if abs(x-a) == abs(y-b) and (x != a): 
                count += self.freq[(a, y)] * self.freq[(x, b)]
        
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)