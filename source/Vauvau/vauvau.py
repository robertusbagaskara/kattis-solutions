def dog(x, y, n, num):
    if num==1:
        counter = n
        tmp = 0
        flag = True
        while flag:
            tmp += counter
            if(x >= tmp):
                flag = False
                return 1
            elif(x+y >= tmp):
                flag = False
                return 0
    else:
        counter = x
        tmp = 0
        flag = True
        while flag:
            tmp += counter
            if(tmp >= n):
                flag = False
                return 1
            elif(tmp+y >= n):
                flag = False
                return 0
            tmp += y
            
    
def calculate(a, b, c, d, n):
    if a>n:
        num = 1
    else:
        num = 0
    ans1 = dog(a, b, n, num)
    ans2 = dog(c, d, n, num)
    if(ans1==1 and ans2==1):
        print('both')
    elif(ans1==0 and ans2==0):
        print('none')
    elif(ans1==0 or ans2==0):
        print('one')
    

a, b, c, d = map(int, input().split())
worker = input()
workers = worker.split()
for i in workers:
    calculate(a, b, c, d, int(i))