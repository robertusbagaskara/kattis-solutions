looping = int(input())
a = []
b = []
missingNumber = []
for i in range(looping):
    number = int(input())
    a.append(number)
for i in range(a[looping-1]):
    b.append(i+1)
    if(b[i] not in a):
        missingNumber.append(b[i])

if(missingNumber == []):
    print('good job')
else:
    for i in range(len(missingNumber)):
        print(missingNumber[i])