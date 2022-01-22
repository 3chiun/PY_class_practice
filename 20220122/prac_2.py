import random
key = random.randint(0 ,100)
if key > 100 or key < 0:
        print("0~100辣幹")
answer = -1
count = 0
max = 101
min = 0
while answer != key:
    try:
        answer = int(input("猜~"))
    except:
        print("蛤? 猜數字ㄟ")
        continue    
    if answer > key and max > answer:
        max = answer
        print("小點",min,"~",max)
        count+=1
    elif answer < key and min < answer:
        min = answer
        print("大點",min,"~",max)
        count+=1
    elif answer == key:
        break
    else:
        print("你是在哭嗎???")
        count+=1
count+=1
if count > 10:
    lol = "等到花都謝了"
elif count == 1:
    lol = "作弊吧，居然"
else:
    lol = "恩" 
print(lol,"對了","猜了",count,"次")

# try: 試錯

# except: 出錯執行

# finally: 無論如何都執行

# else: 無錯執行   