n, m = map(int, input().split())
items = input()
itemsList = items.split(' ')
countList = [1] * m
for i in range(n-1):
    newItems = input()
    newItemList = newItems.split(' ')
    for j in range(m):
        if itemsList[j] in newItemList:
            countList[j] += 1
printedList = []
for i in range(len(countList)):
    if countList[i] == n:
        printedList.append(itemsList[i])
print(len(printedList))
printedList.sort()
for i in printedList:
    print(i)
