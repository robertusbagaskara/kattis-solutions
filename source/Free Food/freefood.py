looping = int(input())
numbers = []
for i in range(looping):
    a, b = map(int, input().split())
    for j in range(a,b+1):
        numbers.append(j)
print(len(set(numbers)))