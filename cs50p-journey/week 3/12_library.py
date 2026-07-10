import random #import the random module/library
import statistics

#random
def rand():
    coin = random.choice(["heads","tails"]) #in parameters we'll pass a list
    prints = random.choices(["heads","tails"],k=5)#Returns (k) random items from the list (duplicates allowed)                                        
    num = random.random()# return random float between 0.0 and 1.0
    cool = random.sample(["heads","tails","your win"],k=3)# Returns unique random items(k in number, k<=2)from the list (no duplicates)
    integer = random.randint(a=5,b=9)#random number between a and b(a<b)
    
    
    cards = ["king","queen","jack"]
    random.shuffle(cards)# shuffles the list you pass
    for card in cards:
        print(card)


#statistics
def stat():
    avg = statistics.mean([19,25,76])#calculate average of a list
    med = statistics.median([24,33,23,55])#calculate median of a list
    mod = statistics.mode([23,45,12,76,12])#calculate mode of a list
    variance_value = statistics.variance([55,65,75,45,35])# calculate sample variance
    print(variance_value)
   

