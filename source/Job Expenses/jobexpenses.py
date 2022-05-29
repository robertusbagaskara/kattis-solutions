n = int(input())
sum = 0
numbers = list(input().split())
for i in range(n):
    numbers[i] = int(numbers[i])
    if(numbers[i]<0):
        sum += abs(numbers[i])
print(sum)