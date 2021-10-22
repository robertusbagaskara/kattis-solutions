L = int(input())
D = int(input())
X = int(input())
candidate = []
for i in range(L,D+1):
    stringNum = str(i)
    num = []
    for j in range(len(stringNum)):
        num.append(int(stringNum[j]))
    if(sum(num)==X):
        candidate.append(i)
print(candidate[0])
print(candidate[len(candidate)-1])