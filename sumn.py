num=int(input())
if num<0:
  print("enter the positive number")
else:
  sum=0
  while(num>0):
    sum=sum+num
    num=num-1
  print("the sum is",sum)
