class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = []
        l = max_pick = 0
        for r in range(len(fruits)):
            if len(types) == 2 and (fruits[r] == types[0][0] or fruits[r] == types[1][0]):
                if fruits[r] == types[0][0]: types[0][1] = r
                else: types[1][1] = r
                continue
            elif len(types) == 1 and fruits[r] == types[0][0]:
                types[0][1] = r
                continue
            elif len(types) < 2:
                types.append([fruits[r], r])
                continue
            print(r)
            max_pick = max(max_pick, r-l)
            types.sort(key=lambda x: x[1], reverse=True)
            l = types.pop()[1] + 1
            types.append([fruits[r], r])
        
        print(len(fruits), l)
        return max(max_pick, len(fruits) - l)
            
            
        