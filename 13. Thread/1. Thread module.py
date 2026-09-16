import threading
def print_cube(num):
    print("cube: {}" .format(num*num*num))

def print_square(num):
    print("square: {}" .format(num*num))

if __name__ == "__main__":
    t1=threading.Thread(target=print_square, args=(10,))
    t2=threading.Thread(target=print_cube, args=(10,))

t1.start() #This will start thread 1
t2.start() #This will start thread 2

t1.join()
t2.join()

print("Done")