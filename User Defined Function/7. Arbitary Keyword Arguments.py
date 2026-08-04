def arbitraryKeywordArgument(**kid):
    print("His last name is "+ kid["Lastname"])
    for i in kid:
        print("Your", i, "is", kid[i])

print("Arbitrary Keyword Argument")
arbitraryKeywordArgument(firstname="Tobias", Lastname="Refsnes")
