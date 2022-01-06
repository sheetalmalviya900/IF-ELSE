num=int(input("enter the number"))
if(num%7==0 and num%8==0):
    print("navgurukul")
elif(num%7==0):
    print("nav")
elif(num%8==0):
    print("gurukul")
else:
    print("not divisible by 7 and 8")