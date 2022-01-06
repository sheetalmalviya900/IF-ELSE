name=(input("enter the word :"))
if("ing"in name):
    k=name[0:-3]
    print(k+"ly")
elif("ly"in name):
    k=name[0:-2]
    print(k+"ing")
else:
    print(name+"ly"+"ing") 