print("your options are:")
print(" \na:sum\n b:sub\n c:mul\n d:div\n e:modulus\n f:flor division\n g:power")
opt=input("\n\nenter your option")
if opt=='a':
  n1=int(input("enter num 1"))
  n2=int(input("enter num 2"))
  print("your sum is",n1+n2)
elif opt=='b':
  n1=int(input("enter num 1"))
  n2=int(input("enter num 2"))
  print("your sub is",n1-n2)
elif opt=='c':
  n1=int(input("enter num 1"))
  n2=int(input("enter num 2"))
  print("your multiplication is",n1*n2) 
elif opt=='d':
  n1=int(input("enter dividend 1"))
  n2=int(input("enter divisor 2"))
  print("your division is",n1/n2)
elif opt=='e':
  n1=int(input("enter num 1"))
  n2=int(input("enter num 2"))
  print("your modulus is",n1%n2)  
elif opt=='f':
  n1=int(input("enter num 1"))
  n2=int(input("enter num 2"))
  print("your flor division is",n1//n2)
elif opt=='g':
  n1=int(input("enter base number"))
  n2=int(input("enter power number"))
  print("your power is",n1**n2)  
else :
  print("please enter valid opetion")
