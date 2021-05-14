n = int(input())
t = []
for i in range(n):
    num = int(input())
    t.append(num)
if n%2 == 1: print('still running')
else:
    even = 0
    odd = 0
    for i in range(len(t)):
        if i % 2 == 0:
            even += t[i]
        else:
            odd += t[i]
    print(odd - even)
