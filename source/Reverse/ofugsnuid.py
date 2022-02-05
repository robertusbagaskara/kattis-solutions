looping = int(input())
points = []
for i in range(looping):
    num = int(input())
    points.append(num)
for j in reversed(range(looping)):
    print(points[j])