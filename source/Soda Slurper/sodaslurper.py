a, b, c = map(int, input().split())
tmp = 0
drink = 0
bottle = a + b
while bottle >= c :
    drink = int(bottle / c)
    tmp += drink
    mod = bottle % c
    bottle = drink + mod
print(tmp)