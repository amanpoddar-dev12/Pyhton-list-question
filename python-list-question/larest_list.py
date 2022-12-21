list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element here='))
    list.append(element)
print(list)
list.sort()
largest_index=len(list)-1
print('smallest element in Your list is',list[largest_index])
