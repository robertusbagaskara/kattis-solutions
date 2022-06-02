n = int(input())
for i in range(n):
    num = input()
    numbers = num.split()
    sum = 0
    for j in range(1, len(numbers)):
        sum += int(numbers[j])
    print(sum + 1 - int(numbers[0]))