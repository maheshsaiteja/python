n=int(input("Enter a number :"))
tem=n
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
if tem==rev:
    print(f"{tem} is a palindrome number")
else:
    print(f"{tem} is not a palindrome numer")
        