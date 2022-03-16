import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import datetime


class AddUserFrame(tk.Frame):
    def __init__(self, parent, controller, library):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.library = library

        container = tk.Frame(self)
        container.pack(expand=True, fill="both", side="top")

        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)
        container.grid_rowconfigure(2, weight=1)
        container.grid_rowconfigure(3, weight=1)
        container.grid_rowconfigure(4, weight=1)
        container.grid_rowconfigure(5, weight=1)
        container.grid_rowconfigure(6, weight=1)
        container.grid_rowconfigure(7, weight=1)
        container.grid_rowconfigure(8, weight=1)

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)
        container.grid_columnconfigure(3, weight=1)

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Book.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(container, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        id_vcmd = (self.register(self.id_validate), '%P')
        name_vcmd = (self.register(self.name_validate), '%P')
        surname_vcmd = (self.register(self.surname_validate), '%P')

        # Radio buttons for student or lecturer
        student_lecturer_label = tk.Label(container, text='New User to Create:')
        student_lecturer_label.config(font=('Arial', 35, 'bold'), borderwidth=3, relief="ridge",
                                      background='AntiqueWhite3')
        student_lecturer_label.grid(row=0, columnspan=4, pady=(50, 0))

        self.selected_user = tk.IntVar()

        student_radio_button = tk.Radiobutton(container, text='Student', variable=self.selected_user, value=0)
        student_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=8,
                                    background='AntiqueWhite3')
        student_radio_button.grid(row=1, column=0, columnspan=2, padx=(100, 0), pady=(10, 0))

        lecturer_radio_button = tk.Radiobutton(container, text='Lecturer', variable=self.selected_user, value=1)
        lecturer_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=8,
                                     background='AntiqueWhite3')
        lecturer_radio_button.grid(row=1, column=2, columnspan=2, padx=(10, 0), pady=(10, 0))

        # ID fields
        self.person_id = tk.StringVar()

        id_label = tk.Label(container, text='ID:')
        id_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8, background='AntiqueWhite3')
        id_label.grid(row=2, column=0, columnspan=2, padx=(100, 0), pady=(10, 0))

        self.id_entry = tk.Entry(container, textvariable=self.person_id, validate='key', validatecommand=id_vcmd)
        self.id_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=18,
                             background='AntiqueWhite3')
        self.id_entry.grid(row=2, column=2, columnspan=2, padx=(0, 100), pady=(10, 0))

        # Name fields
        self.name = tk.StringVar()

        name_label = tk.Label(container, text='Name:')
        name_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8, background='AntiqueWhite3')
        name_label.grid(row=3, column=0, columnspan=2, padx=(100, 0), pady=(10, 0))

        self.name_entry = tk.Entry(container, textvariable=self.name, validate='key', validatecommand=name_vcmd)
        self.name_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=18,
                               background='AntiqueWhite3')
        self.name_entry.grid(row=3, column=2, columnspan=2, padx=(0, 100), pady=(10, 0))

        # Surname fields
        self.surname = tk.StringVar()

        surname_label = tk.Label(container, text='Surname:')
        surname_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8,
                             background='AntiqueWhite3')
        surname_label.grid(row=4, column=0, columnspan=2, padx=(100, 0), pady=(10, 0))

        self.surname_entry = tk.Entry(container, textvariable=self.surname, validate='key', validatecommand=surname_vcmd)
        self.surname_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=18,
                                  background='AntiqueWhite3')
        self.surname_entry.grid(row=4, column=2, columnspan=2, padx=(0, 100), pady=(10, 0))

        # Birthdate fields
        birthdate_label = tk.Label(container, text='Birthdate:')
        birthdate_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8,
                               background='AntiqueWhite3')
        birthdate_label.grid(row=5, column=0, columnspan=2, padx=(100, 0), pady=(10, 0))

        # Max age 21 years, leap years weren't taken into consideration.
        self.max_birthdate = datetime.date.today() - datetime.timedelta(days=365*21)

        self.date_entry = DateEntry(container, date_pattern='dd/mm/yyyy', maxdate=self.max_birthdate)
        self.date_entry.config(width=36, background='AntiqueWhite4')
        self.date_entry.grid(row=5, column=2, columnspan=2, padx=(0, 100), pady=(10, 0))

        # Sign to course button
        self.selected_courses = None

        sign_to_courses_button = tk.Button(container, text='Sign to Courses', command=self.sign_to_courses)
        sign_to_courses_button.config(font=('Arial', 20, 'bold'), width=12, borderwidth=3, relief="raised",
                                      background='AntiqueWhite3')
        sign_to_courses_button.grid(row=6, columnspan=4, pady=(10, 0))

        # Add user button
        add_user_button = tk.Button(container, text='Add User', command=self.add_user)
        add_user_button.config(font=('Arial', 20, 'bold'), width=12, borderwidth=3, relief="raised",
                               background='SpringGreen3')
        add_user_button.grid(row=7, columnspan=4, pady=(50, 0))

        # Cancel button
        cancel_button = tk.Button(container, text='Cancel', command=lambda: controller.show_frame('AddToLibraryFrame'))
        cancel_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        cancel_button.grid(row=8, columnspan=4, pady=(10, 10))

    def id_validate(self, person_id):
        if re.fullmatch('[0-9]{9}', person_id):
            self.id_entry['foreground'] = 'green'
        else:
            self.id_entry['foreground'] = 'red'

        return True

    def name_validate(self, name):
        if re.fullmatch('[A-Z][a-z]{1,20}', name):
            self.name_entry['foreground'] = 'green'
        else:
            self.name_entry['foreground'] = 'red'

        return True

    def surname_validate(self, surname):
        if re.fullmatch('[A-Z][a-z]{1,20}(-[A-Z][a-z]{1,20}){0,2}', surname):
            self.surname_entry['foreground'] = 'green'
        else:
            self.surname_entry['foreground'] = 'red'

        return True

    def save_selected_courses(self, window, is_course_selected_dictionary):
        self.selected_courses = []

        # Run through the dictionary with the course id as the key, each value that holds 1 append it to a list.
        for course in self.library.courses:
            if is_course_selected_dictionary[course.COURSE_ID].get() == 1:
                self.selected_courses.append(course)

        window.destroy()

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

    def sign_to_courses(self):
        courses = self.library.courses

        if not courses:
            messagebox.showinfo('No Courses', 'There are no courses in the library.')
            return

        popup = tk.Toplevel(self.controller)
        popup.title('Sign to Course')
        popup.config(background='AntiqueWhite3')

        # Dictionary which will hold check boxes values the keys will be an id from a course.
        is_course_selected = dict()

        # Dynamically create checkboxes according to the number of courses in the library.
        for course in courses:
            is_course_selected[course.COURSE_ID] = tk.IntVar()

            course_checkbutton = tk.Checkbutton(popup, text=course.COURSE_ID, onvalue=1, offvalue=0,
                                                variable=is_course_selected[course.COURSE_ID])
            course_checkbutton.config(font=('Arial', 12, 'bold'), borderwidth=3, relief="ridge", width=8,
                                      background='AntiqueWhite3')
            course_checkbutton.pack(side='top')

        save_courses_button = tk.Button(popup, text='Save Courses', width=20,
                                        command=lambda: self.save_selected_courses(popup, is_course_selected))
        save_courses_button.config(font=('Arial', 15, 'bold'), width=12, borderwidth=3, relief="raised",
                                   background='SpringGreen3')
        save_courses_button.pack(padx=(70, 70), pady=(10, 10))

        self.set_toplevel_to_center_of_window(popup)

    def add_user(self):
        person_id = self.person_id.get()
        name = self.name.get()
        surname = self.surname.get()
        birthdate = self.date_entry.get_date()

        if re.fullmatch('[0-9]{9}', person_id) is None \
                or re.fullmatch('[A-Z][a-z]{1,20}', name) is None \
                or re.fullmatch('[A-Z][a-z]{1,20}(-[A-Z][a-z]{1,20}){0,2}', surname) is None:
            messagebox.showerror('Invalid Info Error', 'Please correct your info to match the format!')
            return

        if self.selected_user.get() == 0:
            user_id = self.library.add_student(person_id, name, surname, birthdate, self.selected_courses)
        else:  # Lecturer
            user_id = self.library.add_lecturer(person_id, name, surname, birthdate, self.selected_courses)

        messagebox.showinfo('Registration Complete', 'Your user ID is: ' + str(user_id))

        self.controller.show_frame('AddToLibraryFrame')

        self.person_id.set('')
        self.name.set('')
        self.surname.set('')
        self.date_entry.set_date(self.max_birthdate)
