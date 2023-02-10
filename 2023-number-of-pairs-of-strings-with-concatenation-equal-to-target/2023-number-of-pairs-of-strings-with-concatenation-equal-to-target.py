class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        temp = defaultdict(str)
        for i in range(len(target)): temp[target[:i+1]] = target[i+1:]
        freq = Counter(nums)
        
        pairs = 0
        for k,v in temp.items():
            if v in freq and k in freq:
                if v != k: pairs += freq[k]*freq[v]
                else: pairs += freq[k]*(freq[v]-1)

        return pairs