class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def something(self):
        print(f"this is about {self.title}")


b1 = Book("harry potter", 1999, "JkR")
b1.something()