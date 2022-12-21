# list=[]
# n=int(input('enter a number='))
# for i in range(1,n+1):
#     element=int(input('enter element here='))
#     list.append(element)
# print(list)
# start=0
# end=len(list)-1
# while start<end:
#     #swap
#     temp=list[start]
#     list[start]=list[end]
#     list[end]=temp
#     start=+1
#     end=-1
# print(list)
    
    
def reverse_list(arr):
    left=0
    right=len(arr)-1
    while(left<right):
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left+=1
        right-=1
    return arr
arr=[1,2,3,4,5,6,7,8,9,10]
print(reverse_list(arr))
    
    