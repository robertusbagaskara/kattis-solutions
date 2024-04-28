n = int(input())
forgetedItems = ["keys", "phone", "wallet"]
for i in range(n):
    grabbedItem = input()
    for item in forgetedItems:
        if grabbedItem == item:
            forgetedItems.remove(grabbedItem)

if len(forgetedItems) == 0:
    print("ready")
else:
    forgetedItems.sort()
    for item in forgetedItems:
        print(item)
    