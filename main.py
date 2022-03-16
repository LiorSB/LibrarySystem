from Entities.Library import Library
from datetime import date
from GUI.LibraryWindow import LibraryWindow


def main():
    library = Library()

    library.add_librarian('123456789', 'Lior', 'Sabri', date(day=6, month=2, year=1995))
    library.add_librarian('100000000', 'Omri', 'Kellner', date(day=15, month=1, year=1996))

    library.add_lecturer('512345687', 'Nadav', 'Voloch', date(day=22, month=5, year=1948))
    library.add_lecturer('555449871', 'Arik', 'Pizza', date(day=30, month=1, year=1981))
    library.add_lecturer('100054684', 'Moshe', 'Deutch', date(day=22, month=6, year=1972))

    library.add_student('436549871', 'Yosi', 'Bublil', date(day=1, month=6, year=1996))
    library.add_student('363658791', 'Rin', 'Sap', date(day=25, month=7, year=1990))
    library.add_student('846577236', 'Taho', 'Kork', date(day=19, month=1, year=1994))
    library.add_student('458753154', 'Roy', 'Ari', date(day=15, month=12, year=1998))
    library.add_student('123548544', 'Ariel', 'Kir', date(day=6, month=5, year=1991))
    library.add_student('756482125', 'Borno', 'Balil', date(day=10, month=6, year=1989))
    library.add_student('986421412', 'Kebab', 'Bepita', date(day=30, month=10, year=1995))
    library.add_student('450024410', 'Pikachu', 'Cohen', date(day=28, month=4, year=1992))

    library.add_course('Python', 3, library.lecturers[0], library.students[0:2])
    library.add_course('Math', 9, library.lecturers[2], library.students)
    library.add_course('Cyber', 2, library.lecturers[2], library.students[3:])
    library.add_course('Physics', 6, library.lecturers[1], library.students[2:4])
    library.add_course('Lawyers', 10, library.lecturers[1], library.students[5:])
    library.add_course('Sports', 1, library.lecturers[1])

    library.add_book('Narnia', 'John Cena', 15)
    library.add_book('Harry Potter', 'J.K. Rowling', 2, library.courses[0])
    library.add_book('Pokemon Forever', 'Golden Pepe', 1, library.courses[0])
    library.add_book('Math Advanced', 'Donald Duck', 55, library.courses[2])

    library_window = LibraryWindow(library)


if __name__ == "__main__":
    main()
