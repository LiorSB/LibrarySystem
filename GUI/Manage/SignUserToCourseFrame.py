import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class SignUserToCourseFrame(tk.Frame):
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

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Book.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(container, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        # Radio buttons for student or lecturer
        student_lecturer_label = tk.Label(container, text='User Type to Assign Courses:')
        student_lecturer_label.config(font=('Arial', 35, 'bold'), borderwidth=3, relief="ridge",
                                      background='AntiqueWhite3')
        student_lecturer_label.grid(row=0, columnspan=2, pady=(50, 0))

        self.selected_user_type = tk.IntVar()

        student_radio_button = tk.Radiobutton(container, text='Student', variable=self.selected_user_type, value=0)
        student_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=8,
                                    background='AntiqueWhite3')
        student_radio_button.grid(row=1, column=0, padx=(120, 0), pady=(10, 0))

        lecturer_radio_button = tk.Radiobutton(container, text='Lecturer', variable=self.selected_user_type, value=1)
        lecturer_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=8,
                                     background='AntiqueWhite3')
        lecturer_radio_button.grid(row=1, column=1, padx=(0, 0), pady=(10, 0))

        # User combobox
        user_label = tk.Label(container, text='User:')
        user_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=8,
                          background='AntiqueWhite3')
        user_label.grid(row=2, column=0, padx=(120, 0), pady=(10, 0))

        self.selected_user = tk.StringVar()

        self.user_combobox = ttk.Combobox(container, textvariable=self.selected_user, state='readonly',
                                          postcommand=self.update_user_combobox)
        self.user_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.user_combobox.grid(row=2, column=1, padx=(0, 120), pady=(10, 0))

        # Choose course button
        self.selected_courses = None
        self.unassigned_courses = None

        choose_course_button = tk.Button(container, text='Choose Courses', command=self.choose_course)
        choose_course_button.config(font=('Arial', 20, 'bold'), width=14, borderwidth=3, relief="raised",
                                    background='AntiqueWhite3')
        choose_course_button.grid(row=3, columnspan=2, pady=(10, 0))

        # Sign to course button
        sign_button = tk.Button(container, text='Sign to Courses', command=self.assign_to_course)
        sign_button.config(font=('Arial', 20, 'bold'), width=15, borderwidth=3, relief="raised",
                           background='SpringGreen3')
        sign_button.grid(row=4, columnspan=2, pady=(50, 0))

        # Return to manage button
        return_button = tk.Button(container, text='Return', command=lambda: controller.show_frame('ManageLibraryFrame'))
        return_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        return_button.grid(row=5, columnspan=2, pady=(40, 20))

    def update_user_combobox(self):
        if self.selected_user_type.get() == 1:  # Radio button is on lecturer
            if self.library.lecturers is None:
                self.user_combobox['values'] = None
            else:
                self.user_combobox['values'] = [f'{lecturer.LECTURER_ID} {lecturer.name} {lecturer.surname}'
                                                for lecturer in self.library.lecturers]
        else:  # Radio button is on student
            if self.library.students is None:
                self.user_combobox['values'] = None
            else:
                self.user_combobox['values'] = [f'{student.STUDENT_ID} {student.name} {student.surname}'
                                                for student in self.library.students]

    def save_selected_courses(self, window, is_course_selected_dictionary):
        self.selected_courses = []

        # Run through the dictionary with the course id as the key, each value that holds 1 append it to a list.
        for course in self.unassigned_courses:
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

    def choose_course(self):
        courses = self.library.courses

        if not courses:
            messagebox.showerror('No Courses Error', 'There are no courses in the library.')
            return

        user_details = self.selected_user.get()

        if not user_details:
            messagebox.showerror('User Not Selected Error', 'Please select a user!')
            return

        user_id = user_details.split(' ')[0]
        user_type = self.selected_user_type.get()

        if user_type == 1:
            user = self.library.search_lecturer_id(user_id)
            user_courses = user.courses_teaching
        else:
            user = self.library.search_student_id(user_id)
            user_courses = user.courses_taken

        self.unassigned_courses = list(set(courses).difference(user_courses))

        if not self.unassigned_courses:
            messagebox.showerror('Choose Course Error', f'The user: {user_details} is signed to all courses.')
            return

        popup = tk.Toplevel(self.controller)
        popup.title('Choose Courses')
        popup.config(background='AntiqueWhite3')

        # Dictionary which will hold check boxes values the keys will be an id from a course.
        is_course_selected = dict()

        # Dynamically create checkboxes according to the number of courses in the library.
        for course in self.unassigned_courses:
            is_course_selected[course.COURSE_ID] = tk.IntVar()

            course_checkbutton = tk.Checkbutton(popup, text=course.COURSE_ID, onvalue=1, offvalue=0,
                                                variable=is_course_selected[course.COURSE_ID])
            course_checkbutton.config(font=('Arial', 12, 'bold'), borderwidth=3, relief="ridge", width=8,
                                      background='AntiqueWhite3')
            course_checkbutton.pack(side='top')

        save_courses_button = tk.Button(popup, text='Save Courses',
                                        command=lambda: self.save_selected_courses(popup, is_course_selected))
        save_courses_button.config(font=('Arial', 15, 'bold'), width=12, borderwidth=3, relief="raised",
                                   background='SpringGreen3')
        save_courses_button.pack(padx=(70, 70), pady=(10, 10))

        self.set_toplevel_to_center_of_window(popup)

    def assign_to_course(self):
        user = self.selected_user.get()

        if not user:
            messagebox.showerror('Sign Error', 'Please select a user!')
            return

        user_id = user.split(' ')[0]
        user_type = 'Lecturer' if self.selected_user_type.get() == 1 else 'Student'
        courses = self.selected_courses

        if not courses:
            messagebox.showerror('Sign Error', f'No courses assigned to the user: {user}')
            return

        self.library.sign_user_to_courses(user_id, user_type, courses)
        messagebox.showinfo('Sign Success', f'The user: {user}, has been signed to the courses: '
                                            f'{[course.COURSE_ID for course in courses]}')

        self.selected_courses = None
        self.user_combobox['values'] = None
        self.controller.show_frame('ManageLibraryFrame')
