looping = int(input())
num = map(int, input().split())
sum = 0
length = 0
for i in num:
    if(i>=0):
        sum += i
        length += 1
print(sum/length)