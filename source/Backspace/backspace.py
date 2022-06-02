bjarki = input()
result = []
for i in bjarki:
    if i=='<':
        result.pop()
    else:
        result.append(i)
print(''.join(result))