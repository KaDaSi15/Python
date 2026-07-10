import random
import string
def inp():
    while True: 
        try: 
            return int(input("Enter the length of password: "))
        except ValueError:
            print("only integral values supported!!!")

def generate():
    passw=""

    k=inp()
    chars = string.ascii_letters + string.punctuation + string.digits


    for i in range(k):
        passw += random.choice(chars)

    print(f"password is: {passw}")

def main():
    generate()
    while True:
        choice = input("Do you want another password (y/N): ")
        if choice == "N":
            break
        else:
            return main()

main()