def hello(to="world"):#in perenthesis goes the value we pass(to) and a default value(=" ") if we don't pass
    print(f"Hello, {to}")

def main():
    hello() #if we don't pass any value it will print the default value
    name = input("What's your name: ")
    hello(name)
    hey(name)

def hey(to="user"):#in perenthesis goes the value we pass(to) and a default value(=" ") if we don't pass
    print(f"Hey, {to}")

main()# calling the main function to execute the code
''' without main there would be an error because the function hey would
 not be found when control will transfer at line 8. The main function 
 is used to call other functions and execute the code. It is a good
 practice to  have a main function in your code.'''