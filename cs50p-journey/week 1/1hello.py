# ask user for their name and greet them
name = input("what's your name? ")


print("hello,", name)# + will concatenate and , will add a space between the two strings


#remove whitespace from the name
name = name.strip()


#capitalize the first letter of the name(only first letter of the first word will be capitalized)
name=name.capitalize()


#capitalize the first letter of each word in the name
name=name.title()


#split name into first and last name
first, last = name.split(" ")


print(f"hello, {name}")# f-string tells the program to replace the variable name with its value

print(f"your first name is {first} and your last name is {last}")
