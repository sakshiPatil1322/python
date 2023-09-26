a=input("enter any number:")
b="" 
for i in a:
  if (i=="0") or (i=="1"):
    b=b+i 
if b==a:
  print("given number is binary")
else:
  print("given number is not binary")
