score_list=[]
name_list=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append(score)
    name_list.append([name,score])
s=set(score_list)
l=list(s)
l.sort()
sls=l[1]
sls_list=[]
for i,j in name_list:
  if j==sls:
    sls_list.append(i)
sls_list.sort()    
for k in (sls_list):
  print(k)
