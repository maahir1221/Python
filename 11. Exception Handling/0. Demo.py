try:
    a=10
    b=0
    c=a/b
except Exception as e:
    print(e)
finally:
    print("hello")