

class employee:
    company="Google"
    def getsalary(self):
        print("Salary of employee",self.name, "working in", self.company, "is $", self.salary)

raj=employee()
raj.name="Raj"
raj.salary=10000
raj.getsalary()