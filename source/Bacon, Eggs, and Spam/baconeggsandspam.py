def printDictionary(dictTarget):
    for key in sorted(dictTarget):
        print(key, end=' ')
        dictTarget[key] = sorted(dictTarget[key])
        for value in dictTarget[key]:
            print(value, end=' ')
        print('')
    print('')

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0: break 
        else:
            data = {}
            for i in range(n):
                tmp = input().split()
                for j in range(1,len(tmp)):
                    if tmp[j] in data:
                        data[tmp[j]].append(tmp[0])
                    else:
                        data[tmp[j]] = [tmp[0]]
            printDictionary(data)