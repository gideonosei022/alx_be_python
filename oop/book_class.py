class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    # User-friendly string representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.year}')"
    


 # Uses __str__

book1 = Book("1984", "George Orwell", 1949)
print(book1)  # Output: 1984 by George Orwell, published in 194