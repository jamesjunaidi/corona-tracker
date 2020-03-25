from sys import stdin

#this is the date class, allows for easy storage of dates
class date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def printDate(self):
        print("Date: " + str(self.month) + "/" + str(self.day))


#the main class
def main():
    #hard coded the dates in Feb.
    dates = [date(2,24), date(2,25), date(2,26), date(2,27), date(2,28), date(2,29)]
    #hard coded with a loop for dates in Mar. 
    for x in range(1, 25):
        dates.append(date(3,x))

    #initialize array of case numbers
    caseNums = []

    #this allows us to take the case numbers from standard input
    for line in stdin:
        caseNums.append(int(line))

    #initialize array of the increases
    increases = []

    #prints the daily increases
    for x in range(len(caseNums)):
        dates[x].printDate()
        print("count: "  + str(caseNums[x]))
        if x != 0:
            print("Increase by: " + str((caseNums[x] - caseNums[x-1])) + " from the previous date")
            increases.append(caseNums[x] - caseNums[x-1])

    #prints how much they increased by initialialy
    for x in range(len(increases)):
        print("Numbers increased by: " + str(increases[x]) + " on: ")
        dates[x + 1].printDate()
        if x != 0:
            print("Rate of increasing increasingness is: " + str(increases[x] - increases[x-1]))

main()
