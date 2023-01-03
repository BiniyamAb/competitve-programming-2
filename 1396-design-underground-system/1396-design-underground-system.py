class UndergroundSystem:

    def __init__(self):
        self.average_times = defaultdict(int)
        self.num_of_travels = defaultdict(int)
        self.checkins = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName,t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkins[id]
        path = (start_station,stationName)
        average = (self.average_times[path] * self.num_of_travels[path]) + (t - start_time)
        average /= (self.num_of_travels[path] + 1)
        self.average_times[path] = average
        self.num_of_travels[path] += 1
        del self.checkins[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average_times[(startStation,endStation)]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)