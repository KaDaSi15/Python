import statistics
print('Enter subject and it\'s marks respectively, and just press enter when you\'re done')
dictt = {}
score = []
sub = None
marks = 0
while True:
    sub = input("Enter the name of subject: ").strip().capitalize()
    if sub == "" :
        break
    while True:
        try :
            marks = float(input("Enter the marks: "))
        except ValueError :
            print("Enter numeric value!!!!!")
        else:
            break
    dictt[sub] = marks



for name in dictt:
    print(f"Subject: {name}\tMarks: {dictt[name]}")
    score.append(dictt[name])

avg_marks = statistics.mean(score)

print(f"Average marks are {avg_marks}")
