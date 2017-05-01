import random

def coin_flip(num):
    heads_counter=0
    tails_counter=0
    for i in range (1,num+1):
        randnum=random.randint(0,1)
        if randnum==0:
            tails_counter=tails_counter+1
            print "Attempt #{}: Throwing a coin...Its tails...Got{} heads so far and {} tails so far".format(num,heads_counter,tails_counter)
        else:
            heads_counter=heads_counter+1
            print "Attempt #{}: Throwing a coin...Its heads...Got{} heads so far and {} tails so far".format(num,heads_counter,tails_counter)
    print "Total heads: {} and tails:{}".format(heads_counter,tails_counter)

coin_flip(5)
