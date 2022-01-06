# check whether character is upper or lower 
ch=(input('enter a alphabet'))
if(ch>="A" and ch<="Z"):
    print("upper case")
elif(ch>="a" and ch<="z"):
    print("lower case")
elif(ch>=0 and ch<=9):
    print("number")
else:
    print("mix case")