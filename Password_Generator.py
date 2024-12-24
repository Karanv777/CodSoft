import random

pass_Lenth = int(input("Enter Password Length : "))

while (pass_Lenth > 3):
    char_pass = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


    passWord = ""

    for i in range (pass_Lenth):
        passWord = passWord + random.choice(char_pass) 

    print ("Your password : ", passWord)
    break

if (pass_Lenth < 3):
    print ("\nPassword should be greater than 3 Charactersa\n")