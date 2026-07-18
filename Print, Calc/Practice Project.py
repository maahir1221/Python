# a=int(input("Physics: "))
# b=int(input("Chemistry: "))
# c=int(input("Maths: "))
# d=int(input("English: "))
# e=int(input("Painting: "))
# f=(a+b+c+d+e)/5
# if a<33 or b<33 or c<33 or d<33 or e <33:
#     print("failed")
#     exit()
# if a>=33 or b>=33 or c>=33 or d>=33 or e >=33:
#  if f>=90:
#     print("Grade A")
#  elif f>=75:
#     print("Grade B")
#  elif f>=50:
#     print("Grade C")
#  else:
#     print("Failed")


# age=int(input("Enter your age: "))
# if age < 18:
#     print("Too Young")
#     exit()
# dl=input("Have you passed your driving test? (Yes/No): ")
# ID=input("Do you have ID proof? (Yes/No): ")
# if age>=18 and ID=="Yes" and dl=="Yes":
#     print("You will receive your DL soon")
# elif age>=18 and ID=="No" or dl=="No":
#     print("Please complete your Driving Test or Attach ID proof")


# x=5
# y=8
# z=int(input("Units consumed: "))
# if z<=100:
#     g=z*x
#     print("Your total electricity bill is:", g)
# elif 300>=z>100:
#     b=(100*5)+8*(z-100)
#     print("Your total electricity bill is:", b)
# elif z>300:
#     bill=(100*5)+(8*200)+10*(z-300)
#     print("Your total electricity bill is:", bill)


n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
print("\nCalculations available:")
print("1. Add numbers")
print("2. Subtract numbers")
print("3. Multiply numbers")
print("4. Divide  numbers")

print("5. Exit")
num=int(input("Enter your choice (1-5): "))
if num==1:
    z=n1+n2
    print("Sum of numbers is: ", z )
elif num==2:
    x=n1-n2
    print("Difference of numbers is: ", x )
elif num==3:
    y=n1*n2
    print("Product of numbers is: ", y )
elif num==4:
    if n2 == 0:
        print("Error dividend can't be zero")
        exit()
    else:
         m=n1/n2
    print("Division of numbers is: ",m)

elif num==5:
    print("Thanks for visiting")