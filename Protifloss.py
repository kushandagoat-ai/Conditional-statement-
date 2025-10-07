actual_price= float(input("Enter the actual amount"))
selling_price= float(input("Enter the selling price"))
if selling_price>actual_price:
    amount=(selling_price-actual_price)
    print("The profit amont is", amount)
else:
    print("No profit")