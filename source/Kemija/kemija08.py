if __name__ == '__main__':
    forbid = ["pa", "pe", "pi", "po", "pu"]
    forbid2 = ["papa", "pepe", "pipi", "popo", "pupu"]
    originalWord = input()
    tmp = originalWord
    for word in forbid2:
        tmp = tmp.replace(word, '####')
    for word in forbid:
        tmp = tmp.replace(word, '--')
    tmp, originalWord = list(tmp), list(originalWord)
    for i in range(len(tmp)):
        if tmp[i]!='-':
            tmp[i] = originalWord[i]
        else:
            tmp[i] = ''
    tmp = ''.join(tmp)
    for i in range(len(forbid2)):
        tmp = tmp.replace(forbid2[i], forbid[i])
    print(tmp)
