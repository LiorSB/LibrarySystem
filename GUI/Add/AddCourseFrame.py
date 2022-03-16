import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class AddCourseFrame(tk.Frame):
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

        # Course name fields
        course_name_label = tk.Label(container, text='Course Name:')
        course_name_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=14,
                                 background='AntiqueWhite3')
        course_name_label.grid(row=0, column=0, padx=(100, 0), pady=(150, 0))

        self.course_name = tk.StringVar()

        course_name_entry = tk.Entry(container, textvariable=self.course_name)
        course_name_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                                 background='AntiqueWhite3')
        course_name_entry.grid(row=0, column=1, padx=(0, 100), pady=(150, 0))

        # Weekly Hours fields
        weekly_hours_label = tk.Label(container, text='Weekly Hours:')
        weekly_hours_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=14,
                                  background='AntiqueWhite3')
        weekly_hours_label.grid(row=1, column=0, padx=(100, 0), pady=(10, 0))

        self.weekly_hours = tk.StringVar()

        weekly_hours_spinbox = tk.Spinbox(container, from_=1, to=15, textvariable=self.weekly_hours)
        weekly_hours_spinbox.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=11,
                                    background='AntiqueWhite3')
        weekly_hours_spinbox.grid(row=1, column=1, padx=(0, 100), pady=(10, 0))

        # Lecturer fields
        lecturer_label = tk.Label(container, text='Lecturer:')
        lecturer_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=14,
                              background='AntiqueWhite3')
        lecturer_label.grid(row=2, column=0, padx=(100, 0), pady=(10, 0))

        self.selected_lecturer = tk.StringVar()

        self.lecturer_combobox = ttk.Combobox(container, textvariable=self.selected_lecturer, state='readonly',
                                              postcommand=self.update_combo_box)
        self.lecturer_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.lecturer_combobox.grid(row=2, column=1, padx=(10, 100), pady=(10, 0))

        # Add course button
        add_course_button = tk.Button(container, text='Add Course', command=self.add_course)
        add_course_button.config(font=('Arial', 20, 'bold'), width=12, borderwidth=3, relief="raised",
                                 background='SpringGreen3')
        add_course_button.grid(row=3, columnspan=2, pady=(30, 0))

        # Cancel button
        cancel_button = tk.Button(container, text='Cancel', command=lambda: controller.show_frame('AddToLibraryFrame'))
        cancel_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        cancel_button.grid(row=4, columnspan=2, pady=(10, 10))

    def update_combo_box(self):
        if self.library.lecturers is None:
            self.lecturer_combobox['values'] = None
        else:
            self.lecturer_combobox['values'] = [f'{lecturer.LECTURER_ID} {lecturer.name} {lecturer.surname}'
                                                for lecturer in self.library.lecturers]

    def add_course(self):
        course_name = self.course_name.get()
        weekly_hours = self.weekly_hours.get()
        selected_lecturer = self.selected_lecturer.get()

        if not selected_lecturer:
            selected_lecturer = None
        else:
            selected_lecturer = selected_lecturer.split(' ')[0]
            selected_lecturer = self.library.search_lecturer_id(selected_lecturer)

        if not course_name:
            messagebox.showerror('Invalid Info Error', 'Course name can not be empty!')
            return

        course_id = self.library.add_course(course_name, weekly_hours, selected_lecturer)

        messagebox.showinfo('Course Add', 'The course ID is: ' + str(course_id))

        self.controller.show_frame('AddToLibraryFrame')

        self.selected_lecturer.set('')
        self.course_name.set('')
        self.weekly_hours.set('1')
