x = int(input("What's x? "))#int is also a function that converts a string to an integer
y = int(input("What's y? "))

z = x + y #5we can also use int() directly in the addition operation

print(z)#or print(x + y)

#print with periods like to say lakh, thousand, etc. we can use 
print(f"{z:,}") #f-string formatting with commas   