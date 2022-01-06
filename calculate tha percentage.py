# five subject physics, chemistry, biology, mathematics and computer ;calculate percentage and grade according to following:
a=int(input("enter a percentage :"))

if(a>=90):
    print("grade A")
elif(a<90 and a>=80):
    print("grade B")
elif(a<80 and a>=70):
    print("grade C")
elif(a<70 and a>=60):
    print("grade D")
elif(a<60 and a>=40):
    print("grade E")
elif(a>33 and a<40):
    print("grade F")
else:
    print("you are fail")