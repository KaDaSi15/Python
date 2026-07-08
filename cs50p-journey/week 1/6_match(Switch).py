name = input("What's your name? ")
first =name.split(" ")[0].capitalize()

match first:
    case "Kartikey":
        print("Shastri") 
    case "Tejas":
        print("Tagore")
    case "Kushagra":
        print("Gandhi")
    case "Keshav":
        print("Nehru")
    case _:
        print("Who?")