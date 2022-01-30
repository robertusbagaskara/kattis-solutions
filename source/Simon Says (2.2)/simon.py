t = int(input())
for i in range(t):
    word = input()
    if(word.startswith('simon says')):
        print(' '.join(word.split()[2:]))
    else:
        print('\n')