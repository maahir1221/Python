class employee:
    company="Google"
    def __intit__(self, name="Rajesh", salary=300000):
        self.name=name
        self.salary=salary

def getdetails(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Employee name", self.name)
        print("Employee Salary", self.salary)

e1=employee("Raj", 100000)
e2=employee("Mahesh")
e3=employee()
print("Employee's detail", employee.company, "Company")
e1.getdetails()
e2.getdetails()
e3.getdetails()