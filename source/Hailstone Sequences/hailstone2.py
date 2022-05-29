n = int(input())
counter = 1
while n != 1:
    if n%2 == 0:
        n /= 2
        counter += 1
    else:
        n = 3*n+1
        counter += 1
print(counter)