# x = int(input("num"))
# answer = x*(1+x) /2
# print(answer)
x = int(input("num"))
n = 0
sum = 0
txt = "0"
while n<x:    
    n+=1
    sum+=n
    txt = txt + "+" + str(n)
print(txt,"=",sum)