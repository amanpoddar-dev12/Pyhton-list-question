list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element in a list:'))
    list.append(element)
print('Before interchnage the element')
print(list)
size=len(list)
num1=int(input('enter a postion 1='))
num2=int(input('enter a postion 2='))

max_element=list[num1-1]   

list[num1-1]=list[num2-1]

list[num2-1]=max_element
print('After interchnage the element')
print(list) 
