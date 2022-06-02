n = int(input())
won = 0
for i in range(n):
    abilities = input()
    if 'CD' not in abilities:
        won+=1
print(won)