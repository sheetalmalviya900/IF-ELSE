num=int(input("Enter the number"))
a=num%10
b=(num//10)%10
c=(num//100)%10
if(num<1000):
    print(a*100+b*10+c)