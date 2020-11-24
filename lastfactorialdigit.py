loop = int(input())
for i in range(loop):
    result = 1
    number = int(input())
    for j in range(1, number+1):
        result *= j
        stringResult = str(result)
    print(stringResult[len(stringResult)-1])
