a=0
b=1
n=int(input("enter times="))
print(" ",a," ",b,end="")
for i in range(n):
  c=a+b
  a=b
  b=c
  print(" ",c,end="")