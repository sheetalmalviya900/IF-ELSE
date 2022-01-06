num1=int(input("Enter the three digit number"))
a=num1%10
if a%3==0:
    print(a,"divisible by 3" )
else:
    print("not divisible",a)
