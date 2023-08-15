a=int(input("enter any integer:"))
s=str(a)
l=len(s)
b=0
for i in range(0,l,1):
  c=(int(s[i])**l)
  b=b+c  
if b==a:
  print("it is armstrong number")
else:
  print("not armstrong")
