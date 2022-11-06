n = int(input())
cups = {}

for i in range(n):
    token1, token2 = input().split()
    if token1.isnumeric():
        cups[int(int(token1)/2)] = token2 
    else:
        cups[int(token2)] = token1 

cups = sorted(cups.items())

for cup in cups:
    print(cup[1])
