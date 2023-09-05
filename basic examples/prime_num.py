n=int(input("enter the num:"))
i=2
x=1
while i<n:
    if n%i==0:
        print("not prime num")
        x=0
        break
    i=i+1
if x==1:
    print("prime num")