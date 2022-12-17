result = 0
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def exp(num1, num2):
    return num1 ** num2

def div(num1, num2):
    return num1 / num2

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = sub(num1, num2)
elif operator == "*":
    result = mul(num1, num2)
elif operator == "**":
    result = exp(num1, num2)
elif operator == "/":
    result = div(num1, num2)

print ("The result is: ", result)