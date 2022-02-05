x = []
y = []
xNum = 0
yNum = 0
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for j in range(3):
    countX = x.count(x[j])
    countY = y.count(y[j])
    if(countX==1):
        xNum = x[j]
    if(countY==1):
        yNum = y[j]
print('%i %i' % (xNum,yNum))