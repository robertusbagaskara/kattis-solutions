looping = int(input())
for i in range(looping):
    word = input()
    simonSays = word.split()
    if((simonSays[0]=='Simon')and(simonSays[1]=='says')):
        result = simonSays[2:len(simonSays)]
        print(' '.join(result))
    else:
        pass