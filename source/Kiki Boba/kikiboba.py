word = input()
counterB = 0
counterK = 0

for character in word:
    if character == "b":
        counterB += 1
    elif character == "k":
        counterK += 1

if counterB > counterK:
    print("boba")
elif counterK > counterB:
    print("kiki")
elif counterK == 0 and counterB == 0:
    print("none")
elif counterB == counterK:
    print("boki")