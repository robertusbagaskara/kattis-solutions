a, b, c = map(int, input().split())
num = []
num.append(a)
num.append(b)
num.append(c)
num.sort(reverse=False)
sequence = input()

dictNum = {'A':num[0], 'B':num[1], 'C':num[2]}
print('%i %i %i' % (dictNum[sequence[0]], dictNum[sequence[1]], dictNum[sequence[2]]))