amt=int(input("enter amount:"))
note500=amt//500 
note100=(amt-(note500*500))//100
note50=(amt-(note500*500+note100*100))//50
note10=(amt-(note500*500+note100*100+note50*50))//10
note5=(amt-(note500*500+note100*100+note50*50+note10*10))//5
note1=(amt-(note500*500+note100*100+note50*50+note10*10+note5*5))//1
if(amt>=500): 
    (note500==amt//500) 
    (amt==amt-note500*500)
if(amt>=100):
    (note100==amt//100)
    (amt==amt-note100*100)
if(amt>=50):
    (note50==amt//50)
    (amt==amt-note50*50)
if(amt>10):
    (note10==amt//10)
    (amt==amt-note10*10)
if(amt>5):
    (note5==amt//5)
    (amt==amt-note5*5)
if(amt>1):
    (note1==amt//1)
    (amt==amt-note1*1)
    print("500" , note500)
    print("100" ,note100 )
    print("50" , note50)
    print("10" ,note10)
    print("5", note5)
    print("1" , note1)
# else:
#     print("i dont know")
