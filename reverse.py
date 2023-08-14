a=int(input("enter any integer"))
s=str(a)
l=len(s)
b=" "
for i in range(0,l,1) :
  b=s[i]+b
print(b)  
