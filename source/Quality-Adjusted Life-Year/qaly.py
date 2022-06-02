looping = int(input())
qaly = 0
for i in range(looping):
    q, y = map(float, input().split())
    sum = q*y
    qaly += sum
print('{:.3f}'.format(qaly))