import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class GetUsersCoursesFrame(tk.Frame):
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

        # Radio buttons for student or lecturer
        student_lecturer_label = tk.Label(container, text='Choose User:')
        student_lecturer_label.config(font=('Arial', 38, 'bold'), borderwidth=3, relief="ridge",
                                      background='AntiqueWhite3')
        student_lecturer_label.grid(row=0, columnspan=4, pady=(100, 0))

        self.selected_user_type = tk.IntVar()

        student_radio_button = tk.Radiobutton(container, text='Student', variable=self.selected_user_type, value=0)
        student_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=8,
                                    background='AntiqueWhite3')
        student_radio_button.grid(row=1, column=0, columnspan=2, padx=(180, 0), pady=(0, 0))

        lecturer_radio_button = tk.Radiobutton(container, text='Lecturer', variable=self.selected_user_type, value=1)
        lecturer_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=8,
                                     background='AntiqueWhite3')
        lecturer_radio_button.grid(row=1, column=2, columnspan=2, padx=(0, 110), pady=(0, 0))

        # User combobox
        user_label = tk.Label(container, text='User:')
        user_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8, background='AntiqueWhite3')
        user_label.grid(row=2, column=0, columnspan=2, padx=(180, 0), pady=(10, 0))

        self.selected_user = tk.StringVar()

        self.user_combobox = ttk.Combobox(container, textvariable=self.selected_user, state='readonly',
                                          postcommand=self.update_combobox)
        self.user_combobox.config(font=('Arial', 14, 'bold'), width=18, background='AntiqueWhite3')
        self.user_combobox.grid(row=2, column=2, columnspan=2, padx=(0, 130), pady=(10, 0))

        # Get courses button
        get_courses_button = tk.Button(container, text='Get Courses', command=self.get_courses)
        get_courses_button.config(font=('Arial', 20, 'bold'), width=12, borderwidth=3, relief="raised",
                                  background='SpringGreen3')
        get_courses_button.grid(row=3, columnspan=4, pady=(50, 0))

        # Return to get info button
        return_button = tk.Button(container, text='Return', command=lambda: controller.show_frame('GetInfoFrame'))
        return_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        return_button.grid(row=4, columnspan=4, pady=(10, 10))

    def update_combobox(self):
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

    def get_courses(self):
        user = self.selected_user.get()

        if not user:
            messagebox.showerror('No User Error', 'Please select a user!')
            return

        popup = tk.Toplevel(self.controller)
        popup.title('User Courses')
        popup.geometry('700x400')
        popup.config(background='AntiqueWhite4')

        popup.grid_columnconfigure(0, weight=1)
        popup.grid_columnconfigure(1, weight=1)
        popup.grid_columnconfigure(2, weight=1)

        user_id = user.split(' ')[0]

        if self.selected_user_type.get() == 1:
            user_courses = self.library.get_lecturer_courses(user_id)
            total_weekly_hours = self.library.get_lecturer_weekly_hours(user_id)
        else:
            user_courses = self.library.get_student_courses(user_id)
            total_weekly_hours = self.library.get_student_weekly_hours(user_id)

        i = 1

        user_courses_label = tk.Label(popup, text=f'{user} Courses:')
        user_courses_label.config(font=('Arial', 14, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        user_courses_label.grid(row=i, columnspan=3, pady=(10, 0))

        for course in user_courses:
            i += 1

            # Course ID
            courses_id_label = tk.Label(popup, text=f'Course ID: {course.COURSE_ID}')
            courses_id_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                    background='AntiqueWhite3')
            courses_id_label.grid(row=i, column=0, pady=(5, 0))

            # Course Name
            courses_name_label = tk.Label(popup, text=f'Course Name: {course.course_name}')
            courses_name_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                      background='AntiqueWhite3')
            courses_name_label.grid(row=i, column=1, pady=(5, 0))

            # Weekly Hours
            weekly_hours_label = tk.Label(popup, text=f'Course Name: {course.weekly_hours}')
            weekly_hours_label.config(font=('Arial', 10, 'bold'), borderwidth=3, relief="ridge", width=30,
                                      background='AntiqueWhite3')
            weekly_hours_label.grid(row=i, column=2, pady=(5, 0))

        i += 1

        # Total Weekly Hours
        total_hours_label = tk.Label(popup, text=f'Total Weekly Hours: {total_weekly_hours}')
        total_hours_label.config(font=('Arial', 14, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        total_hours_label.grid(row=i, columnspan=3, pady=(10, 10))

        self.set_toplevel_to_center_of_window(popup)
