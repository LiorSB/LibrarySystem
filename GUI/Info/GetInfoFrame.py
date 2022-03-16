import tkinter as tk
from PIL import Image, ImageTk


class GetInfoFrame(tk.Frame):
    def __init__(self, parent, controller, library):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.library = library

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Info.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(self, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        # Get Users
        get_users_button = tk.Button(self, text='Get All Users', command=lambda: self.popup_message('Get Users'))
        get_users_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                background='AntiqueWhite4')
        get_users_button.pack(side='top', pady=(50, 0))

        # Get Courses
        get_courses_button = tk.Button(self, text='Get All Courses', command=lambda: self.popup_message('Get Courses'))
        get_courses_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                  background='AntiqueWhite4')
        get_courses_button.pack(pady=(10, 0))

        # Get Books
        get_books_button = tk.Button(self, text='Get All Books', command=lambda : self.popup_message('Get Books'))
        get_books_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                background='AntiqueWhite4')
        get_books_button.pack(pady=(10, 0))

        # Get Lecturer Salary
        get_lecturer_salary_button = tk.Button(self, text='Get Lecturer Salary',
                                               command=lambda: controller.show_frame('GetLecturerSalaryFrame'))
        get_lecturer_salary_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                          background='AntiqueWhite4')
        get_lecturer_salary_button.pack(pady=(10, 0))

        # Get Users Courses
        get_users_courses_button = tk.Button(self, text='Get Users Courses',
                                             command=lambda: controller.show_frame('GetUsersCoursesFrame'))
        get_users_courses_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                        background='AntiqueWhite4')
        get_users_courses_button.pack(pady=(10, 0))

        # Return to Hub
        return_to_hub_button = tk.Button(self, text='Return to Hub', width='30', height='1',
                                         command=lambda: controller.show_frame('LibraryHubFrame'))
        return_to_hub_button.config(font=('Arial', 20, 'bold'), width='12', borderwidth=3, relief="raised",
                                    background='IndianRed1')
        return_to_hub_button.pack(pady=(100, 0))

    def set_toplevel_to_center_of_window(self, top_level):
        top_level.update_idletasks()

        main_window_position_x = self.controller.winfo_x()
        main_window_position_y = self.controller.winfo_y()

        main_window_width = self.controller.winfo_width() / 2
        main_window_height = self.controller.winfo_height() / 2

        popup_width = top_level.winfo_width() / 2
        popup_height = top_level.winfo_height() / 2

        position_right = main_window_width - popup_width
        position_down = main_window_height - popup_height

        top_level.geometry('+%d+%d' % (main_window_position_x + position_right, main_window_position_y + position_down))

    def popup_message(self, button_clicked):
        popup = tk.Toplevel(self.controller)
        popup.config(background='AntiqueWhite4')

        match button_clicked:
            case 'Get Users':
                popup.title('All Users')
                self.get_all_users(popup)
            case 'Get Courses':
                popup.title('All Courses')
                self.get_all_courses(popup)
            case 'Get Books':
                popup.title('All Books')
                self.get_all_books(popup)

        self.set_toplevel_to_center_of_window(popup)

    def get_all_users(self, window):
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        window.grid_columnconfigure(2, weight=1)

        i = 0

        librarian_label = tk.Label(window, text='Librarians:')
        librarian_label.config(font=('Arial', 14, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        librarian_label.grid(row=i, columnspan=3, pady=(10, 5))

        for librarian in self.library.librarians:
            i += 1

            # Librarian ID
            id_label = tk.Label(window, text=f'ID: {librarian.LIBRARIAN_ID}')
            id_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                            background='AntiqueWhite3')
            id_label.grid(row=i, column=0, pady=(0, 5))

            # Librarian Name
            name_label = tk.Label(window, text=f'Full Name: {librarian.name} {librarian.surname}')
            name_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                              background='AntiqueWhite3')
            name_label.grid(row=i, column=1, pady=(0, 5))

            # Librarian Birthdate
            birthdate_label = tk.Label(window, text=f'Birthdate: {librarian.birthdate}')
            birthdate_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                   background='AntiqueWhite3')
            birthdate_label.grid(row=i, column=2, pady=(0, 5))

        i += 1

        lecturer_label = tk.Label(window, text='Lecturers:')
        lecturer_label.config(font=('Arial', 14, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        lecturer_label.grid(row=i, columnspan=3, pady=(10, 5))

        for lecturer in self.library.lecturers:
            i += 1

            # Lecturer ID
            id_label = tk.Label(window, text=f'ID: {lecturer.LECTURER_ID}')
            id_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                            background='AntiqueWhite3')
            id_label.grid(row=i, column=0, pady=(0, 5))

            # Lecturer Name
            name_label = tk.Label(window, text=f'Full Name: {lecturer.name} {lecturer.surname}')
            name_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                              background='AntiqueWhite3')
            name_label.grid(row=i, column=1, pady=(0, 5))

            # Lecturer Birthdate
            birthdate_label = tk.Label(window, text=f'Birthdate: {lecturer.birthdate}')
            birthdate_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                   background='AntiqueWhite3')
            birthdate_label.grid(row=i, column=2, pady=(0, 5))

        i += 1

        student_label = tk.Label(window, text='Students:')
        student_label.config(font=('Arial', 14, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        student_label.grid(row=i, columnspan=3, pady=(10, 5))

        for student in self.library.students:
            i += 1

            # Student ID
            id_label = tk.Label(window, text=f'ID: {student.STUDENT_ID}')
            id_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                            background='AntiqueWhite3')
            id_label.grid(row=i, column=0, pady=(0, 5))

            # Student Name
            name_label = tk.Label(window, text=f'Full Name: {student.name} {student.surname}')
            name_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                              background='AntiqueWhite3')
            name_label.grid(row=i, column=1, pady=(0, 5))

            # Student Birthdate
            birthdate_label = tk.Label(window, text=f'Birthdate: {student.birthdate}')
            birthdate_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                   background='AntiqueWhite3')
            birthdate_label.grid(row=i, column=2, pady=(0, 5))

    def get_all_courses(self, window):
        # Get lecturers and then use "set" to cancel out duplicates in case a lecturer teaches several courses.
        lecturers = [course.lecturer for course in self.library.courses]
        unique_lecturers = set(lecturers)

        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        window.grid_columnconfigure(2, weight=1)

        i = 0

        course_label = tk.Label(window, text='Courses:')
        course_label.config(font=('Arial', 22, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        course_label.grid(row=i, columnspan=3, pady=(10, 5))

        for lecturer in unique_lecturers:
            i += 1

            if lecturer is None:
                lecturer_label = tk.Label(window, text='Lectured by nobody:')
            else:
                lecturer_label = tk.Label(window, text=f'Lectured by {lecturer.name} {lecturer.surname}:')

            lecturer_label.config(font=('Arial', 14, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
            lecturer_label.grid(row=i, columnspan=3, pady=(10, 5))

            # Run through the courses that each lecturer teaches or courses that don't have a lecturer.
            for course in self.library.courses:
                if course.lecturer == lecturer:
                    i += 1

                    # Course ID
                    id_label = tk.Label(window, text=f'Course ID: {course.COURSE_ID}')
                    id_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                    background='AntiqueWhite3')
                    id_label.grid(row=i, column=0, pady=(0, 5))

                    # Course Name
                    name_label = tk.Label(window, text=f'Course Name: {course.course_name}')
                    name_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                      background='AntiqueWhite3')
                    name_label.grid(row=i, column=1, pady=(0, 5))

                    # Course Weekly Hours
                    weekly_hours_label = tk.Label(window, text=f'Weekly Hours: {course.weekly_hours}')
                    weekly_hours_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                              background='AntiqueWhite3')
                    weekly_hours_label.grid(row=i, column=2, pady=(0, 5))

    def get_all_books(self, window):
        courses = [book.related_course for book in self.library.books]
        unique_courses = set(courses)

        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        window.grid_columnconfigure(2, weight=1)
        window.grid_columnconfigure(3, weight=1)

        i = 0

        book_label = tk.Label(window, text='Books:')
        book_label.config(font=('Arial', 22, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        book_label.grid(row=i, columnspan=4, pady=(10, 5))

        for course in unique_courses:
            i += 1

            if course is None:
                course_label = tk.Label(window, text='None Course Books:')
            else:
                course_label = tk.Label(window, text=f'{course.course_name} Course Books:')

            course_label.config(font=('Arial', 14, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
            course_label.grid(row=i, columnspan=4, pady=(10, 5))

            for book in self.library.books:
                if book.related_course == course:
                    i += 1

                    # Book ID
                    id_label = tk.Label(window, text=f'Book ID: {book.BOOK_ID}')
                    id_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=40,
                                    background='AntiqueWhite3')
                    id_label.grid(row=i, column=0, pady=(0, 5))

                    # Book Label
                    title_label = tk.Label(window, text=f'Title: {book.title}')
                    title_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=40,
                                       background='AntiqueWhite3')
                    title_label.grid(row=i, column=1, pady=(0, 5))

                    # Book Author
                    author_label = tk.Label(window, text=f'Author: {book.author}')
                    author_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=40,
                                        background='AntiqueWhite3')
                    author_label.grid(row=i, column=2, pady=(0, 5))

                    # Book Number of Copies
                    number_of_copies_label = tk.Label(window, text=f'Number of Copies: {book.number_of_copies}')
                    number_of_copies_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=40,
                                                  background='AntiqueWhite3')
                    number_of_copies_label.grid(row=i, column=3, pady=(0, 5))
