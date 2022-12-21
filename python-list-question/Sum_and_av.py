
list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element here='))
    list.append(element)
print('Your list',list)
sum=0 
count=0
for i in list:
    sum=sum+i
    count=count+1
print('average of {} is {} and addition of Your list is {}'.format(list,sum//count,sum))