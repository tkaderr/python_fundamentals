class mathdojo(object):
    def __init__(self):
        self.sum=0
    def addition(self, *param):
        for i in range(0,len(param)):
            if isinstance(param[i],list):   
                self.sum += sum(param[i])
            else:
                self.sum +=param[i]
        return self
    def subtraction(self, *param):
        for i in range(0,len(param)):
            if isinstance(param[i],list):
                self.sum -= sum(param[i])
            else:
                self.sum -=param[i]
        return self
    def result(self):
        print self.sum

md=mathdojo().addition(2).addition(2, 5).subtraction(3, 2).result()
#md.addition([1],3,4).addition([3, 5, 7, 8], [2, 4.3, 1.25]).subtraction(2, [2,3], [1.1, 2.3]).result()
