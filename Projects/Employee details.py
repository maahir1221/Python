class employee:
    def __init__(self, employeepost, employeesalary):
        self.employeepost = employeepost
        self.employeesalary = employeesalary

    def amount(self):
        return self.employeesalary+self.employeepost
    def show(self):
        print(f"Post: {self.employeepost}, Salary: {self.employeesalary}")

class details:
    def add_employee(self):
        item = employee(employeepost=input("Post of Employee"))

