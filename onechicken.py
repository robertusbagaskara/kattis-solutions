n, m = map(int, input().split())
num = m-n 
s = 'pieces'
if(abs(num)==1 or num==0):
    s = 'piece'
if(num>0 or s==0):
    print('Dr. Chaz will have %i %s of chicken left over!' % (num, s))
else:
    print('Dr. Chaz needs %i more %s of chicken!' % (abs(num), s))