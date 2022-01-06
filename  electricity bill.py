unit=int(input("enter the unit :"))
Rs1=5*unit
Rs2=10*unit
if(unit<=100):
    print("no charge")
elif(unit>100 and unit<=200):
    print("chrge",Rs1)
elif(unit>200):
    print("charge",Rs2)