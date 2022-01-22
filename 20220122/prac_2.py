import random
key = random.randint(0 ,100)
if key > 100 or key < 0:
        print("0~100辣幹")
answer = -1
count = 0
max = 100
min = 0
while answer != key:
    answer = int(input("猜~"))
    if answer > key:
        max = answer
        print("小點",min,"~",max)
        count+=1
    if answer < key:
        min = answer
        print("大點",min,"~",max)
        count+=1
count+=1
if count > 10:
    lol = "等到花都謝了"
elif count == 1:
    lol = "作弊吧，居然"
else:
    lol = "恩" 
print(lol,"對了","猜了",count,"次")
    

