from collections import Counter as C
#num of shoes in stock
X = int(raw_input())
sizes = map(int, raw_input().split())

#enumerate the stock available
stock = C(sizes)

#initialize earnings
money = 0

n_customers = int(raw_input())
#check availability for each customer and buy if available
for i in range(0,n_customers):
    size,price = map(int,raw_input().split())
    if stock[size] > 0:
        stock[size]-=1
        money += price

print money
