n=int(input("enter any no:"))
flag=0
if n==1:
  print("given no is prime")
else:  
  for i in range(1,n+1,1):
    if n%i==0:
      flag=flag+1
  if flag==2:
    print("given no is prime")
  else:
    print("not prime")
