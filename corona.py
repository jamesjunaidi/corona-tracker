from sys import stdin

class date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def printDate(self):
        print("Date: " + str(self.month) + "/" + str(self.day))

def main():
    dates = [date(2,24), date(2,25), date(2,26), date(2,27), date(2,28), date(2,29)]

    for x in range(1, 25):
        dates.append(date(3,x))
    
    caseNums = []
    for line in stdin:
        caseNums.append(int(line))
    
    increases = []
    for x in range(len(caseNums)):
        dates[x].printDate()
        print("count: "  + str(caseNums[x]))
        if x != 0:
            print("Increase by: " + str((caseNums[x] - caseNums[x-1])) + " from the previous date")
            increases.append(caseNums[x] - caseNums[x-1])

    for x in range(len(increases)):
        print("Numbers increased by: " + str(increases[x]) + " on: ")
        dates[x + 1].printDate()
        if x != 0:
            print("Rate of increasing increasingness is: " + str(increases[x] - increases[x-1]))

main()
