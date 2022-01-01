def printFormat(dictData, n):
    print("List {}:".format(n))
    for key in sorted(dictData.keys()):
        print("{} | {}".format(key, dictData[key]))

counter = 0
while True:
    counter += 1
    n = int(input())
    animals = {}
    if n == 0: break 
    for _ in range(n):
        tmp = input().split()
        if tmp[-1].lower() not in animals.keys():
            animals.update({tmp[-1].lower():1})
        else:
            animals[tmp[-1].lower()] += 1 
    printFormat(animals, counter)