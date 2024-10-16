class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self) -> str:
        return f"{self.title} {self.author}"



class EBook(Book):
    def __init__(self, title, author, file_Size: int):
        super().__init__(title, author)
        self.file_size = file_Size
    

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        return self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(f"{book.__class__.__name__}: {book}")
    