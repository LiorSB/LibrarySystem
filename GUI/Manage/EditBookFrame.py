import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class EditBookFrame(tk.Frame):
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

        # Book combobox
        book_label = tk.Label(container, text='Book:')
        book_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=15,
                          background='AntiqueWhite3')
        book_label.grid(row=0, column=0, padx=(80, 0), pady=(120, 0))

        self.selected_book = tk.StringVar()

        self.book_combobox = ttk.Combobox(container, textvariable=self.selected_book, state='readonly',
                                          postcommand=self.update_book_combobox)
        self.book_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.book_combobox.grid(row=0, column=1, padx=(0, 80), pady=(120, 0))

        # Number of copies fields
        number_of_copies_label = tk.Label(container, text='Number of Copies:')
        number_of_copies_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=15,
                                      background='AntiqueWhite3')
        number_of_copies_label.grid(row=1, column=0, padx=(80, 0), pady=(10, 0))

        self.number_of_copies = tk.StringVar()

        number_of_copies_spinbox = tk.Spinbox(container, from_=1, to=100, textvariable=self.number_of_copies)
        number_of_copies_spinbox.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=11,
                                        background='AntiqueWhite3')
        number_of_copies_spinbox.grid(row=1, column=1, padx=(0, 80), pady=(10, 0))

        # Course combobox
        course_label = tk.Label(container, text='Course:')
        course_label.config(font=('Helvetica', 18, 'bold'), borderwidth=3, relief="ridge", width=15,
                            background='AntiqueWhite3')
        course_label.grid(row=2, column=0, padx=(80, 0), pady=(10, 0))

        self.selected_course = tk.StringVar()

        self.course_combobox = ttk.Combobox(container, textvariable=self.selected_course, state='readonly',
                                            postcommand=self.update_course_combobox)
        self.course_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.course_combobox.grid(row=2, column=1, padx=(0, 80), pady=(10, 0))

        # Edit book button
        edit_book_button = tk.Button(container, text='Edit Book', command=self.edit_book)
        edit_book_button.config(font=('Arial', 20, 'bold'), width=13, borderwidth=3, relief="raised",
                                background='SpringGreen3')
        edit_book_button.grid(row=3, columnspan=2, pady=(80, 0))

        # return button
        return_button = tk.Button(container, text='Return', command=lambda: controller.show_frame('ManageLibraryFrame'))
        return_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        return_button.grid(row=4, columnspan=2, pady=(40, 20))

    def update_book_combobox(self):
        if self.library.books is None:
            self.book_combobox['values'] = None
        else:
            self.book_combobox['values'] = [book.BOOK_ID for book in self.library.books]

    def update_course_combobox(self):
        if self.library.courses is None:
            self.course_combobox['values'] = None
        else:
            self.course_combobox['values'] = [course.COURSE_ID for course in self.library.courses]

    def edit_book(self):
        book_id = self.selected_book.get()
        course_id = self.selected_course.get()
        number_of_copies = self.number_of_copies.get()

        if not book_id or not course_id:
            messagebox.showerror('Field Error', 'Please fill all fields!')
            return

        self.library.edit_book(book_id, course_id, number_of_copies)

        messagebox.showinfo('Book Successfully Edited', f'The book: {book_id} has been edited.')

        self.controller.show_frame('ManageLibraryFrame')

        self.book_combobox['values'] = None
        self.course_combobox['values'] = None
        self.number_of_copies.set('1')
