a=int(input("enter num1:"))
b=int(input("enter num2:"))
temp=0
l = a if a > b else b
for i in range(1,l,1):
  if a%i==0 and b%i==0 and (temp<i or temp==i):
    temp=i
print(temp)  
