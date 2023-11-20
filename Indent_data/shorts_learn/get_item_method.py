class Book:
    """
    A class representing a book.

    Attributes:
    - content (list): a list of strings representing the pages of the book.

    Methods:
    - __init__(self, content): Initializes a Book instance with the given content.
    - __getitem__(self, index): Retrieves the page at the given index. If the index is out of range, returns 'PAGE not found..!'.
    """

    def __init__(self, content):
        self.content = content

    def __getitem__(self, index):
        try:
            page = self.content[index]
        except IndexError:
            page = 'PAGE not found..!'
        return page

book = Book(['Eggs','Spam','Ham'])
print(book[24])
