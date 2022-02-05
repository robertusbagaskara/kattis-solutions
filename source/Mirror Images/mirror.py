T = int(input())
for i in range(T):
    R, C = map(int, input().split())
    characters = []
    for j in range(R):
        char = input()
        characters.append(char)
    print('Test %i' % (i+1))
    for j in reversed(range(R)):
        print(characters[j][::-1])