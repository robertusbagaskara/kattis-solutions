def summation(number):
    number *= 2
    if len(str(number)) == 2:
        return int(str(number)[0]) + int(str(number)[1])
    else:
        return number

def checksum(cardNumber):
    cardNumber = cardNumber[::-1]
    lenNum = len(cardNumber)
    sumNum = 0
    for i in range(1, lenNum+1):
        if i%2 == 0:
            tmp = summation(int(cardNumber[i-1]))
            sumNum += tmp
        else:
            sumNum += int(cardNumber[i-1])
    return sumNum


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        cardNumber = input()
        if checksum(cardNumber)%10 == 0:
            print('PASS')
        else:
            print('FAIL')