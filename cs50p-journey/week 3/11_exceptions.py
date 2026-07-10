def get_int(prompt):
    while True:
        try:
            x = float(input(prompt))
            if x<0:
                raise ValueError("Can't be Negative")
        except ValueError as e: #we can use [except Exception] that catches every error but make it very difficult to find bugs 
            print(e) # e refers to default message shown due to error
            pass # do nothing and move control to next line
        else:#if nothing goes wrong
            return x


def main():
    x = get_int("What's x? ")
    print(f"X is {x}")

main()
    