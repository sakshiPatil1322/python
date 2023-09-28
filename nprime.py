n=int(input("enter any number"))
count=0
i=0
print("1")
while(count!=n-1):
  i=i+1
  flag=0
  for j in range(1,i+1,1):
    if(i%j==0):
      flag=flag+1
  if (flag==2):
    print(i)
    count=count+1
  
