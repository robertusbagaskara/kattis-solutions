t = int(input())
list_result = []
for i in range(t):
    n = int(input())
    candidates = []
    for j in range(n):
        candidate = int(input())
        candidates.append(candidate)
    total_votes = sum(candidates)
    winner = max(candidates)
    candidate_number = 0
    winner_frequent = candidates.count(winner)
    for j in range(len(candidates)):
        if candidates[j] == winner:
            candidate_number = j
            break
    candidates.sort(reverse=True)
    if candidates[0] == candidates[1]:
        list_result.append("no winner")
    elif winner > total_votes/2:
        list_result.append("majority winner {}".format(j+1))
    else:
        list_result.append("minority winner {}".format(j+1))
for i in list_result:
    print(i)

