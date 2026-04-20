def sum (a,b):
    return a+b
n=int(input("enter numbers of additions :"))
for i in range(n):
    a,b=map(int,input("enter two numbers :").split())
    result=sum(a,b)
    print("the sum is :",result)