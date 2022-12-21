list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element here='))
    list.append(element)
print('before copying',list)
list1=[]
for i in list:
    list1.append(i)
    
print('after copying',list1)