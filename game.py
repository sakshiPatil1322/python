li=[]
for i in range (int(input("enter number of player:"))):
  li.append(int(input("enter the score of player:")))
li=set(li)
li=list(li)
li.sort(reverse=True)
print("score of the winner player is",li[0])
print("score of the runner player is",li[1])
