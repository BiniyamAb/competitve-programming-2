class Solution:
    def minimumBuckets(self, street: str) -> int:
        if (len(street) == 2 or len(street) == 1) and "." not in street: return -1
        elif len(street) == 1: return 0
        if "." not in [street[-1],street[-2]] or "." not in [street[0],street[1]]: return -1
        for i in range(1,len(street)-1):
            if street[i] == street[i-1] == street[i+1] == "H": return -1
        
        buckets = street.count("H")
        street = list(street)
        for i in range(1,len(street)-1):
            if street[i] == "." and (street[i-1] == street[i+1] == "H"): 
                street[i+1] = street[i-1] = "B"
                buckets-=1
        
        return buckets