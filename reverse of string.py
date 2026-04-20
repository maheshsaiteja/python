

s=input("Enter a string:")
l=list(s)
print(f"list form  of string: {s} is {l}")
t=[]
for i in range (0,len(l)):
    t.append(l[len(l)-1-i])
c=''.join(t)
print(f"string in reverse form of list: {l} is {c}")

