n=int(input("Enter a number:"))
d=len(str(n))
c=n
s=0
while(n!=0):
    r=n%10
    s=s+r**d
    n=n//10
if s==c:
    print(f"{c} is an armstrong number")
else:
    print(f"{c} is not armstrong number")        
