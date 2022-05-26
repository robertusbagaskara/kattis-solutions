n, k = map(int, input().split())
colours = input().split()
dictColours = {}
tmp = 1000
for i in range(1, k+1):
    if str(i) not in colours:
        tmp = 0
        dictColours[str(i)] = 0
    elif str(i) not in dictColours.keys() and str(i) in colours:
        dictColours[str(i)] = colours.count(str(i))
        if tmp > dictColours[str(i)]:
            tmp = dictColours[str(i)]
counter = 0
numbers = []
for key in dictColours.keys():
    if tmp == 0:
        if dictColours[key] == 0:
            counter += 1
            numbers.append((int(key)))
    elif dictColours[key] == tmp:
        counter += 1
        numbers.append(int(key))
print(counter)
for num in numbers: print(num, end=" ")