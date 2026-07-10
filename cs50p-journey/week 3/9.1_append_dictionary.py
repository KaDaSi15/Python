students = {
     "Kartikey":"Shastri", # it's like index of shastri is kartikey
     "Keshav":"Nehru",
     "Tejas":"Tagore",
     "Kushagra":"Gandhi"
     }

new_name = input("Enter the name of student you want to add: ")
house = input(f"Enter the house of {new_name}: ")

students[new_name]=house # this creates new index in dictionary named as (new_name) with its value as(house)

for name in students:
    print(name,students[name] , sep="-->")
