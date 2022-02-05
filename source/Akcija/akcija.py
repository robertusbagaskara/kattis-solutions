n = int(input())
list_price = []
total = 0
for i in range(n):
    price = int(input())
    list_price.append(price)
list_price.sort(reverse=True)
for i in range(1, len(list_price)+1):
    if i % 3 != 0:
        total += list_price[i-1]
print(total)