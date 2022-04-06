class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = collections.Counter(arr)
        ans = 0
        for i, j in itertools.combinations_with_replacement(count, 2):
            k = target - i - j
            if i == j == k: ans += count[i] * (count[i] - 1) * (count[i] - 2) / 6
            elif i == j != k: ans += count[i] * (count[i] - 1) / 2 * count[k]
            elif k > i and k > j: ans += count[i] * count[j] * count[k]
                
        return int(ans % (10**9 + 7))
        