import math
r, c = map(int, input().split())
totalArea = math.pi*(r**2)
cheeseArea = math.pi*((r-c)**2)
print(cheeseArea/totalArea*100)