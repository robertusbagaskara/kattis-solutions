n = int(input())
x = input()
list_x = list(x.split())
result = 1
for i in range(1, len(list_x)):
    if int(list_x[i]) > int(list_x[i-1]):
        result += 1
print(result)