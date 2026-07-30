a={'apple', 'banana', 'cherry', 'apple'}
print(a)
tropical={'pineapple', 'mango', 'papaya'}
a.update(tropical)
print(a)

# unlike using append for list, we can't use append here, instead we have update.
# here's the syntax for update: variable.update(variable2)