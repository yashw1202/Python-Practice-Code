operator = input("Enter the operator + - * / : ")
if operator == "+":
    num1 = int(input("Enter the number1 : "))
    num2 = int(input("Enter the number2 : "))
    result = num1 + num2
    print(f"Your answer is : {result}  ")
elif operator == "-":
    num1 = int(input("Enter the number1 : "))
    num2 = int(input("Enter the number2 : "))
    result = num1 - num2
    print(f"Your answer is : {result}  ")
elif operator == "*":
    num1 = int(input("Enter the number1 : "))
    num2 = int(input("Enter the number2 : "))
    result = num1 * num2
    print(f"Your answer is : {result}  ")
elif operator == "/":
    num1 = int(input("Enter the number1 : "))
    num2 = int(input("Enter the number2 : "))
    result = num1 / num2
    print(f"Your answer is : {round(result, 2)}  ")
else:
    print(f"{operator} is not valid operator")
