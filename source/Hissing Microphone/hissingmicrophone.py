word = input()
flag = 'no hiss'
i = 0
for i in range(len(word)-1):
    if((word[i]=='s') and (word[i+1]=='s')):
        flag = 'hiss'
print(flag)
