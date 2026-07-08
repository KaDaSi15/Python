k=1 #counter variable


while True:
    n= int(input("Enter counter: "))
    if n<0:
        print("Please enter a positive number")
        continue
    else:
        i=n
        break

while k <= i:
    print("meow")
    k += 1


print('for loop')


'''for loop is used when we know the number of iterations in advance.
 It is also used to iterate over a sequence (list, tuple, dictionary, set, or string).'''

for _ in range(i):# instead of range there could be a list or tuple
    print("meow")

    
print('multiplication of string with integer')


'''multiplication of string with integer'''
print("meow\n" * i , end = "") 