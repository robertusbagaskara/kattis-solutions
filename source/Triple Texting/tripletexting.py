s = input()
group = int(len(s)/3)
real = []
for i in range(0, int(len(s)), group):
    real.append(s[i:i+group])
if (real.count(real[0]) == 2):
    print(real[0])
else:
    print(real[1])