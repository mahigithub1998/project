nu=int(input())
if nu<0:
  print("enter positive number")
else:
  sum=0
  while(nu>0):
    sum=sum+nu
    nu=nu-1
  print("the sum is",sum)
