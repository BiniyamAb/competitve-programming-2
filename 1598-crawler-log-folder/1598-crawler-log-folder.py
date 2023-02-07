class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder = 0
        for log in logs:
            if log == './': pass
            elif log == '../':
                folder = max(0, folder - 1)
            else:
                folder += 1
                
        return folder
        