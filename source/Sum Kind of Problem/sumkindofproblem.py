def positiveSum(n):
    sum = 0
    for i in range(0,n+1):
        sum += i
    return sum

def oddSum(n):
    sum = 0
    for i in range(1,n*2,2):
        sum += i
    return sum

def evenSum(n):
    sum = 0
    for i in range(0,n*2+1,2):
        sum += i
    return sum

p = int(input())
for i in range(p):
    k, n = map(int, input().split())
    pos = positiveSum(n)
    odd = oddSum(n)
    even = evenSum(n)
    print("%i %i %i %i" % (k, pos, odd, even))
