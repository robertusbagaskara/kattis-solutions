def searchCorrect(max, errors):
    correct = []
    for num in range(1, max+1):
        if num not in errors:
            correct.append(num)
    return correct

def generateOutput(sequences):
    result = []
    for i in range(len(sequences)-1):
        if i == 0:
            if sequences[i+1]-sequences[i]!=1:
                result.append("{}, ".format(sequences[i]))
            else:
                result.append("{}".format(sequences[i]))
        elif sequences[i]-sequences[i-1]==1 and sequences[i+1]-sequences[i]==1:
            continue 
        elif sequences[i]-sequences[i-1]==1:
            result.append("-{}, ".format(sequences[i]))
        elif sequences[i+1]-sequences[i]==1:
            result.append("{}".format(sequences[i]))
        else:
            result.append("{}, ".format(sequences[i]))
    if sequences[len(sequences)-1]-sequences[len(sequences)-2]==1:
        result.append("-{}".format(sequences[len(sequences)-1]))
    else:
        result.append(str(sequences[len(sequences)-1]))
    return result

def printResult(sequences, detail):
    sequences = generateOutput(sequences)
    print("{}: ".format(detail), end='')
    if '-' in sequences[-1]:
        sequences[-2] = "and " + sequences[-2]
        sequences[-3] = sequences[-3].replace(',','')
    else:
        sequences[-1] = "and " + sequences[-1]
        sequences[-2] = sequences[-2].replace(',','')
    print("".join(sequences))

c, n = map(int, input().split())
errors = [int(x) for x in input().split()]
correct = searchCorrect(c, errors)
printResult(errors, "Errors")
printResult(correct, "Correct")