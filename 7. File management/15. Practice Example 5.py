with open('sample.txt','w') as f:
    f.write("Donkey")
with open('sample.txt','r') as f:
    x=f.read()
x=x.replace('Donkey', '#######')
print(x)
with open('sample.txt', 'w') as f:
    f.write(x)
