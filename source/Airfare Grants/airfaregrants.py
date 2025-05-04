n = int(input())
minimum_ticket = 100000
maximum_ticket = 0

for ticket in range(n):
    ticket_price = int(input())
    if minimum_ticket > ticket_price:
        minimum_ticket = ticket_price
    if maximum_ticket < ticket_price:
        maximum_ticket = ticket_price

pay_by_me = minimum_ticket - int((maximum_ticket)/2)

if pay_by_me < 0:
    print(0)
else:
    print(pay_by_me)