actual_cost = float(input("please enter the actual product cost :"))
sale_amount = float(input("please enter the actual sale cost :"))

if(sale_amount > actual_cost) :

    amount = sale_amount  - actual_cost
    print( "Total profit= ", amount)

else:
    print("no profit!!!")