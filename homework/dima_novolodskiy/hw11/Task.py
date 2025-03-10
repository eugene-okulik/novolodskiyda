class Book:

    page_material = 'paper'
    has_text = True


    def __init__(self, book_title, book_author, page_count, isbn, is_reserved):
        self.book_title = book_title
        self.book_author = book_author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = is_reserved

    def __print_book_info__(self):
        base_info = (f'Название: {self.book_title}, Автор: {self.book_author}, '
                     f'страниц: {self.page_count}, материал: {self.page_material}')
        if self.is_reserved:
            return print(base_info + ', зарезервирована')
        return print(base_info)


class ShoolBook(Book):

    def __init__(self, book_title, book_author, page_count, isbn, is_reserved, subject, school_grade, has_exercises):
        super().__init__(book_title, book_author, page_count, isbn, is_reserved)
        self.subject = subject
        self.school_grade = school_grade
        self.has_exercises = has_exercises

    def __print_schoolbook_info__(self):
        base_info = (f'Название: {self.book_title}, Автор: {self.book_author}, '
                     f'страниц: {self.page_count}, предмет: {self.subject}, класс: {self.school_grade}')
        if self.is_reserved:
            return print(base_info + ', зарезервирована')
        return print(base_info)



book_1 = Book(
    book_title = 'Идиот',
    book_author = 'Воронов А.С.',
    page_count = 112,
    isbn = '978695457439',
    is_reserved = False
)

book_2 = Book(
    book_title = 'Война и мир',
    book_author = 'Оставьев С.А.',
    page_count = 134,
    isbn = '978733845776',
    is_reserved = False
)

book_3 = Book(
    book_title = 'Лукоморье',
    book_author = 'Островский Ю.В.',
    page_count = 176,
    isbn = '978020054560',
    is_reserved = False
)

book_4 = Book(
    book_title = 'Онегин',
    book_author = 'Бортич Д.В.',
    page_count = 98,
    isbn = '978842590848',
    is_reserved = False
)

book_5 = Book(
    book_title = 'Золотая рыбка',
    book_author = 'Аронов Г.И.',
    page_count = 110,
    isbn = '978559447321',
    is_reserved = False
)

book_5.is_reserved = True

list_books = [book_1, book_2, book_3, book_4, book_5]
for book in list_books:
    book.__print_book_info__()

schoolbook_1 = ShoolBook(
    book_title = 'Алгебра',
    book_author = 'Титов А.С.',
    page_count = 132,
    isbn = '978877662466',
    is_reserved = False,
    subject = 'Математика',
    school_grade = '9',
    has_exercises = True
)

schoolbook_2 = ShoolBook(
    book_title = 'Русский',
    book_author = 'Осипов А.С.',
    page_count = 102,
    isbn = '978999339813',
    is_reserved = False,
    subject = 'Русский язык',
    school_grade = '11',
    has_exercises = True
)

schoolbook_3 = ShoolBook(
    book_title = 'Зарубежная литература',
    book_author = 'Бурский А.С.',
    page_count = 304,
    isbn = '978395866557',
    is_reserved = False,
    subject = 'Литература',
    school_grade = '10',
    has_exercises = False
)

schoolbook_2.is_reserved = True

list_schoolbooks = [schoolbook_1, schoolbook_2, schoolbook_3]
for book in list_schoolbooks:
    book.__print_schoolbook_info__()
