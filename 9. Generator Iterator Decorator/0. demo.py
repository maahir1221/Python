l=[3,4]
data=iter(l)
print(next(data))
print(next(data))
print(next(data))

def show():
    yield 1
    yield 2
data=show()
print(next(data))
print(next(data))