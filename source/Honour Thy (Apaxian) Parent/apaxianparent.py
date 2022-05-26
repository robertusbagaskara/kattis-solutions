vowel = ['a','i','o','u']
y, p = input().split()
if y[-1] == 'e':
    print(y+'x'+p)
elif y[-1] in vowel: 
    print(y[:-1]+'ex'+p)
elif y[-2:] == "ex":
    print(y+p)
else:
    print(y+"ex"+p)