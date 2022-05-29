loop = int(input())
for i in range(loop):
    a, b, c = map(int, input().split())
    num = [a, b, c]
    num.sort()
    if(num[0]+num[1]==num[2] or num[0]*num[1]==num[2]):
        print('Possible')
    else:
        print('Impossible')