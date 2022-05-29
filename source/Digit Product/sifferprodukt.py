x = input()
while True:
    tmp = 1
    for i in x:
        if i!='0':tmp *= int(i) 
    x = str(tmp)
    if int(x)>=1 and int(x)<=9:
        print(x)  
        break
