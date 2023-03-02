print("welcome to the online bank, here to withdraw cash?")
print("if so, then enter your ammount you have as of right now")
user_ammount = float(input("enter it here: "))
print("now enter the ammount you want to add to it")
user_add = float(input("enter it here: "))
total_ammout = user_ammount - user_add
print("your bank acount has $ " +total_ammout+ " in it")