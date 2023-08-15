a="" 
b=""
vowel="aeiouAEIOU"
for i in range(0,5,1):
  kelvin=input("enter strings for kelvin:") 
  a=a+kelvin[0]
for i in range(0,5,1):
  shiv=input("enterstrings for shiv:")
  b=b+shiv[0]
flag1=0
for i in a:
  if i in vowel:
    flag1=flag1+1
flag2=0  
for i in b:
  if i in vowel:
    flag2=flag2+1
if flag1==0 and flag2==0:
  print("fails")
elif flag1==flag2:
  print("tie")
elif flag1<flag2:
  print("shiv is win")
elif flag1>flag2:
  print("kelvin is win")
else:
  print("enter valid string")
