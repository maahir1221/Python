try:
    a=float(input("Enter value of a: "))
    b=float(input("Enter value of b: "))
    c=a/b
except ZeroDivisionError:
    print("Division by zero is not possible")
except Exception as e:
    print(e)
else:
    print("Div =", c)
finally:
    print("Division completed successfully")