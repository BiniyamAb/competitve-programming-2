class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        position = defaultdict()
        for i,letter in enumerate(word):
            if letter == letter.upper():
                if not position.get(letter): position[letter] = i + 1
            else:
                position[letter] = i + 1

        specials = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if position.get(letter) and position.get(letter.upper()) and position[letter] < position[letter.upper()]:
                specials += 1
        
        return specials
        
        