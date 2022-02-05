k = int(input())
friends = {}
rememberedFriends = []
for _ in range(k):
    friendData = input().split()
    if friendData[2] not in friends.keys():
        friends[friendData[2]] = {}
    friends[friendData[2]][int(friendData[1])] = friendData[0]
for friend in friends:
    target = max(friends[friend].keys())
    rememberedFriends.append((friends[friend][target]))
print(len(rememberedFriends))
for friend in sorted(rememberedFriends): print(friend)