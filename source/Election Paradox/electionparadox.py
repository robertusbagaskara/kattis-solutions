N = int(input())
populations = list(map(int, input().split()))
populations.sort()
countForWin = int(N/2)+1
sumSmaller = 0
for i in range(0, countForWin):
    sumSmaller += int(populations[i]/2)
sumGreater = 0
for i in range(countForWin, N):
    sumGreater += populations[i]
print(sumSmaller+sumGreater)