headheight = 4
height = 5
width = 1

for i in range(1, headheight + 1):
    stars = "*" * (2 * i - 1)
    spaces = " " * (headheight + width - i)
    print(spaces + stars)

for i in range(height):
    spaces = " " * (headheight + width - 1)
    print(spaces + "*" * width)