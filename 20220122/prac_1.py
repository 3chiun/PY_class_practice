import random
key = random.randint(0 ,int(input("NUMBER")))
answer = 0
while answer != key:
    answer+=1
print("password","is",str(answer),str(key))
