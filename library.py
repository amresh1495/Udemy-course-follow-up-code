# class => Library
# Layers of abstraction => display available books, lend a book and add a book

# class => Customer
# Layers of abstraction => request book and return a book


class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAavailableBooks(self):
        print ('')
        print ('Aavailable Books : ')
        for book in self.availableBooks:
            print (book)
        print ('')

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print ("You have now borrowed the book !")
            self.availableBooks.remove(requestedBook)
        else:
            print ("Sorry, the book is not present in the library")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print ("Thank you, now you have returned the book")

class Customer:

    def requestBook(self):
        print ("Enter the name of book that you want to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print ("Enter the name of book that you returned : ")
        self.book = input()
        return self.book

library = Library(['Think and Grow Rich', 'Who Will Cry When You Die', 'Elon Musk Biography'])
customer = Customer()

# creating menu for the user
while True:
    print ("Enter 1 to display the available books")
    print ("Enter 2 to request for a book")
    print ("Enter 3 to return a book")
    print ("Enter 4 to exit")

    userChoice = int(input())
    if userChoice is 1:
        library.displayAavailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()
