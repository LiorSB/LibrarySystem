import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk


class LendBookFrame(tk.Frame):
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
        student_lecturer_label = tk.Label(container, text='User Type to Loan:')
        student_lecturer_label.config(font=('Arial', 35, 'bold'), borderwidth=3, relief="ridge",
                                      background='AntiqueWhite3')
        student_lecturer_label.grid(row=0, columnspan=2, pady=(50, 0))

        self.selected_user_type = tk.IntVar()

        student_radio_button = tk.Radiobutton(container, text='Student', variable=self.selected_user_type, value=0,
                                              command=self.set_student_date)
        student_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=12,
                                    background='AntiqueWhite3')
        student_radio_button.grid(row=1, column=0, padx=(100, 0), pady=(10, 0))

        lecturer_radio_button = tk.Radiobutton(container, text='Lecturer', variable=self.selected_user_type, value=1,
                                               command=self.set_lecturer_date)
        lecturer_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=12,
                                     background='AntiqueWhite3')
        lecturer_radio_button.grid(row=1, column=1, padx=(0, 0), pady=(10, 0))

        # User combobox
        user_label = tk.Label(container, text='User:')
        user_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                          background='AntiqueWhite3')
        user_label.grid(row=2, column=0, padx=(100, 0), pady=(10, 0))

        self.selected_user = tk.StringVar()

        self.user_combobox = ttk.Combobox(container, textvariable=self.selected_user, state='readonly',
                                          postcommand=self.update_user_combobox)
        self.user_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.user_combobox.grid(row=2, column=1, padx=(0, 100), pady=(10, 0))

        # Book combobox
        book_label = tk.Label(container, text='Book:')
        book_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                          background='AntiqueWhite3')
        book_label.grid(row=3, column=0, padx=(100, 0), pady=(10, 0))

        self.selected_book = tk.StringVar()

        self.book_combobox = ttk.Combobox(container, textvariable=self.selected_book, state='readonly',
                                          postcommand=self.update_book_combobox)
        self.book_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.book_combobox.grid(row=3, column=1, padx=(0, 100), pady=(10, 0))

        # Loan end date
        loan_end_date_label = tk.Label(container, text='Loan End Date:')
        loan_end_date_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                                   background='AntiqueWhite3')
        loan_end_date_label.grid(row=4, column=0, padx=(100, 0), pady=(10, 0))

        tomorrows_date = datetime.date.today() + datetime.timedelta(days=1)

        self.loan_date_entry = DateEntry(container, date_pattern='dd/mm/yyyy', mindate=tomorrows_date)
        self.loan_date_entry.config(width=36, background='AntiqueWhite4')
        self.loan_date_entry.grid(row=4, column=1, padx=(0, 100), pady=(10, 0))

        # Lend book button
        lend_book_button = tk.Button(container, text='Lend Book', command=self.lend_book)
        lend_book_button.config(font=('Arial', 20, 'bold'), width=12, borderwidth=3, relief="raised",
                                background='SpringGreen3')
        lend_book_button.grid(row=5, columnspan=2, pady=(50, 0))

        # Return to manage button
        return_button = tk.Button(container, text='Return', command=lambda: controller.show_frame('ManageLibraryFrame'))
        return_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        return_button.grid(row=6, columnspan=2, pady=(40, 20))

    def set_student_date(self):
        max_loan_date = datetime.date.today() + datetime.timedelta(days=7)
        self.loan_date_entry.config(maxdate=max_loan_date)

    def set_lecturer_date(self):
        max_loan_date = datetime.date.today() + datetime.timedelta(days=30)
        self.loan_date_entry.config(maxdate=max_loan_date)

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

    def update_book_combobox(self):
        if self.library.books is None:
            self.book_combobox['values'] = None
        else:
            self.book_combobox['values'] = [book.BOOK_ID for book in self.library.books]

    def lend_book(self):
        book_id = self.selected_book.get()
        user = self.selected_user.get()
        user_id = user.split(' ')[0]
        user_type = 'Lecturer' if self.selected_user_type.get() == 1 else 'Student'
        loan_end_date = self.loan_date_entry.get_date()

        if not user or not book_id:
            messagebox.showerror('Empty Fields Error', 'Please fill all required fields!')
            return

        if self.library.lend_book(book_id, user_id, user_type, loan_end_date):
            messagebox.showinfo('Loan Succeed', f'Book loaned to: {user}, till: {loan_end_date}')
        else:
            messagebox.showerror('Loan Failed', f'The following book is out of stock: {loan_end_date}')

        self.user_combobox['values'] = None
        self.book_combobox['values'] = None

        self.controller.show_frame('ManageLibraryFrame')
