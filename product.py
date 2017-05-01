class product(object):
    def __init__(self,price,item_name,weight,cost,brand):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.cost=cost
        self.brand=brand
        self.status="For Sale"
        self.box="New"
    def sell(self):
        self.status="Sold"
        return self
    def add_tax(self):
        self.price=self.price+(self.price*0.12)
        return self
    def return_(self):
        if self.box=="Defective":
            self.status="Defective"
            self.price=0
        elif self.box=="New":
            self.status="For Sale"
        elif self.box=="Opened":
            self.status="Used"
            self.price=self.price*0.8
        return self
    def displayInfo(self):
        print "Price:",self.price
        print "ItemName:",self.item_name
        print "Weight:",self.weight
        print "Brand:",self.brand
        print "Status:",self.status
        print "Product Status:",self.box

product1=product(6,"Cereal","5 lbs", "Kellogs",3)
product1.displayInfo()
