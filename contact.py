names=[]
numbers=[]
n=int(input("enter the number of contach you want to save "))
flag=0
for i in range(n):
  names.append(input("enter the name of contact:"))
  numbers.append(input("enter the number of given name"))
search=input("enter the name you want to find")
for i in range(n):
  if search==names[i]:
    print("contact of given number is:",numbers[i])
    flag=1
if flag==0:
  print("enter valid name")
