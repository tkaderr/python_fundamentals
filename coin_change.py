import math

def coin_change(num):
    name=["Dollars","Quarters","Dimes","Nickels","Pennies"]
    coins=[100,25,10,5,1]
    newarr=[]
    for i in range(0,len(coins)):
        newarr.append(int(math.floor(num/coins[i])))
        num=num%coins[i]
        print name[i], ":",newarr[i]

coin_change(210)
