print(1+2+3+4+5)
print(1*2/3*4)
print(2**(1/2))
pi = 3.14
print(pi)
max=max(1,2,100)
print(max)

print("%dis%3d , both them are%3d" %(87 ,87 ,87))

#欄位
print("{0:3s} {1:3s}  {2:f}".format("123","9*9",pi))
print("{0:3s} {1:3s}  {2:s}".format("456","81","-----"))
print("{0:3s} {1:3s}  {2:f}".format("789","3²*3²",pi))
#資料型態辨識
print(type(True),type("str"),type(000),type(1.00))

ans = input("number!!!")
print(type(ans))
if(type(ans) == str):
    print(True)
else:
    print(False)
