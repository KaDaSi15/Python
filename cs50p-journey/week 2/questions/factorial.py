def factorial(n=0):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

num =int(input("Enter the number: "))
print(f"Factorial of {num} is {factorial(num)}")
# this program is about 