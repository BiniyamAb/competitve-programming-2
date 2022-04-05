class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leads, freq, leader = [], {}, -1
        for person in self.persons:
            freq[person] = freq.get(person, 0) + 1
            if freq[person] >= freq.get(leader, 0): leader = person
            self.leads.append(leader)

    def q(self, t: int) -> int:
        l, r, best = 0, len(self.times) - 1, -1
        while l <= r:
            mid = l + (r-l)//2
            if self.times[mid] <= t:
                best = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return self.leads[best]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)