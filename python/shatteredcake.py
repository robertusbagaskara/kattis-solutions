W = int(input())
N = int(input())
area = 0
for i in range(N):
    w, l = map(int, input().split())
    area += w*l 
L = int(area/W)
print(L)