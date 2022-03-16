from Entities.Book import Book
from Entities.Course import Course
from Entities.Student import Student
from Entities.Lecturer import Lecturer
from Entities.Librarian import Librarian
from Entities.BookLoanRecord import BookLoanRecord
from datetime import date


class Library:
    def __init__(self, librarians=None, lecturers=None, students=None, books=None, courses=None):
        self.librarians = [] if librarians is None else librarians
        self.lecturers = [] if lecturers is None else lecturers
        self.students = [] if students is None else students
        self.books = [] if books is None else books
        self.courses = [] if courses is None else courses

    """
    Addition Functions.
    An add function for each on the entities in library.
    """

    def add_librarian(self, person_id, name, surname, birthdate):
        librarian = Librarian(person_id, name, surname, birthdate)
        self.librarians.append(librarian)

        return librarian.LIBRARIAN_ID

    def add_lecturer(self, person_id, name, surname, birthdate, courses_teaching=None):
        lecturer = Lecturer(person_id, name, surname, birthdate, courses_teaching)
        self.lecturers.append(lecturer)

        # In case the new lecturer is teaching a course, tie the course to the lecturer.
        if courses_teaching is not None:
            for course in courses_teaching:
                course.lecturer = lecturer

        return lecturer.LECTURER_ID

    def add_student(self, person_id, name, surname, birthdate, courses_taken=None):
        student = Student(person_id, name, surname, birthdate, courses_taken)
        self.students.append(student)

        # In case the new student is taking a course, tie the course to the student.
        if courses_taken is not None:
            for course in courses_taken:
                course.signed_students.append(student)

        return student.STUDENT_ID

    def add_book(self, title, author, number_of_copies=0, related_course=None):
        book = Book(title, author, number_of_copies, related_course)
        self.books.append(book)

        # In case the new book is has a subject, tie the course to the book.
        if related_course is not None:
            related_course.related_books.append(book)

        return book.BOOK_ID

    def add_course(self, course_name, weekly_hours, lecturer=None, signed_students=None, related_books=None):
        course = Course(course_name, weekly_hours, lecturer, signed_students, related_books)
        self.courses.append(course)

        # In case the new course has a lecturer, tie the lecturer to the course.
        if lecturer is not None:
            lecturer.courses_teaching.append(course)

        # In case the new course has a student, tie the lecturer to the student.
        if signed_students is not None:
            for student in signed_students:
                student.courses_taken.append(course)

        # In case the new course has a book, tie the lecturer to the book.
        if related_books is not None:
            related_books.related_course = course

        return course.COURSE_ID

    """
    Search Functions.
    A search function for each of the entities in library, they receive an ID and return an object.
    """

    def search_librarian_id(self, librarian_id):
        for librarian in self.librarians:
            if librarian.LIBRARIAN_ID == librarian_id:
                return librarian

        return None

    def search_lecturer_id(self, lecturer_id):
        for lecturer in self.lecturers:
            if lecturer.LECTURER_ID == lecturer_id:
                return lecturer

        return None

    def search_student_id(self, student_id):
        for student in self.students:
            if student.STUDENT_ID == student_id:
                return student

        return None

    def search_course_id(self, course_id):
        for course in self.courses:
            if course.COURSE_ID == course_id:
                return course

        return None

    def search_book_id(self, book_id):
        for book in self.books:
            if book.BOOK_ID == book_id:
                return book

        return None

    """
    Get info which answer the GUI Info frames.
    """

    def get_lecturer_salary(self, lecturer_id):
        lecturer = self.search_lecturer_id(lecturer_id)

        if lecturer is None:
            return None

        return lecturer.get_salary()

    def get_lecturer_courses(self, lecturer_id):
        lecturer = self.search_lecturer_id(lecturer_id)

        if lecturer is None:
            return None

        return lecturer.courses_teaching

    def get_student_courses(self, student_id):
        student = self.search_student_id(student_id)

        if student is None:
            return None

        return student.courses_taken

    def get_lecturer_weekly_hours(self, lecturer_id):
        lecturer = self.search_lecturer_id(lecturer_id)

        if lecturer is None:
            return None

        return lecturer.get_weekly_hours()

    def get_student_weekly_hours(self, student_id):
        student = self.search_student_id(student_id)

        if student is None:
            return None

        return student.get_weekly_hours()

    """
    Manage functions which answer the GUI Manage frames.
    """

    def edit_course(self, course_id, lecturer_id, weekly_hours):
        course = self.search_course_id(course_id)
        lecturer = self.search_lecturer_id(lecturer_id)

        if not course or not lecturer:
            return None

        previous_lecturer = course.lecturer
        previous_lecturer.courses_teaching.remove(course)

        lecturer.courses_teaching.append(course)

        course.lecturer = lecturer
        course.weekly_hours = weekly_hours

    def edit_book(self, book_id, course_id, number_of_copies):
        book = self.search_book_id(book_id)
        course = self.search_course_id(course_id)

        if not book or not course:
            return None

        previous_related_course = book.related_course
        previous_related_course.related_books.remove(book)

        course.related_books.append(book)

        book.related_course = course
        book.number_of_copies = number_of_copies

    def sign_user_to_courses(self, user_id, user_type, courses):
        if user_type == 'Lecturer':
            user = self.search_lecturer_id(user_id)

            for course in courses:
                course.lecturer = user
                user.courses_teaching.append(course)
        else:
            user = self.search_student_id(user_id)

            for course in courses:
                course.signed_students.append(user)
                user.courses_taken.append(course)

    def lend_book(self, book_id, user_id, user_type, loan_end_date):
        book = self.search_book_id(book_id)

        if book.number_of_copies <= 0:
            return False

        if user_type == 'Lecturer':
            user = self.search_lecturer_id(user_id)
        else:
            user = self.search_student_id(user_id)

        loan_start_date = date.today()
        book_loan_record = BookLoanRecord(book, loan_start_date, loan_end_date)

        user.loaned_books.append(book_loan_record)
        book.number_of_copies -= 1

        return True

    def return_book(self, book_id, user_id, user_type):
        if user_type == 'Lecturer':
            user = self.search_lecturer_id(user_id)
        else:
            user = self.search_student_id(user_id)

        book_record = None

        for loaned_book in user.loaned_books:
            if loaned_book.book.BOOK_ID == book_id:
                book_record = loaned_book
                break

        if book_record is None:
            return None

        user.loaned_books.remove(book_record)
        book_record.book.number_of_copies += 1

        current_date = date.today()
        days_late = (current_date - book_record.loan_end_date).days

        return 0 if days_late <= 0 else days_late
