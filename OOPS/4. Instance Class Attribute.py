class employee:
    company="Google"
    salary=10000
mahesh=employee()
ramesh=employee()

mahesh.salary=20000
ramesh.salary=15000

print(mahesh.salary)
print(ramesh.salary)

print(ramesh.address)
# The above line shows error because address is not present in instance/class