students = {
     "Kartikey":"Shastri", # it's like index of shastri is kartikey
     "Keshav":"Nehru",
     "Tejas":"Tagore",
     "Kushagra":"Gandhi"
     }

#print(students["Keshav"])

for name in students:#index is name
    print(name,students[name], sep="-->")

print("list of dictionaries ")
'''a list of dictionaries i.e. each name is itself a dictionary'''
students = [
    {"name":"Kartikey", "house":"Shastri", "future":"IT"},#whole dictionary is index for list, and name,house and future are index for dictionary
    {"name":"Tejas", "house":"Tagore", "future":"Bussiness"},
    {"name":"Keshav", "house":"Nehru", "future":None},
    {"name":"Kushagra", "house":"Gandhi", "future":"IIT"},
]

for person in students:
    # if we use: for i in range(len(students)): then we'd need students[i] to call a list cause whole dictionary is index for list
    print(person["name"], person["house"], person["future"], sep="-->")
    print(person)