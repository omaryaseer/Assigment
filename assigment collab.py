class Library:
    def __init__(self, booklist, name, lended_books={}):
        # Assuming that 'booklist' are all the books that belong to the library, whether they were borrowed or not.
        self.booklist = booklist
        self.name = name
        self.lended_books = lended_books

    def display_available(self):
        if len(self.booklist) > 0:
            for i in self.booklist:
                if i not in self.lended_books:
                    print(i)
        else:
            print("There are no books available at the moment.")

    def lend_book(self, book, client):
        if book not in self.lended_books:
            if book in self.booklist:
                self.lended_books[client] = book

            else:
                print("This book is not in the library.")

    def return_lended(self, book):
        if book in self.lended_books:
            self.lended_books.remove(book)
        else:
            print("The book has not been borrowed by anyone.")

    def add_book(self, book):
        self.booklist.append(book)


Harry = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")
Harry.add_book('harry potter dar knight prince')
print(Harry.booklist)
