def result(number):
    if number == '':
        return "YODA"
    elif number[0] == '0' and number[-1] == '0':
        return '0'
    else:
        return number

n = input()
m = input()
nTemp = ''
mTemp = ''
if len(n) != len(m):
    if len(n) < len(m):
        n = ('0'*(len(m)-len(n)))+n
    else:
        m = ('0'*(len(n)-len(m)))+m
for i in range(len(n)):
    if n[i] == m[i]:
        nTemp += str(n[i])
        mTemp += str(m[i])
    elif int(n[i]) > int(m[i]):
        nTemp += n[i]
    elif int(n[i]) < int(m[i]):
        mTemp += m[i]
print(result(nTemp))
print(result(mTemp))