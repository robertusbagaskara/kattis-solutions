looping = int(input())
resultSet = 0
for i in range(looping):
    num = input()
    num1 = num[0:len(num)-1]
    pow = num[len(num)-1]
    number = int(num1)
    power = int(pow)
    result = number**power
    resultSet = resultSet + result
print(resultSet)