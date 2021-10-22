l, x = map(int, input().split())
total = 0
tryToEnter = 0
enter = 0
for i in range(x):
    act, num = map(str, input().split())
    if act == 'enter' : tryToEnter += 1
    if act == 'enter' and total + int(num) <= l:
        total += int(num)
        enter += 1
    elif act == 'leave':
        total -= int(num)
print(tryToEnter - enter)