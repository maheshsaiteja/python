t = int(input("Enter the target number: "))
n = int(input("Enter number of elements: "))

s = []  

for i in range(n):
    num = int(input("Enter number: "))
    s.append(num)

l = len(s)

for i in range(l):
    for j in range(i + 1, l):
        if s[i] + s[j] == t:
            print("The index  are:", i, j)
            print("The numbers are:", s[i], s[j])