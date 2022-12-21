arr=[]
n=int(input('enter a number='))
for i in range(1,n+1):
    element=int(input('enter element here='))
    arr.append(element)
print(arr)
arr=list(set(arr))
#index=len(arr)-2
print(arr[len(arr)-2])
      

