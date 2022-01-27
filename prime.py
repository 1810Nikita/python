a= int(input("enter first number:"))
b=int(input("enter second number:"))
for i in range(a,b+1):
    flag=1
    for j in range(2,(i//2)+1):
        if(i%j==0):
            flag=0
            break
    if flag==1 and i>1:
        print("prime number",i)



        
    
        
