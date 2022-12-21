c=0
n=int(input("enter a number="))
for i in range(1,n+1):
        for a in range(i):
         if n%i==0:
           c+=1
        if c==2:
          print("prime",n)
    

    