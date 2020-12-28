n = int(input())
answer = []
sum = 0
for i in range(n):
    char = input()
    answer.append(char)
for i in range(n-1):
    if(answer[i]==answer[i+1]):
        sum += 1
print(sum)