sentence = input()
words = sentence.split('-')
for word in words:
    print(word[0].upper(), end='')