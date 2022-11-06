keypad = {
    0: [' '],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']
}

def searchTheKey(character):
    for key in keypad:
        if character.upper() in keypad[key]:
            return str(key), keypad[key].index(character.upper())+1

def translate(message):
    translated = ""
    for character in message:
        key, position = searchTheKey(character)
        if len(translated) >= 1:
            if key == translated[-1] or (translated[-1] == ' ' and key == translated[-1]):
                translated += " "
        translated += key * position
    return translated

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        case = input()
        print("Case #{}: {}".format(i+1, translate(case)))