def vowels(char):
    vowels='aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return False

char = input("Enter the sentence to check: ")
count=0

for i in char:
    if vowels(i):
        count += 1
    
print(f"Number of vowels: {count}")