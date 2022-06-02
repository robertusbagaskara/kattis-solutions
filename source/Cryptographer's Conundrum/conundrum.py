cipher = input()
name = 'PER'
day = 0
for i in range(len(cipher)):
    if cipher[i] != name[i%3]:
        day += 1
print(day)