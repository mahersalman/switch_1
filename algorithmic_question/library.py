class book:
    def __init__(self, title, author, genre=None, publication_year=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

class library:
    def __init__(self):
        self.books_by_title = {}
        self.books_by_author = {}

    def add_book(self, book):
        self.books_by_title[book.title] = book
        if book.author not in self.books_by_author:
            self.books_by_author[book.author] = []
        self.books_by_author[book.author].append(book)

    def search_by_title(self, title):
        return self.books_by_title.get(title, None)

    def search_by_author(self, author):
        return self.books_by_author.get(author, [])


# Example usage:
lib = library()
b1 = book("Title1", "Author1", "Genre1", 2001)
b2 = book("Title2", "Author1", "Genre2", 2002)
b3 = book("Title3", "Author2", "Genre3", 2003)

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

a = lib.search_by_title("Title1")
b = lib.search_by_author("Author1")

a.publication_year = 9999999

print(a.publication_year)
print(b[0].publication_year)
#pros : Search by title and author is O(1)-average time complexity
#cons : Memory usage is high

