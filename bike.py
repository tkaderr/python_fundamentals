class bike(object):
    def __init__(self,price,max_speed):
        self.price=price
        self.max_speed=max_speed
        self.miles=0
    def displayInfo(self):
        print "The bike costs {} and the maximum speed {} and the total miles is {}".format(self.price,self.max_speed,self.miles)
        return self
    def ride(self):
        print "Riding"
        self.miles=self.miles+10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles<=0:
            self.miles=0
        else:
            self.miles=self.miles-5
        return self

bike1=bike(200,"25mph")
bike2=bike(100,"10mph")
bike3=bike(50,"5mph")
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
