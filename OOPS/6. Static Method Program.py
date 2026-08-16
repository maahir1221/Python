class Employee:
    company="Google"

    def getSalary(self,signature):
        print ("Salary of Employee",self.name,"working in",self.company,"is $",self.salary)
        print (signature)

    @staticmethod
    def greet():
        print ("Good Morning .. Sir !! ")
    @staticmethod
    def timeDisplay():
        import datetime
        print (datetime.datetime.now())
raj=Employee()
raj.name="Raj"
raj.salary=10000
raj.greet()# Employee.greet()
raj.getSalary("Thanks ..!! ")# Employee.getSalary(raj)
raj.timeDisplay()