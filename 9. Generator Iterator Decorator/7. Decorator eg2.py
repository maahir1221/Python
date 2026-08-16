def make_pretty(fun):
    def inner():
        print("I got decorated")
        fun()
    return inner()
# @make_pretty
def ordinary():
    print("I am ordinary")

print(make_pretty(ordinary))

# You can either use @function to call it or call it normally
# @FUNCTION IS COMMNETED above, if you want to use it than comment line 10 or else there will be an error