class book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __del__(self):
        print(f"Deleting {self.title}")

    # User-friendly string representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"