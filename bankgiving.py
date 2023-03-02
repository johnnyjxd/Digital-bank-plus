print("welcome to the bank, here to give? to get startet type the ammount you want to give.")
give_ammount = input("enter it here: ")
print("now type the persons user on who you want to donate to")
give_person = input("enter the user here: ")
print("so you are giving $" +give_ammount+ " to " +give_person+ "?")
answer = input("is that corretct?")
if answer == 1:
    print("Ok, donated " +give_ammount+ " to " +give_person)
