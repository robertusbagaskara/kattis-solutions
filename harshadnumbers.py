inputUser = input()
for i in range(int(inputUser),1000000000+1):
    inputUser = str(i)
    result = inputUser
    number = int(inputUser)
    stringNum = []
    sum = 0
    for j in range(len(inputUser)):
        num = int(inputUser[j])
        sum += num
    if i%sum == 0:
        break
print(i)