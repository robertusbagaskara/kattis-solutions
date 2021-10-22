flag = False
while flag == False:
    x, y = map(int, input().split())
    if (x==0 and y==0):
        flag = True
    elif (x == y):
        print('Undecided.')
    elif (x + y == 13):
        print('Never speak again.')
    elif (x < y):
        print('Left beehind.')
    elif (x > y):
        print('To the convention.')