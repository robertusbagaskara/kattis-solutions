#
#can -> 6, 6, 6, 6, 6
#    . - - - - -
#      . - - - -
#        . - - -
#          . - -
#            . -

#can't -> 6, 7, 8
#    . . - - - -
#        . . - - -
#            . . - -

#can -> 7, 7, 8
#    . . - - - - -
#        . . - - - 
#            . . - -

n, t = map(int, input().split())
list_poison = []
for i in range(n):
    poison = int(input())
    list_poison.append(poison)
list_poison.sort(reverse=True)

list_poison_mod = list_poison.copy()

flag_over = False
for i in range(0, len(list_poison)):
    #start counting
    list_poison_mod[i] = ((i+1) * t) + list_poison_mod[i]
    if list_poison_mod[i] - list_poison[i] >= list_poison_mod[0] and i!=0:
        flag_over = True
        break

if flag_over:
    print("NO")
else:
    print("YES")
