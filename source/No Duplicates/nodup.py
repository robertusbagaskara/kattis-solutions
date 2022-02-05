word = input().split()
wordSet = set(word)
if(len(word)==len(list(wordSet))):
    print('yes')
else:
    print('no')