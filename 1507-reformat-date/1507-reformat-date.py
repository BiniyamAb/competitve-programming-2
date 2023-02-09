class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", 
                  "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        dates = date.split(" ")
        day = dates[0][0:-2]
        if len(day) == 1: day = "0" + day
        return dates[2] + "-" + months[dates[1]] + "-" + day
        