name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age<18:
    print("go to WHO site for this age group")
    exit()
weight = float(input("Enter your weight: "))
height = input("Enter your height in feet format[f/in]")
def unitc(height):
    feet,inch=height.split("/")
    feet=int(feet)
    inch=int(inch)
    inch+=feet*12
    return inch*0.0254
height=unitc(height)
bmi=round(weight/(height**2),1)
print(f"BMI is {bmi}")
if bmi<=18.5:
    print("Underweight")
elif bmi<24.9:
    print("Normal Weight")
elif bmi<29.9:
    print("Overweight")
else:
    print("Obese")
