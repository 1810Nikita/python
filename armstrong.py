i=int(input("enter number: "))
temp=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10

if(temp==sum):
    print("armstrong number")
else:
    print("not")