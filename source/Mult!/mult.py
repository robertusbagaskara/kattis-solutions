n = int(input())
flag = False 
multipler = None
for i in range(n):
    tmp = int(input())
    if flag == False:
        multipler = tmp 
        flag = True
    else:
        if tmp%multipler==0:
            print(tmp)
            flag = False 