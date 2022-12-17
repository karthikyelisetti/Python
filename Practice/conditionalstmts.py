#check if the given number is odd or even
num = int(input("enter the number: "))

if (num % 2 == 0):
    print("Entered number is a even number")
else: #(num % 2 == 1):
    print("Entered number is odd number")

#Challenge:
# A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print percentage of class attended
# Is student is allowed to sit in exam or not.

#Solution:
# Input variables to pass the inputs for the number of classes
classesHeld = int(input("enter the number of classes held: "))
classesAttended = int(input("enter the number of classes attended: "))

#Calculating the percentage of the classes attended
percentage = round((classesAttended / classesHeld)*100)
percentage_str = str(percentage)+"%"
print("Percentage of the classes Attended:" ,percentage_str)

if (percentage < 75):
    print("Student is not allowed to sit in exam as the percentage is: "+percentage_str)
else:
    print("Student is allowed to sit in exam as the percentage is: "+percentage_str)
