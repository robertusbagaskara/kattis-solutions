word = input()
whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0
for character in word:
    if character == '_':
        whitespace += 1
    elif ord(character) >= 97 and ord(character) <= 122:
        lowercase += 1
    elif ord(character) >=65 and ord(character) <= 90:
        uppercase += 1
    else:
        symbols += 1
length = len(word)
print('%.6f\n%.6f\n%.6f\n%.6f' % ((whitespace/length), (lowercase/length), (uppercase/length), (symbols/length)))