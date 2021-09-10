n=int(input("enter no. of terms"))
a=0
b=1
count=0

if n<=0:
    print("enter a positive integer")
elif n == 1:
    print("fibonacci series upto"":")
    print(a)
else:
    print("fibonacci series:")
    while count<n:
        print(a,end="")
        c=a+b
        a=b
        b=c
        count+=1