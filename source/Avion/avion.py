num = []
for i in range(5):
    blimps = input()
    if('FBI' in blimps):
        num.append(i+1)
if(len(num)==0):
    print('HE GOT AWAY!')
else:
    for i in range(len(num)):
        print('%i ' % num[i], end = '')