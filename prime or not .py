n=int(input("Enter a number:"))
f=0
for i in range(1,n+1):
    if n%i==0:
        f=f+1
if f==2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")            