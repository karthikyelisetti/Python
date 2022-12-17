f = open("product.csv", "r")
f.readline()
for i in f:
    lst = i.split(",")
    print("The price of " + lst[1] + " is", lst[2])