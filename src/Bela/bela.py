def dominant(s):
    score = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10,
    '9':14, '8':0, '7':0}
    return score[s]

def notDominant(s):
    score = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10,
    '9':0, '8':0, '7':0}
    return score[s]

word = input()
word = word.split()
n = int(word[0])
s = word[1]
points = 0
for i in range(n*4):
    card = input()
    if(card[1]==s):
        points += dominant(card[0])
    else:
        points += notDominant(card[0])
print(points)