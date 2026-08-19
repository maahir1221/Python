class Employees:
    company="Google"
    salary=1000000
    age=23
e1=Employees()
e2=Employees()
e1.salary=300000
e2.salary=400000
print(e1.company)
print(e2.company)
Employees.company="YouTube"
print("Company of Employee 1:", e1.company)
print("Company of Employee 2:", e2.company)
print("Salary of Employee 1:", e1.salary)
print("Salary of Employee 2:", e2.salary)

e1.age=45
print("Age of Employee 1:", e1.age)
print("Age of Employee 2:", e2.age)