# price of a house is 1m, if buyer has good credit, they need to put down 10%
# otherwise, they need to put down 20%
# print payment

house_price = 1000000

house_10 = house_price / 10

house_20 = house_price / 5

put_down = 0

good_credit = True

if good_credit:
    put_down = house_10
else:
    put_down = house_10

print(f"the down payment is: ${put_down} ")
