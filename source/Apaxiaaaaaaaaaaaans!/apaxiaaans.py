word = input()
nodup = ''
for i in range(len(word)):
    if i == 0:
        nodup += word[i]
    else:
        if(word[i]!=word[i-1]):
            nodup += word[i]
print(nodup)