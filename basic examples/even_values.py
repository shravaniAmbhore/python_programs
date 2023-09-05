#print all even numbers between 1 to n (take n value from the user).
n=int(input("enter the number:"))
i=2
while i<=n:
    print(i)
    i=i+2

   #  also we can write the program in different way
n=int(input("enter the num:"))
while i<=n:
    if i%2==0:
        print(i)
        i=i+1

