class  Employee:
    company="Google"

    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee created")

    def getdetails(self):
        print("Employee Name", self.name)
        print("Employee salary", self.salary)
        print("Employee subunit", self.subunit)
        print("Employee Main unit", self.company)

    def getsalary(self, signature):
        print("Salary of", self.name, "working in", self.company, self.subunit, "is", self.salary)
        print(signature)

    @staticmethod
    def greet():
        print("Good Morning Sir!!")

    @staticmethod
    def timedisplay():
        import datetime
        print(datetime.datetime.now())

raj=Employee("Raj", 500000, "Google")
raj.greet()
raj.getdetails()
raj.getsalary("Thanks!!")
raj.timedisplay()