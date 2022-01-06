# check:
# water<1 = needs Hai 
# water>1 and water<10 = no need of water 
# water>10 = water is overflow

water=47
if(water<1):
    print("needs of water")
if(water>1 and water<10):
    print("no need of water")
else:
    print("water is overflow")
