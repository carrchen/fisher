
class BookViewModel:

    @classmethod
    def package_single(cls, keyword, data):

        returned = {
            'books': [],
            'total': 0,
            'keyword': ''
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls._cut_book_data(data)]
            returned['keyword'] = keyword
        return returned

    @classmethod
    def package_collection(cls, keyword, data):
        returned = {
            'books': [],
            'total': 0,
            'keyword': ''
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls._cut_book_data(book) for book in data['books']]
            returned['keyword'] = keyword
        return returned

    @classmethod
    def _cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book

