def function(**std):
    print(std)
    print(type(std))
    if std is not None:
        for key, value in std.items():
            print("%s=%s"%(key,value))
function(fn='Abc', In='Def', name='Yash', demo='Hemil')