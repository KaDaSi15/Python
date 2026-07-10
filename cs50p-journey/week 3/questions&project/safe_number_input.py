while True:
    try:
         x = float(input("Enter any numerical value "))
    except ValueError:
         pass
    else:
         print(f"correct input: {x}")
         break