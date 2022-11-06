def searchGreatest(a, b):
    if a == b:
        return a 
    elif a > b:
        return a 
    elif a < b:
        return b

def calculate(forecasts):
    smallestTemp = 40
    smallestDay = 0
    for i in range(len(forecasts)-2):
        greatest = searchGreatest(forecasts[i], forecasts[i+2])
        if greatest < smallestTemp:
            smallestTemp = greatest
            smallestDay = i
    return smallestDay+1, smallestTemp

if __name__ == "__main__":
    _ = int(input())
    forecasts = [int(i) for i in input().split()]
    day, temp = calculate(forecasts=forecasts)
    print(day, temp)