name= input("Enter Your Name:")
gender= input("Enter Your Gender:")
DOB= input("Enter Your DOB:")
age= int(input("Enter Your Age:"))
address=input("Enter Your Address:")
state=input("Enter Your State:")
p=float(input("Marks Obtained in Physics:"))
c=float(input("Marks Obtained in Chemistry:"))
m=float(input("Marks Obtained in Maths:"))
e=float(input("Marks Obtained in English:"))
painting=float(input("Marks Obtained in Painting:"))
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBIO DATA")
print("\n\nName:", name, "\t\t\t\t\t\t\t\t\t\tGender:", gender)
print("Date of Birth:", DOB, "\t\t\t\t\t\t\tAge:", age)
print("Address:", address, "\t\t\tState:", state)

print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEDUCATIONAL QUALIFICATION")
print("\nClass 12th Result")
print("\nSubject\t\t\t\t\t", "Marks Obtained")
print("\nPhysics\t\t\t\t\t\t", p)
print("Chemistry\t\t\t\t\t", c)
print("Maths\t\t\t\t\t\t", m)
print("English\t\t\t\t\t\t", e)
print("Painting\t\t\t\t\t", painting)
a, b, c, d, e, f = p, c, m, e, painting, p+c+m+e+painting
print("\n\nTotal\t\t\t\t\t\t", f)
print("Percentage\t\t\t\t\t", f/5, "%")
Percentage= f/5
if Percentage >=90:
    print("grade:\t\t\t\t\t\t" "A")
elif Percentage >=80:
    print("grade:\t\t\t\t\t\t" "B")
elif Percentage >=60:
    print("grade:\t\t\t\t\t\t" "C")
else:
    print("Failed")