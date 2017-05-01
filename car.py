class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if self.price>10000:
            self.tax=0.15
        else:
            self.tax=0.12
        self.display_all()

    def display_all(self):
        print "Price:{}".format(self.price)
        print "Speed:{}".format(self.speed)
        print "Fuel:{}".format(self.fuel)
        print "Mileage:{}".format(self.mileage)
        print "Tax:{}".format(self.tax)

car1=car(2000,"35mph","full","15mph")
car2=car(2000000000,"5mph","Not-full","105mpg")
