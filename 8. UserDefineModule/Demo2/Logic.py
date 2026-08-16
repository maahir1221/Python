hheight = 4
height = 5
width = 1

for i in range(1, hheight + 1):
    stars = "*" * (2 * i - 1)
    spaces = " " * (hheight + width - i)
    print(spaces + stars)

for i in range(height):
    spaces = " " * (hheight + width - 1)
    print(spaces + "*" * width)