loop = int(input())
for i in range(loop):
    sum = 0
    a, b = map(int, input().split())
    for j in range(1, b+1):
        sum += j
    print('%i %i' % (a,sum+b))