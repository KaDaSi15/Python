def check_balance(bal=0):
    if bal < 0:
        raise ValueError("Negative value not permitted")
    
def withd_check(bal,wit):
    if wit > bal:
        raise ValueError("Amount more than balance can not be withdrawal")



def balance():
    while True:
        try:
            bal = float(input("Enter balance of account: "))
            check_balance(bal)
        except ValueError as e:
            print(e)
        else :
            return bal
bal = balance()


def withdraw():
    while True:
        try:
            withdrawal = float(input("Enter amount to be withdrawal: "))
            check_balance(withdrawal)
            withd_check(bal,withdrawal)
        except ValueError as e:
            print(e)
        else:
            return withdrawal
        

withdrawal = withdraw()


print(f"Amount of {withdrawal:,} debited from account you are now left with balance of {bal - withdrawal :,}")
        


