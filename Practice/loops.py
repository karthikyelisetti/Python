for i in range(10):
    print("Hello World")

while (i <= 10):
    print("While - hello world")
    i += 1

for i in range(0, 11, 2):
    print(i)

for i in range(1, 11):
    print(27*i)

#Sum of 25 natural numbers
sum = 0
for i in range(1, 26):
    sum = sum + i
print(sum)

#Sum of 25 natural numbers using while loop
sum = 0
i = 0
while (i <= 25):
    sum = sum + i
    i = i + 1
print(sum)


# Use for loop to iterate from 0 to 100 and 
# print the sum of all evens
even_sum = 0
for i in range(0, 101, 2):
    even_sum = even_sum + i
print(even_sum)

# print the sum of all odds
odd_sum = 0
for i in range(1, 100, 2):
    odd_sum = odd_sum + i
print(odd_sum)
