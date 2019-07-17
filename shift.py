k,l=map(int,input().split())
b=list(map(int,input().split()[:k]))
for i in range (0,l):
  b=[b[-1]]+c[:-1]
for j in b:
  print(j,end=" ")
