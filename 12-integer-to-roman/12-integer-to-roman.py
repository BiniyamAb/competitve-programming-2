class Solution:
    def intToRoman(self, num: int) -> str:
        places = [("I", "V"), ("X", "L"), ("C", "D"), ("M","Nan")]
        str_num = str(num)
        digit_len = len(str_num)
        roman = []
        for i in range(digit_len):
            dig = int(str_num[i])
            place = digit_len - i - 1
            less_5, greater_5 = places[place]
            if 1 <= dig <= 3:
                roman.append(less_5 * dig)
            elif dig == 4:
                roman.append(less_5 + greater_5)
            elif 5 <= dig <= 8:
                roman.append(greater_5 + (less_5 * (dig - 5)))
            elif dig == 9:
                next_roman = places[place+1][0]
                roman.append(less_5 + next_roman)
        
        return "".join(roman)
                
            
            
            
        