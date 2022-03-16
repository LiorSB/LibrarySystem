import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class EditCourseFrame(tk.Frame):
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

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Book.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(container, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        # Course combobox
        course_label = tk.Label(container, text='Course:')
        course_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                            background='AntiqueWhite3')
        course_label.grid(row=0, column=0, padx=(100, 0), pady=(120, 0))

        self.selected_course = tk.StringVar()

        self.course_combobox = ttk.Combobox(container, textvariable=self.selected_course, state='readonly',
                                            postcommand=self.update_course_combobox)
        self.course_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.course_combobox.grid(row=0, column=1, padx=(0, 100), pady=(120, 0))

        # Weekly Hours fields
        weekly_hours_label = tk.Label(container, text='Weekly Hours:')
        weekly_hours_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                                  background='AntiqueWhite3')
        weekly_hours_label.grid(row=1, column=0, padx=(100, 0), pady=(10, 0))

        self.weekly_hours = tk.StringVar()

        weekly_hours_spinbox = tk.Spinbox(container, from_=1, to=15, textvariable=self.weekly_hours)
        weekly_hours_spinbox.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=11,
                                    background='AntiqueWhite3')
        weekly_hours_spinbox.grid(row=1, column=1, padx=(0, 100), pady=(10, 0))

        # Lecturer combobox
        lecturer_label = tk.Label(container, text='Lecturer:')
        lecturer_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                              background='AntiqueWhite3')
        lecturer_label.grid(row=2, column=0, padx=(100, 0), pady=(10, 0))

        self.selected_lecturer = tk.StringVar()

        self.lecturer_combobox = ttk.Combobox(container, textvariable=self.selected_lecturer, state='readonly',
                                              postcommand=self.update_lecturer_combobox)
        self.lecturer_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.lecturer_combobox.grid(row=2, column=1, padx=(0, 100), pady=(10, 0))

        # Edit course button
        edit_course_button = tk.Button(container, text='Edit Course', command=self.edit_course)
        edit_course_button.config(font=('Arial', 20, 'bold'), width=13, borderwidth=3, relief="raised",
                                  background='SpringGreen3')
        edit_course_button.grid(row=3, columnspan=2, pady=(80, 0))

        # Return to manage button
        return_button = tk.Button(container, text='Return', command=lambda: controller.show_frame('ManageLibraryFrame'))
        return_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        return_button.grid(row=4, columnspan=2, pady=(40, 20))

    def update_course_combobox(self):
        if self.library.courses is None:
            self.course_combobox['values'] = None
        else:
            self.course_combobox['values'] = [course.COURSE_ID for course in self.library.courses]

    def update_lecturer_combobox(self):
        if self.library.lecturers is None:
            self.lecturer_combobox['values'] = None
        else:
            self.lecturer_combobox['values'] = [f'{lecturer.LECTURER_ID} {lecturer.name} {lecturer.surname}'
                                                for lecturer in self.library.lecturers]

    def edit_course(self):
        course_id = self.selected_course.get()
        lecturer_id = self.selected_lecturer.get().split(' ')[0]
        weekly_hours = self.weekly_hours.get()

        if not course_id or not lecturer_id:
            messagebox.showerror('Field Error', 'Please fill all fields!')
            return

        self.library.edit_course(course_id, lecturer_id, weekly_hours)

        messagebox.showinfo('Course Successfully Edited', f'The course: {course_id} has been edited.')

        self.controller.show_frame('ManageLibraryFrame')

        self.course_combobox['values'] = None
        self.lecturer_combobox['values'] = None
        self.weekly_hours.set('1')
