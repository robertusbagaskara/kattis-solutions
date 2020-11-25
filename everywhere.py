outerLoop = int(input())
for i in range(outerLoop):
    cities = {}
    innerLoop = int(input())
    for j in range(innerLoop):
        cities[input()] = j
    print(len(cities)) 
        