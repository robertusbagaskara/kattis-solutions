tmp = []
problems = []
counter = 0
result = 0
while True:
    lines = input()
    if lines == '-1': break 
    else: tmp.append(lines.split())
for line in tmp:
    if line[2] == "right":
        counter += 1 
        problems.append(line[1])
for line in tmp:
    if line[1] in problems and line[2]=="right":
        result += int(line[0])
    elif line[1] in problems and line[2]=="wrong":
        result += 20
print("{} {}".format(counter, result))
