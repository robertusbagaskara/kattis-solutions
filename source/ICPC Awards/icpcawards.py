n = int(input())
winnersCount = 0
winners = {}

for i in range(n):
    universities, team = map(str, input().split())
    if universities not in winners.keys() and winnersCount < 12:
        winners[universities] = team
        winnersCount += 1

for i in winners:
    print(i, winners[i])