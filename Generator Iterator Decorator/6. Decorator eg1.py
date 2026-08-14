def make_pretty(fun):
    def inner():
        print("I got decorated")
        fun()
    return inner()
def ordinary():
    print("I am ordinary")
ordinary()
pretty=make_pretty(ordinary)