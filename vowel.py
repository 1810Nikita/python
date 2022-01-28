n=int(input("enter  number of elements: "))
arr=[]

print("enter elements: ")

for i in range(0,n):
    arr.append(int(input()))

x=list(dict.fromkeys(arr))

for i in x:

    print("\n {} occurs {} time(s)".format(i,arr.count(i)))


