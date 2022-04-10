class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []
        for i in range(len(ops)):
            if ops[i] == "C": records.pop()
            elif ops[i] == "D": records.append(2*records[-1])
            elif ops[i] == "+": records.append(records[-1] + records[-2])
            else: records.append(int(ops[i]))
        
        return sum(records)
                
        