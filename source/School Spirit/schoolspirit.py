def calculateGroupScore(scores):
    total = 0
    for i in range(len(scores)):
        total += scores[i]*((4/5)**i)
    return 1/5*total    

if __name__ == "__main__":
    n = int(input())
    scores = []
    for i in range(n):
        score = int(input())
        scores.append(score)
    scores.sort(reverse=True)
    print(calculateGroupScore(scores))
    newGroupScore = 0
    for i in range(n):
        small = scores.copy()
        del small[i]
        newGroupScore += calculateGroupScore(small)
    print(newGroupScore/n)
