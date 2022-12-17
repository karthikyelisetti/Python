w = open("book1.csv", "w")

#This function will write the mentioned argument 
#in the very first line of the csv file and the entire file will be replaced with the above writelines function
w.write("1, 2, 3, 4, 5, 6")
w.write("\n")
w.write("7, 8, 9, 10, 11, 12")

# we need to close the file for the read operation of the file to take place
w.close()

# reading the file from the csv file to print the latest updates to the book1.csv file
f = open("book1.csv", "r")
print(f.read())
f.close()