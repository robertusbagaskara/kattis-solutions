input1, input2 = map(str, input().split())
input1Rev = list(reversed(input1))
input2Rev = list(reversed(input2))
num1 = int("".join(input1Rev))
num2 = int("".join(input2Rev))
if(num1>num2):
    print(num1)
else:
    print(num2)
