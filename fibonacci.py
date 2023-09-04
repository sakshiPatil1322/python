n=int(input("enter the value of series length:"))
a=[0,1]
first=0
last=1
for i in range(n-1):
  sum=first+last
  a.append(sum)
  first=last
  last=sum
print(a)  
