print("welcome to the online bank type 1 to continue")
x = input("press key, 1 to continue")
print("create a login username")
login = input("type the login here: ")
print("is" +login+ "correct?")
y = input("press 1 to continue")
print("Ok, now type how much money you own")
user_ammount = float(input("enter here: "))
print("Ok, you can now add or remove from your bank account")
print("currently, " +user_ammount+ " is in your bank account " +login)
print("thank you for your service " + login + "!" )