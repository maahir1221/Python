# class car:
#     pass
# mycar=car()

# class car:
#     def __init__(self, brand, color):
#         self.brand=brand
#         self.color=color
#
# mycar=car("BMW", "Emerald Green")
# print(mycar.brand)
# print(mycar.color)

# class sum:
#     def __init__(self):
#         self.a = 19
#         self.b = 22
#
#     def show(self):
#         print(self.a + self.b)
#
# y=sum()
# y.show()


class book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def details(self):
        status = "available" if self.available else "not available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

    def borrow(self):
        if self.available:
            self.available = False
            return f"You borrowed {self.title}."
        else:
            return f"sorry, {self.title} is not available."

    def returnbook(self):
        if not self.available:
            self.available = True
            return f"You returned {self.title}."
        else:
            return f"'{self.title}' was not borrowed."

class library:
    def __init__(self):
        self.books=[]

    def addbook (self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def showbooks(self):
        print("\nLibrary Collection:")
        for book in self.books:
            print (book.details())

    def findbook(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

book1=book("Python basics", "Guido van Rossum", "ISBN001")
book2=book("AI Fundamentals", "Andrew Garfield", "ISBN002")
book3=book("Data Science 101", "Maahir Bhavsar", "ISBN003")

library = library()

library.addbook(book1)
library.addbook(book2)
library.addbook(book3)

library.showbooks()

print("\nBorrowing a book:")
print(book2.borrow())

library.showbooks()

print("\nReturning a book:")
print(book2.returnbook())

library.showbooks()