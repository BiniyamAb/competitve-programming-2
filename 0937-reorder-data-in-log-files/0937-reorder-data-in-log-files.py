class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            curr = log.split()
            if curr[-1].isdigit():
                digits.append(log)
            else:
                letters.append(tuple([curr[1:], [curr[0]]]))

        arr = []
        letters.sort()
        for letter in letters:
            letter, char = letter
            arr.append(char[0] + " " + " ".join(letter))
            
        for digit in digits: arr.append(digit)
        return arr