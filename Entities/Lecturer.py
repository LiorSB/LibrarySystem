from Entities.Person import Person


class Lecturer(Person):
    lecturer_id_counter = 0

    def __init__(self, person_id, name, surname, birthdate, courses_teaching=None, loaned_books=None):
        Person.__init__(self, person_id, name, surname, birthdate)

        self.courses_teaching = [] if courses_teaching is None else courses_teaching
        self.loaned_books = [] if loaned_books is None else loaned_books

        self.LECTURER_ID = 'Lecturer' + str(Lecturer.lecturer_id_counter)
        Lecturer.lecturer_id_counter += 1

    def get_salary(self):
        salary = 0

        for course in self.courses_teaching:
            # A lecturer makes 10$ for each student in a course every hour.
            salary += course.weekly_hours*10*len(course.signed_students)

        return salary

    def get_weekly_hours(self):
        total_weekly_hours = 0

        for course in self.courses_teaching:
            total_weekly_hours += course.weekly_hours

        return total_weekly_hours
