n = int(input())
players = []
check = []
for i in range(n):
    name = input()
    players.append(name)
    check.append(name)
players.sort()
if(players==check):
    print('INCREASING')
else:
    players.sort(reverse=True)
    if(players==check):
        print('DECREASING')
    else:
        print('NEITHER')