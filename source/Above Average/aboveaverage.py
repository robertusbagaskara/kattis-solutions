c = int(input())
for i in range(c):
    numbers = input()
    num = numbers.split()
    total = 0
    for j in range(1, len(num)):
        total += int(num[j])
    average = total/int(num[0])
    counter = 0
    for j in range(1, len(num)):
        if(int(num[j]) > average):
            counter += 1
    print('%.3f' % (counter/int(num[0])*100) + '%')