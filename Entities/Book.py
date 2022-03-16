class Book:
    book_id_counter = 0

    def __init__(self, title, author, number_of_copies, related_course=None):
        self.title = title
        self.author = author
        self.number_of_copies = number_of_copies
        self.related_course = related_course

        self.BOOK_ID = f'{self.title}_{self.author}_{Book.book_id_counter}'
        Book.book_id_counter += 1
