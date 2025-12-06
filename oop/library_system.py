class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __del__(self):
        print(f"Deleting {self.title}")

    # User-friendly string representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"

    # Official representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.publication_year}')"
    





class EBook(Book):
   def __init__(self, title, author, publication_year, file_size):
      super().__init__(title, author, publication_year)
      self.file_size = file_size


def __str__(self):
   return f"{self.title} by {self.author} (E-Book, {self.file_size}MB)"




class PrintBook(Book):
   def __init__(self, title, author, publication_year, page_count):
      super().__init__(title, author, publication_year)
      self.page_count = page_count


def __str__(self):
   return f"{self.title} by {self.author} (Print Book, {self.page_count} pages)"




class Library:
   def __init__(self):
      self.books = []


def add_book(self, book):
   self.books.append(book)


def list_books(self):
   for book in self.books:
      print(book)    