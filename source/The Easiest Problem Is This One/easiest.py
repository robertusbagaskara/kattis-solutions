def sumDigit(strNum):
    sum = 0
    for digit in strNum:
        sum += int(digit)
    return sum

if __name__ == '__main__':
    while(True):
        N = input()
        if int(N) == 0:
            break
        sumP = sumDigit(N)
        for i in range(11, 100000):
            if sumDigit(str(i*int(N))) == sumP:
                print(i)
                break