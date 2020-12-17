looping = int(input())
firstPrint = []
secondPrint = []
result = []
for i in range(looping):
    differences = []
    firstWord = input()
    firstPrint.append(firstWord)
    secondWord = input()
    secondPrint.append(secondWord)
    for j in range(len(firstWord)):
        if firstWord[j] == secondWord[j]:
            differences.append('.')
        elif firstWord[j] != secondWord[j]:
            differences.append('*')
    result.append(''.join(differences))

for i in range(looping):
    print(firstPrint[i])
    print(secondPrint[i])
    print(''.join(result[i]))
    print('')