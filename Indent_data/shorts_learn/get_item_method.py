class Book:
    def __init__(self,content):
        self.content = content

    def __getitem__(self, index):
        try:
            page = self.content[index]
        except IndexError:
            page = 'PAGE not found..!'
        return page
    
book = Book(['Eggs','Spam','Ham'])
print(book[24])
