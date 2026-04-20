n=int(input("Enter a number upto which u want to print the fibonacci series:"))
f=0
s=1
i=2
print(f,end=" ")
print(s,end=" ")
while i<=n:
    t=f+s
    f=s
    s=t
    print(t,end=" ")
    i=i+1


