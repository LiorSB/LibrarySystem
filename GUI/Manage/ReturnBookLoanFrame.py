import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class ReturnBookLoanFrame(tk.Frame):
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
        student_lecturer_label = tk.Label(container, text='User Type to Loan:')
        student_lecturer_label.config(font=('Arial', 35, 'bold'), borderwidth=3, relief="ridge",
                                      background='AntiqueWhite3')
        student_lecturer_label.grid(row=0, columnspan=2, pady=(50, 0))

        self.selected_user_type = tk.IntVar()

        student_radio_button = tk.Radiobutton(container, text='Student', variable=self.selected_user_type, value=0)
        student_radio_button.config(font=('Arial', 15, 'bold'), borderwidth=3, relief="ridge", width=12,
                                    background='AntiqueWhite3')
        student_radio_button.grid(row=1, column=0, padx=(100, 0), pady=(10, 0))

        lecturer_radio_button = tk.Radiobutton(container, text='Lecturer', variable=self.selected_user_type, value=1)
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

        # Return book button
        return_book_button = tk.Button(container, text='Return Book', command=self.return_book)
        return_book_button.config(font=('Arial', 20, 'bold'), width=12, borderwidth=3, relief="raised",
                                  background='SpringGreen3')
        return_book_button.grid(row=4, columnspan=2, pady=(50, 0))

        # Return to manage button
        return_button = tk.Button(container, text='Return', command=lambda: controller.show_frame('ManageLibraryFrame'))
        return_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        return_button.grid(row=5, columnspan=2, pady=(40, 20))

    def update_user_combobox(self):
        if self.library.lecturers is None or self.library.students is None:
            self.user_combobox['values'] = None

            return

        user_details = []

        if self.selected_user_type.get() == 1:  # Radio button is on lecturer
            for lecturer in self.library.lecturers:
                user_details.append(f'{lecturer.LECTURER_ID} {lecturer.name} {lecturer.surname}')

            self.user_combobox['values'] = user_details
        else:  # Radio button is on student
            for student in self.library.students:
                user_details.append(f'{student.STUDENT_ID} {student.name} {student.surname}')

            self.user_combobox['values'] = user_details

    def update_book_combobox(self):
        selected_user = self.selected_user.get()

        if not selected_user:
            self.book_combobox['values'] = None
            return

        user_id = selected_user.split(' ')[0]
        user_type = self.selected_user_type.get()

        # Update combobox according to lecturer or student.
        if user_type == 1:
            user = self.library.search_lecturer_id(user_id)
        else:
            user = self.library.search_student_id(user_id)

        # Update combobox according to the chosen user.
        if not user.loaned_books:
            self.book_combobox['values'] = None
        else:
            self.book_combobox['values'] = [loaned_book.book.BOOK_ID for loaned_book in user.loaned_books]

    def return_book(self):
        book_id = self.selected_book.get()
        user = self.selected_user.get()
        user_id = user.split(' ')[0]
        user_type = 'Lecturer' if self.selected_user_type.get() == 1 else 'Student'

        if not user or not book_id:
            messagebox.showerror('Empty Fields Error', 'Please fill all required fields!')
            return

        fine_to_pay = self.library.return_book(book_id, user_id, user_type)

        if fine_to_pay is None:
            messagebox.showerror('Return Loan Error', 'No such book loan record exists!')
            return

        if fine_to_pay <= 0:
            pay_message = f'{user} has not debts.'
        else:
            pay_message = f'{user} has to pay {fine_to_pay}$ for being late.'

        messagebox.showinfo('Book Returned', pay_message)

        self.user_combobox['values'] = None
        self.book_combobox['values'] = None

        self.controller.show_frame('LibraryHubFrame')
