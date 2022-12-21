list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element here='))
    list.append(element)
print(list)
list1=[]
for element in list:
    sum=0
    for digit in str(element):
        sum=sum+int(digit)
    list1.append(sum)
print('after addding element in a list1',list1)