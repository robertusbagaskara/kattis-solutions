n, m = map(int, input().split())
if(n > m):
    tmp = n 
    n = m 
    m = tmp 

for i in range(n+1, m+2):
    print(i)