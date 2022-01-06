girls=int(input("enter the no. of girls"))
lessgirl=12-girls
moregirl=girls-12
if(girls<12):
    print("need : " + str(lessgirl))
elif(girls>12):
    print("extra : "+str(moregirl))
elif(girls==12):
    print('equal to 12')
# else:
    # print("boys hai")
