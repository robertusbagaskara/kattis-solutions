n = int(input())
t = input()
list_t = list(t.split())
num_list = []
for i in list_t:
    num_list.append(int(i)+1)
num_list.sort(reverse=True)
day = 0
for i in range(n):
    if num_list[i] + i > day:
        day = num_list[i] + i
print(day + 1)