num = int(input())
ans = 0
binNum = bin(num).replace('0b','')
binNum = str(binNum)
for i in reversed(range(len(binNum))):
    temp = int(binNum[i])*(2**i)
    ans += temp
print(ans)