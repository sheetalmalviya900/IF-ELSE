a=(input("enter a angle"))
b=(input("enter a angle"))
c=(input("enter a angle"))
if(a==b==c==60):
   (a+b+c==180) 
   print("equilateral triangle")
elif(a==b):
   (b==c)
   (c==a)
   (a+b+c==180)
   print("isoceles triangle")
elif(a!=b):
   (b!=c)
   (c!=a) 
   (a+b+c==180)
#    print("equilateral triangle")
#    print("isoceles triangle")
   print("scalen triangle")
else:
    print("triangle nahi hai")