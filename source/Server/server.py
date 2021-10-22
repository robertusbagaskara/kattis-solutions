N, T = map(int, input().split())
n = input().split()
sum = 0
count = 0
for i in range(N):
    if (sum + int(n[i]) <= T):
        sum += int(n[i])
        count += 1
    else:
        break
print(count)