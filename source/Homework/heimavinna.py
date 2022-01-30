numbers = input()
total = 0
if(';' in numbers):
    number = numbers.split(';')
    for i in number:
        if('-' in i):
            num = i.split('-')
            for j in range(int(num[0]), int(num[1])+1):
                total += 1
        else:
            total += 1
elif('-' in numbers):
    number = numbers.split('-')
    for i in range(int(number[0]), int(number[1])+1):
        total += 1
else:
    total += 1

print(total)