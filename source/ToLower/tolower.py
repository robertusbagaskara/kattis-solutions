p, t = map(int, input().split())
upperString = 'ABCDEFGHIJLLMNOPQRSTUVWXYZ'
total = 0
for i in range(p):
    num = t
    tmp = 0
    for j in range(t):
        test_case = input()
        check = test_case[1:]
        for char in check:
            if char in upperString:
                tmp += 1
        num -= tmp
    if num == t:
        total += 1
print(total)
