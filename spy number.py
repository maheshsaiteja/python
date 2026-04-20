n=int(input("Enter a number"))
sd=0
sp=1
c=n
while n!=0:
    r=n%10
    sd=sd+r
    sp=sp*r
    n=n//10
if sp==sd:
    print(f"{c} is a spy number")
else:
    print(f"{c} is not a spy number")        