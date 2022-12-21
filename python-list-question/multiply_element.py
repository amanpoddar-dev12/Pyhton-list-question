def mul_list(list):
 print(list)
 mul=1
 for i in list:
    mul=mul*i
 return mul

list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element here='))
    list.append(element)
result=mul_list(list)
print(result)
