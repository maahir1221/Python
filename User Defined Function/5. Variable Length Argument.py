def function(arg1, *tuplevar):
    print('arg1=', arg1)
    print(type(arg1))
    print(type(tuplevar))
    print(tuplevar)
# function(50)
function(("String", 70), "Hello", "Disha", "Rushika", "Smit")