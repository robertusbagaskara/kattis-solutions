g, s, c = map(int, input().split())
victoryCards = {
    "Province":[8, 6],
    "Duchy":[5, 3],
    "Estate":[2, 1]
}
treasureCards = {
    "Gold":[6, 3],
    "Silver":[3, 2],
    "Copper":[0, 1]
}
cards = []
buyingPower = treasureCards["Gold"][1]*g + treasureCards["Silver"][1]*s + treasureCards["Copper"][1]*c 
for card in victoryCards.keys():
    if victoryCards[card][0] <= buyingPower:
        cards.append(card)
        break
for card in treasureCards.keys():
    if treasureCards[card][0] <= buyingPower:
        cards.append(card)
        break
if len(cards)==2:
    print(f"{cards[0]} or {cards[1]}")
else:
    print(cards[0]) 