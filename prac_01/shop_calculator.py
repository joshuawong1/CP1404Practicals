total = 0
number_items = int(input("enter number of items:"))
while number_items < 0:
    print("Need more items:")
    number_items = int(input("enter number of items:"))
for i in range(number_items):
    price = float(input("enter price of items:"))
    total += price
if total >= 100:
    total *= 0.9
print("Total price for ", number_items, " items is $", total)