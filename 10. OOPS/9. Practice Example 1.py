class programmer:
    company="canon"
    def __init__(self,name,subunit):
        self.name=name
        self.subunit=subunit

    def getdetails(self):
        print("Tee name of", {self.company},"Programmer is", {self.name}, "and working in", {self.subunit},"Subunit")

e1=programmer("Mahesh", "Camera")
e2=programmer("Ramesh", "Printer")
e1.getdetails()
e2.getdetails()