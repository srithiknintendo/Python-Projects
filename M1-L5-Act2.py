actual_cost = float(input("Enter the starting price:"))
sale_cost = float(input("Enter the sale price:"))

if (actual_cost < sale_cost):
    amount = (sale_cost - actual_cost)
    print("Total Profit =", format(amount))
else:
    print("NO PROFIT")