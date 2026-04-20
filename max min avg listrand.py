import random
num=[random.randint(1,100) for i in range(20)]
print(num)
print("Minimum Number :",min(num))
print("Maximum Number :",max(num))
print("Average of Numbers :",sum(num)//len(num))
Ec=0
  for i in num:
    if i%2==0:
        Ec+=1
print("Even Numbers:",Ec)        