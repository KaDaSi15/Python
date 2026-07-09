def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not prime"
    return "Prime"

number = int(input("Enter the number: "))
print(prime(number))
