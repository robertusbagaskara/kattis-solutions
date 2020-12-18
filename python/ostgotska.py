word = input()
target = 0
listWord = word.split(' ')
for i in range(len(listWord)):
    if('ae' in listWord[i]):
        target += 1
if(target/len(listWord)>=40/100):
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')