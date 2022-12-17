result = 0
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "**":
    result = num1 ** num2
elif operator == "/":
    result = num1 / num2

print ("The result is: ", result)