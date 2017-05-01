class animal(object):
    def __init__(self, name):
        self.name=name
        self.health=100
    def walk(self):
        self.health=self.health-1
        return self
    def run(self):
        self.health=self.health-5
        return self
    def displayHealth(self):
        print "Name:",self.name
        print "Health:",self.health
class dog(animal):
    def __init__(self,name,height):
        super(dog,self).__init__(name)
        self.health=150
        self.height = height
    def pet(self):
        self.health=self.health+5
        return self
    def displayHealth(self):
        super(dog,self).displayHealth()
        print "Height:",self.height

class dragon(animal):
    def __init__(self,name):
        super(dragon,self).__init__(name)
        self.health=170
    def fly(self):
        self.health=self.health-10
        return self
    def displayHealth(self):
        print ("This is a dragon")
        super(dragon,self).displayHealth()


# animal1=animal("Dog")
# animal1.walk().walk().walk().run().run().displayHealth()
# animal2=dog("Woof")
# animal2.walk().walk().walk().run().run().pet().displayHealth()
# animal3=dragon("Wild")
# animal3.walk().walk().walk().run().run().fly().fly().displayHealth()
animal4=dog("Woof",5)
animal4.displayHealth()
