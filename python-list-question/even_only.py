list=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element here='))
    list.append(element)
print(list)
even_count=0
odd_count=0
for i in range(1,len(list)+1):
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print('count of even is {} and odd is {}'.format(even_count,odd_count))   
        



