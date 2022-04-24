class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkins.pop(id)
        time = t - start_time
        if self.times.get((start_station,stationName)) is not None:
            self.times[(start_station,stationName)][0] += time
            self.times[(start_station,stationName)][1] += 1
        else:
            self.times[(start_station,stationName)] = [time,1]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, travels = self.times[(startStation,endStation)]
        return time/travels
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)