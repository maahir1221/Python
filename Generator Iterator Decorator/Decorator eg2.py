def make_pretty(fun):
    def inner():
        print("I got decorated")
        fun()
    return inner()
@make_pretty
def ordinary():
    print("I am ordinary")