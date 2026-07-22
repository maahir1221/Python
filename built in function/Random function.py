import random

a=random.random()
print("random:", a)
a=random.randint(1,100)
print(a)
b=random.randrange(1,101, 20)
print(b)
c=random.choice('computer')
print(c)
c=random.choice([12,23,45,67,65,43])
print(c)
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)
print(numbers)