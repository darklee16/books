class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '<Book: {} by {}>'.format(self.title, self.author)

class TextBook(Book):
    def __init__(self, title, author, edition):
        super().__init__(title, author)
        self.edition = edition

book = Book(title='All the light', author='some person')
textbook = TextBook(title='Physics', author='Physics auther', edition ='5')
print(textbook)
print(book)
