list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element in a list:'))
    list.append(element)
print('Before interchnage the element')
print(list)
size=len(list)
max_element=list[0]   

list[0]=list[size-1]

list[size-1]=max_element
print('After interchnage the element')
print(list) 
