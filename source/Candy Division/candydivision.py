import math
n = int(input())
friends = []
friendsFix = []
for i in range(int(n**0.5)):
    if(n%(i+1) == 0):
        friends.append(i)
        friends.append(int(n/(i+1)-1))
friends.sort()
for i in friends:
    if str(i) not in friendsFix:
        friendsFix.append(str(i))
print(' '.join(friendsFix))