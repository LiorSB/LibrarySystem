from Entities.Person import Person


class Student(Person):
    student_id_counter = 0

    def __init__(self, person_id, name, surname, birthdate, courses_taken=None, loaned_books=None):
        Person.__init__(self, person_id, name, surname, birthdate)

        self.courses_taken = [] if courses_taken is None else courses_taken
        self.loaned_books = [] if loaned_books is None else loaned_books

        self.STUDENT_ID = 'Student' + str(Student.student_id_counter)
        Student.student_id_counter += 1

    def get_weekly_hours(self):
        total_weekly_hours = 0

        for course in self.courses_taken:
            total_weekly_hours += course.weekly_hours

        return total_weekly_hours
