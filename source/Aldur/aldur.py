n = int(input())

youngest = None

for i in range(1, n+1):
    temp = int(input())
    if i == 1:
        youngest = temp 
    if youngest > temp:
        youngest = temp 

print(youngest)