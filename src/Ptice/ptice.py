import builtins
import math

def nameManipulation(n,name):
    if len(name) < n:
        name = name * (math.ceil(n/len(name))+1)
    return name

adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

n = int(input())
answers = input()
if len(adrian) < n:
    adrian = nameManipulation(n,adrian)
if len(bruno) < n:
    bruno = nameManipulation(n,bruno)
if len(goran) < n:
    goran = nameManipulation(n,goran)
adrian = adrian[0:n]
bruno = bruno[0:n]
goran = goran[0:n]

totalAdrian = totalBruno = totalGoran = 0
for i in range(n):
    if adrian[i] == answers[i]:
        totalAdrian += 1
    if bruno[i] == answers[i]:
        totalBruno += 1
    if goran[i] == answers[i]:
        totalGoran += 1
largest = max(totalAdrian, totalBruno, totalGoran)
print(largest)
if totalAdrian == largest: print('Adrian')
if totalBruno == largest: print('Bruno')
if totalGoran == largest: print('Goran')