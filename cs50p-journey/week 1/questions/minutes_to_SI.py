minutes = int(input("Enter the number of minutes: "))
hours = int(minutes / 60)
minutes = minutes % 60
print(f"{hours}:{minutes}")