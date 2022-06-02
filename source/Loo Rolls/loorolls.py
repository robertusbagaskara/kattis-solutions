l, n = map(int, input().split())
counter = 1
while l%n != 0:
    counter += 1
    n -= l%n 
print(counter)