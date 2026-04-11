cost = float(input("Enter the Cost of product "))
sales = float(input("Enter the sales of product "))

if (sales > cost):
    profit = sales - cost
    print("Profit is", profit)
else:
    print("No profit!!")