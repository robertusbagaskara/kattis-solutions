T = int(input())

for i in range(T):
    space = input()
    N = int(input())
    sum = 0
    for i in range(N):
        candy = int(input())
        sum += candy
    status = 'YES' if (sum%N==0) else 'NO'
    print(status)