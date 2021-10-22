n = int(input())
sum = 0
for i in range(n):
    color = input().lower()
    if 'pink' in color or 'rose' in color: sum += 1
if(sum==0):
    print('I must watch Star Wars with my daughter')
else:
    print(sum)