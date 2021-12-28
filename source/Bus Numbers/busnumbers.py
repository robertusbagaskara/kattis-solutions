def targetFormat(listBus):
    for i in range(len(listBus)-1):
        if listBus[i]=='-':
            print('',end='')
        elif listBus[i]!='-' and listBus[i+1]=='-' and i!=len(listBus)-1:
            print(listBus[i],end='-')
        else:
            print(listBus[i],end=' ')
    print(listBus[len(listBus)-1])

if __name__ == '__main__':
    N = int(input())
    listBus = list(map(int, input().split()))
    listBus.sort()
    tmp = []
    for i in range(N-1):
        if i == 0:
            tmp.append(listBus[i])
        elif listBus[i]-listBus[i-1]==1 and listBus[i+1]-listBus[i]==1:
            tmp.append('-')
        else:
            tmp.append(listBus[i])
    tmp.append(listBus[N-1])
    targetFormat(tmp)