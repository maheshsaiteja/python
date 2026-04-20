num1=int(input(" enter first number"))
num2=int(input(" enter second number"))
choise=input("enter your choise :+,-,/,%,*,**:")
if (choise =='+'):
    print(f"{num1}+{num2}={num1+num2}")
elif (choise =='-'):
    print(f"{num1}+{num2}={num1-num2}")
elif (choise =='/'):       
    print(f"{num1}/{num2}={num1/num2}")
elif (choise =='%'):  
    print(f"{num1}%{num2}={num1%num2}")
elif (choise =='*') :  
    print(f"{num1}*{num2}={num1*num2}")
elif (choise=='**') :   
    print(f"{num1}**{num2}={num1**num2}")
else :        
    print("invailed choise")    