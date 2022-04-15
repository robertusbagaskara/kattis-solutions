cards = input().split()
strength = {}
for card in cards:
    if card[0] not in strength.keys():
        strength[card[0]] = 1
    else:
        strength[card[0]] += 1
print(max(strength.values()))