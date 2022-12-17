num = int(input("Enter a range number: "))
num1 = 0
num2 = 1
counter = 0
for val in range(0, num):
    if counter < num:
        print(num1)
        num1 = num2
        num2 = num1 + num2
        counter += 1  

