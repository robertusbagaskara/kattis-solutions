loop = int(input())
for i in range(loop):
    num = int(input())
    if(num%2 == 0):
        print('%i is even' % (num))
    else:
        print('%i is odd' % (num))