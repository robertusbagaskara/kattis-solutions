n = int(input())
for i in range(n):
    num = 0
    g = int(input())
    numbers = list(input().split())
    for j in range(g):
        if(numbers.count(numbers[j])==1):
            num = numbers[j]
    print('Case #%i: %s' % (i+1, num))