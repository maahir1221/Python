import re

text="Hello, I am Maahir, and this 8997324 209348 is 1203845 a 3425 test"
words= re.findall(r'[A-Za-z]+', text)
print("Words found:", words)
