n = int(input())
words = input()
counting = words.split(' ')
conclusion = 'makes sense'
for i in range(n):
    if counting[i] == str(i+1) or counting[i] == 'mumble':
        continue
    else:
        conclusion = 'something is fishy'
        break
print(conclusion)