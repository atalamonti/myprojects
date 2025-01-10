#Angelo Talamonti
#Simple Calculator

#Init

#Function
def add (num1, num2):
    result = num1 + num2
    print("The result is: " + str(result))
def subtract(num1, num2):
    result = num1 - num2
    print("The result is: " + str(result))
def multiply(num1, num2):
    result = num1 * num2
    print("The result is: " + str(result))
def divide(num1, num2):
    result = num1 / num2
    print("The result is: " + str(result))
def calculator():
    print("Welcome Preschoolers to Simple Calculator!")
    while True:
        print("Please choose an operation: ")
        print("""
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Quit""")
        operation = int(input("(1-5) :"))
        if operation == 1:
            add1 = int(input("Enter first number: "))
            add2 = int(input("Enter second number: "))
            add(add1,add2)
        if operation == 2:
            sub1 = int(input("Enter first number: "))
            sub2 = int(input("Enter second number: "))
            subtract(sub1,sub2)
        if operation == 3:
            mul1 = int(input("Enter first number: "))
            mul2 = int(input("Enter second number: "))
            multiply(mul1,mul2)
        if operation == 4:
            div1 = int(input("Enter first number: "))
            div2 = int(input("Enter second number: "))
            divide(div1,div2)
        if operation == 5:
            print("Goodbye")
            break

#Main

calculator()
