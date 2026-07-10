print("Enter \'a\' and \'b\' for \"a/b\"")
ans=0
while True:
    try :
        a = float(input("Enter a: "))
    except ValueError:
        print("enter numeric value only....")
    else:
        break


while True:
    try :
        b = float(input("Enter b: "))
        ans = a/b
    except ValueError:
        print("Enter numeric value!!!")
    except ZeroDivisionError:
        print("Divisor i.e \'b\' can not be zero")
    else:
        print(f"{a} / {b}   =   {round(ans , 2)}")
        break