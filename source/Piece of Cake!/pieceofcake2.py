n, h, v = map(int, input().split())
hNew = n - h
vNew = n - v
if(h<=(n/2)):
    h = hNew
if(v<=(n/2)):
    v = vNew
print(4*h*v)