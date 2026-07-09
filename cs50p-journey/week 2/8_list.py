student = ["Kartikey" , "Kushagra" , "Tejas", "Keshav"]#declaring a list of students

'''print(student[0]) #printing the name at 0th index in list of students
print(student[1]) 
print(student[2]) '''


for i in student:# it goes name to name not index to index
    print(i) #printing the name of students one by one


number = len(student) #len() returns the integer value of length of list
print("The number of students in the list is:", number)

for i in range(len(student)):# it goes index to index not name to name
    print(f"{i+1} {student[i]}") #printing the name of students one by one
