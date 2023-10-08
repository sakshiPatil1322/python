s=int(input("enter starting intenger of range:"))
e=int(input("enter ending intenger of your range:"))
def prime():  
  for i in range(s,e+1,1):
    flag=0
    for j in range(1,i+1,1):
      if(i%j==0):
        flag+=1
    if flag==2:
      print(i)
if(s==1):
  print(1)
  prime()
else:
  prime()
    
