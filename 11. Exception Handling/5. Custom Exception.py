import math
class ValueZeroError(Exception):
    pass
class ValueSmallError(Exception):
    pass
def checkno(n):
    try:
        if n==0:
            raise ValueZeroError("Value is Zero")
        elif n<0:
            raise ValueSmallError("Value is negative")
        else:
            print("Square root of number is:", math.sqrt(n))
    except ValueZeroError as e:
        print(e)
    except ValueSmallError as e:
        print(e)
no=int(input("Enter a number: "))
checkno(no)