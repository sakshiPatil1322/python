n=int(input("enter range of contact:"))
name=list(map(str,input("enter the name:").split()))[:n]
number=list(map(int,input("enter the number:").split()))[:n]
search=input("enter the name you have to searche a number")
for i in range(len(name)):
  if search==name[i]:
    print(number[i])
