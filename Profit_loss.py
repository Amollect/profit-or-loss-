#Calculate profit or loss

a_cost=float(input("enter actual cost of product:"))
s_cost=float(input("enter Selling cost of product:"))
if (a_cost>s_cost):
    amt=a_cost-s_cost
    print("loss amount is",amt)
elif(s_cost>a_cost):
    amt=s_cost-a_cost
    print("Profit amount is",amt)
else:
    print("No profit no loss")