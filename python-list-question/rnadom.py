from cmath import sqrt
from this import d


a=float(input("enter a number="))
b=float(input("enter second number="))
c=float(input("enter third number="))
d=(b**2)-(4*a*c)
if d>=0:
    v1=(-b+sqrt+(d))/(2*a)
    v2=(-b+sqrt+(d))/(2*a)
    print("value",v1,"value",v2)
else:
    print("value not possible")
    


        