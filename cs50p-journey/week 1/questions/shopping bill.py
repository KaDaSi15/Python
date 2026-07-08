def amount(price , qty):
    return round(price*qty,2)

def main():
    n = int(input("Enter the number of items: "))
    tamt=0
    item = [None]*n
    price = [None]*n
    qty = [None]*n
    amt = [None]*n
    for i in range(n):
        print(f"for item {i+1}")
        item[i] = input("Enter name of item: ").capitalize().split(" ")[0]
        price[i]=round(float(input("Enter the price of item: ")),2)
        qty[i]=int(input("Enter quantity: "))
        amt[i]= amount(price[i],qty[i])
        tamt+=amt[i]
    print("Item\t\tPrice\t\tQty\t\tAmount")
    for i in range(n):
        print(f"{item[i]}\t\t{price[i]}\t\t{qty[i]}\t\t{amt[i]}")
    print(f"total amount: {tamt:,}")
    Discount=discount(tamt)*tamt
    tamt-=Discount
    print(f"Discount: {Discount}\nBilling Amount: {tamt:,}")

def discount(Amt:0):
    if Amt>20000:
        return .25
    elif Amt>15000:
        return .20
    elif Amt>10000:
        return .18
    elif Amt>5000:
        return .10
    elif Amt>3000:
        return .08
    else:
        return 0
    
main()
