wordDict = {
    'a' : '@',
    'b' : '8',
    'c' : '(',
    'd' : '|)',
    'e' : '3',
    'f' : '#',
    'g' : '6',
    'h' : '[-]',
    'i' : '|',
    'j' : '_|',
    'k' : '|<',
    'l' : '1',
    'm' : '[]\/[]',
    'n' : '[]\[]',
    'o' : '0',
    'p' : '|D',
    'q' : '(,)',
    'r' : '|Z',
    's' : '$',
    't' : "']['",
    'u' : '|_|',
    'v' : '\/',
    'w' : '\/\/',
    'x' : '}{',
    'y' : '`/',
    'z' : '2',
}

word = input()
for i in word:
    if(ord(i.lower())>=97 and ord(i.lower())<=122):
        print(wordDict[i.lower()], end='')
    else:
        print(i, end='')