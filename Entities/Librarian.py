from Entities.Person import Person


class Librarian(Person):
    librarian_id_counter = 0

    def __init__(self, person_id, name, surname, birthdate):
        Person.__init__(self, person_id, name, surname, birthdate)
        self.LIBRARIAN_ID = 'Librarian' + str(Librarian.librarian_id_counter)
        Librarian.librarian_id_counter += 1
