def add( num1, num2):
    return num1 + num2

def sub( num1, num2):
    return num1 - num2

def mul( num1, num2):
    return num1 * num2

def div( num1, num2):
    try:
        return num1 / num2
    
    except ZeroDivisionError:
        return "Division by zero is not possible"
    
while (True):
    
    print("\tBasic Arithmatic Calculator")
    print("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide")

    ch = input("Enter Your choice : ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if ch == "1":
        print (add(num1 , num2))

    elif ch == "2":
        print (sub(num1 , num2))

    elif ch == "3":
        print (mul(num1, num2))

    elif ch == "4":
        print (div(num1, num2))

    else:
        print ("Please enter a valid input!")
    
    nxt = input ("You want to continue? (yes/no): ")
    if nxt.lower() == "no" :
        break

    