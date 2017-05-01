class patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def update_bed_number(self, bed_number):
        self.bed_number = bed_number
class hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = list()
        self.bed_number = 1
    def add_patient(self, id, name, allergies):
        if self.capacity > len(self.patients):
            patient1 = patient(id,name, allergies)
            self.patients.append(patient1)
            patient1.update_bed_number(self.bed_number)#how can you use this update method if it is in a different method?
            self.bed_number+=1
            print "Patient {0} admitted".format(name)
        else:
            print "Hospital is FULL, sorry"
        return self
    def discharge(self, id):
        for pat in self.patients:
            if pat.id == id:
                pat.bed_number = None
                self.patients.remove(pat)
                break
        return self
    def displayInfo(self):
        print "Patients list"
        for pati in self.patients:
            print "--------"
            print "Patient Id: ",pati.id
            print "Patient Name: ",pati.name
            print "Bed number: ",pati.bed_number
        return self
hos1 = hospital("PAMF",3)
hos1.add_patient(123, "aaaa", "lactose").add_patient(456,"bbbb", "cheese")
hos1.add_patient(789, "cccc", "gluten").add_patient(123, "dddd", "peanut")
hos1.discharge(789).displayInfo()
