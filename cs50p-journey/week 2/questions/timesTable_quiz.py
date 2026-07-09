nums = {
    7:8,
    9:3,
    12:6,
    16:8,
    13:3,
    11:9,
    19:5,
    25:5,
    18:5,
    17:3
}

score=0

for i in nums:
    ans = int(input(f"Whats\t{i}  x  {nums[i]} :  "))
    if i * nums[i] == ans:
        score+=1

print(f"Your score is {score}")