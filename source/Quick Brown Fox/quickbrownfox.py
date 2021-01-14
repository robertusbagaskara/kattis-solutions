import string
key = list(string.ascii_lowercase)
n = int(input())
for i in range(n):
    tmp = []
    word = input().replace(' ','')
    for i in range(len(key)):
        if key[i] not in word.lower():
            tmp.append(key[i])
        else:
            continue
    if(len(tmp)==0):
        print('pangram')
    else:
        tmp.sort()
        print('missing',''.join(tmp))