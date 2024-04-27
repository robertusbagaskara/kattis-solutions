def calculateAddedMinutes(firstTimeZone, secondTimeZone):
    timeZonesDict = {
        "UTC": 0,
        "GMT": 0,
        "BST": 1,
        "IST": 1,
        "WET": 0,
        "WEST": 1,
        "CET": 1,
        "CEST": 2,
        "EET": 2,
        "EEST": 3,
        "MSK": 3,
        "MSD": 4,
        "AST": -4,
        "ADT": -3,
        "NST": -3.5,
        "NDT": -2.5,
        "EST": -5,
        "EDT": -4,
        "CST": -6,
        "CDT": -5,
        "MST": -7,
        "MDT": -6,
        "PST": -8,
        "PDT": -7,
        "HST": -10,
        "AKST": -9,
        "AKDT": -8,
        "AEST": 10,
        "AEDT": 11,
        "ACST": 9.5,
        "ACDT": 10.5,
        "AWST": 8
    }

    addedHour = 0
    addedHour -= timeZonesDict[firstTimeZone]
    addedHour += timeZonesDict[secondTimeZone]
    return addedHour * 60

def calculateTime(clockTime, minutesAdd):
    hours, minutes = map(int, clockTime[:-4].split(":"))
    hours %= 12
    if clockTime[-4:] == "p.m.":
        hours += 12
    timesFinal = hours * 60 + minutes + minutesAdd
    hours, minutes = divmod(timesFinal, 60)
    hours %= 24
    suffix = "a"
    if hours >= 12:
        suffix = "p"
    hours %= 12
    if hours == 0:
        hours = 12
    return "{:01d}:{:02d} {}.m.".format(int(hours), int(minutes), suffix)

def main():
    n = int(input())
    resultOutput = []
    for i in range(n):
        userInput = input().split()
        clockTime = ""
        firstTimeZone = userInput[-2]
        secondTimeZone = userInput[-1]
        timeSource = userInput[0]
        if timeSource == "noon":
            clockTime = "12:00"
            secondPeriod = "p.m."
        elif timeSource == "midnight":
            clockTime = "12:00"
            secondPeriod = "a.m."
        else:
            clockTime = userInput[0]
            secondPeriod = userInput[1]
        addedMinutes = calculateAddedMinutes(firstTimeZone=firstTimeZone, secondTimeZone=secondTimeZone)
        finalTime = calculateTime(str(clockTime)+str(secondPeriod), addedMinutes)

        if finalTime == "12:00 a.m.":
            finalTime = "midnight"
        elif finalTime == "12:00 p.m.":
            finalTime = "noon"
        
        resultOutput.append(finalTime)
        
    
    for i in range(n):
        print(resultOutput[i])

if __name__ == "__main__":
    main()