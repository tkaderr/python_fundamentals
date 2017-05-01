class patients(object):
    def __init__(self,name,allergies):
        self.id_num=0
        self.name=name
        self.allergies=allergies
        self.bed_num=None

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients_list=list()
        self.name=name
        self.capacity=capacity
        self.bed_list=[]
        for i in range(0,capacity):
            self.bed_list=[i]

    def admit(self,name,allergies):
        if len(self.patients_list)<=self.capacity:
            patient1 = patients(name, allergies)
            self.patients_list.append(patient1)
            for i in range(0, self.capacity):
                if self.patients_list[i].bed_num != self.bed_list[i]:
                    self.patients_list[i].bed_num=self.bed_list[i]
                    break;
            patients_list[i].id_num=patients.id_num+1
            self.patients_list[i].id_num=patients.id_num
        else:
            print "No room"
        return self

    def discharge(self,idnumber):
        for i in range(0,len(self.patients_list)):
            if idnumber==self.patients_list[i].id_num:
                self.bed_list.remove(self.patients_list[i].bed_num)
                self.bed_list.append(self.patients_list[i].bed_num)
                self.patients_list.remove(self.patient_list[i])
        return self

    def display_patients(self):
        for i in patients:
            print i.id_num
            print i.name
            print i.allergies
            print i.bed_num



hospital1=Hospital("PAMF",3)
hospital1.admit("Bob","bees").display_patients()
