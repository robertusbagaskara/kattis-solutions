s = input()
out = 1
for i in s:
    if s.count(i) > 1:
        out = 0
        break
print(out) 