from Entities.Student import Student
from Entities.Book import Book


class Course:
    course_id_counter = 0

    def __init__(self, course_name, weekly_hours, lecturer=None, signed_students=None, related_books=None):
        self.course_name = course_name
        self.weekly_hours = weekly_hours
        self.lecturer = None if lecturer is None else lecturer
        self.signed_students = [] if signed_students is None else signed_students
        self.related_books = [] if related_books is None else related_books

        self.COURSE_ID = f'{self.course_name}_{Course.course_id_counter}'
        Course.course_id_counter += 1
