headheight = 4
shaftheight = 5
shaftwidth = 1

for i in range(1, headheight + 1):
    stars = "*" * (2 * i - 1)
    spaces = " " * (headheight + shaftwidth - i)
    print(spaces + stars)

for i in range(shaftheight):
    spaces = " " * (headheight + shaftwidth - 1)
    print(spaces + "*" * shaftwidth)