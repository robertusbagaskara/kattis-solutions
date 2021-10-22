card = input()
points = 0
cardList = ['T', 'G', 'C']
cardCount = []
for i in range(len(cardList)):
    cardCount.append(int(card.count(cardList[i])))
    if(cardCount[i] != 0): points += cardCount[i] ** 2
cardCount.sort()
points += cardCount[0]*7
print(points)