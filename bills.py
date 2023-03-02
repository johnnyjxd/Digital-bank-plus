print("here is where your bills show up")
user_ammount = float(input("enter your ammount of usd cash: "))
print("you have 2 unpaid bills: ")
print("1. water bill")
print("2. house bill")
print("water bill is $110 and house bill is $235.98")
bill_ammount = float(input("pay 1 or 2"))
house_bill = 235.98
water_bill = 110
total2 = user_ammount - water_bill
total1 = user_ammount - house_bill
if bill_ammount == 2:
    print(total1) 
    print("left in your account")
elif bill_ammount == 1:
    print(total2) 
    print("left in your account")
