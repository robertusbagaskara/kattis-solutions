a, b, c, d = map(int, input().split())
expressions = ['*', '+', '-', '//']
flag = False
for operator1 in expressions:
    for operator2 in expressions:
        if (b==0 or d==0) and (operator1=="//" or operator2=="//"):
            continue
        result1 = eval("{} {} {}".format(a, operator1, b))
        result2 = eval("{} {} {}".format(c, operator2, d))
        if result1 == result2:
            flag = True
            print(("{} {} {} = {} {} {}".format(a, operator1, b, c, operator2, d)).replace("//", "/"))
if not flag:
    print("problems ahead") 