import string
import sys 

def num_to_word(string_number):
    units = (None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine") 
    teens = (None, "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
    tens = (None, "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    if string_number == '0':
        return "zero"
    elif len(string_number) == 1:
        return units[int(string_number)]
    elif string_number[0] == '1' and string_number[1] != '0':
        return teens[int(string_number[1])]
    else:
        if string_number[1] == '0':
            return tens[int(string_number[0])]
        else:
            return tens[int(string_number[0])]+'-'+units[int(string_number[1])]

for line in sys.stdin:
    temp = line.split()
    for word in temp:
        if word.isnumeric() == True:
            final_word = num_to_word(word)
        else:
            final_word = word
        if word == temp[0]:
            print(final_word.capitalize(), end=' ')
        else:
            print(final_word, end=' ')