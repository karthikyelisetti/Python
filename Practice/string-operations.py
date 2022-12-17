a = 'Hello World!'

print (len(a))
print ("Index of a[0] is: "+a[-1])
print(a[5])
print(a[0:5])
print(a[-6:-1])
print(a[:5])
print(a[0:5:2])
print(a[::-1])

string1 = "Hello"
string2 = "World"

print ("concatenation: "+ string1+' '+string2)
print ("multiple the string: "+ string1 * 5)

print ("lower case: "+ string1.lower())
print ("upper case: "+ string1.upper())

print (string1.startswith("H"))

print (a.index('W'))
print (a.count('l'))