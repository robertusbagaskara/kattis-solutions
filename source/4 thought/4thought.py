def checkNumber(target):
    operator = ['+', '-', '*', '//']
    writedOperator = ['', '', '']
    for i in operator:
        writedOperator[0] = i
        for j in operator:
            writedOperator[1] = j
            for k in operator:
                writedOperator[2] = k
                result = eval('4{}4{}4{}4'.format(i,j,k))
                if result == target:
                    return ('4 {} 4 {} 4 {} 4 = {}'.format(i,j,k,target)).replace('//', '/')
                    break
                elif i=='//' and j=='//' and k=='//' and result!=target:
                    return "no solution"
                    break


if __name__ == '__main__':
    m = int(input())
    for i in range(m):
        n = int(input())
        if n > 256 and n < -60:
            print("no solution")
        else:
            print(checkNumber(n))



