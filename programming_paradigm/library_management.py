class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_a_book_out(self):
        if self.title and self._is_checked_out == False:
            self._is_checked_out = True
            return self._is_checked_out
        
        
    def return_book(self):
        if self.title and self._is_checked_out == True:
            self._is_checked_out = False
            return self._is_checked_out
        
    def __repr__(self):
        return f"title: {self.title} author: {self.author}"


class Library():
    def __init__(self):
        self._books = []
        self._unavaliable_books = []
    
    def add_book(self, book):
        self._books.append(book)
        return self._books
    
    def check_out_book(self, title):
        if self._books:
            for bk_idx in range(len(self._books)):
                if self._books[bk_idx].title == title:
                    print(self._books[bk_idx]._is_checked_out) 
                    self._books[bk_idx].check_a_book_out()
                    # Remove book from list
                    book_pop = self._books.pop(bk_idx)
                    # move books to unavialable list
                    self._unavaliable_books.append(book_pop)
                         
    def return_book(self, title):
        if self._unavaliable_books:
            for bk_idx in range(len(self._unavaliable_books)):
                if self._unavaliable_books[bk_idx].title == title:
                    self._unavaliable_books[bk_idx].return_book()
                    book_pop = self._unavaliable_books.pop(bk_idx)

                    # Adding book back thus making it avaliable
                    self._books.append(book_pop)
                    
    def list_available_books(self):
        for book in self._books:
            print(book)
            


