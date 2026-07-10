import random
count_head=0
count_tail=0
for i in range(10):
    a="heads" 
    b="tails"
    final = random.choice([a,b])
    if final == a :
        count_head+=1
    elif final == b :
        count_tail+=1

print(f"No of heads : {count_head}\nNo of tails : {count_tail}")