astrologicalDictionary = {
    "Aries": ["Mar", 21],
    "Taurus": ["Apr", 21],
    "Gemini":["May", 21],
    "Cancer": ["Jun", 22],
    "Leo": ["Jul", 23],
    "Virgo": ["Aug", 23],
    "Libra": ["Sep", 22],
    "Scorpio": ["Oct", 23],
    "Sagittarius": ["Nov", 23],
    "Capricorn": ["Dec", 22],
    "Aquarius": ["Jan", 21],
    "Pisces": ["Feb", 20]
}

listAstrologicalSign = []

t = int(input())

for i in range(t):
    day, month = input().split()
    for astrologicalSign in astrologicalDictionary.keys():
        listAstrologicalSign.append(astrologicalSign)
    targetIndexAstrologicalSign = 0
    for j in range(len(listAstrologicalSign)):
        if month == astrologicalDictionary[listAstrologicalSign[j]][0]:
            if int(day) < astrologicalDictionary[listAstrologicalSign[j]][1]:
                targetIndexAstrologicalSign = j-1
            elif int(day) >= astrologicalDictionary[listAstrologicalSign[j]][1]:
                targetIndexAstrologicalSign = j 
    print(listAstrologicalSign[targetIndexAstrologicalSign])    