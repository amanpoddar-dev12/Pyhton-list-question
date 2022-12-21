def count_element(list,num):
 count=0
 for i in list:
    if i==num: 
        count=count+1
 return count
list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element here='))
    list.append(element)
num=int(input('Which element You want to find:'))
result=count_element(list,num)
print('Your element {} has occurred {} times'.format(num,count_element(list,num)))