import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class AddBookFrame(tk.Frame):
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

        # Book title fields
        book_title_label = tk.Label(container, text='Book Title:')
        book_title_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=15,
                                background='AntiqueWhite3')
        book_title_label.grid(row=0, column=0, padx=(100, 0), pady=(70, 0))

        self.book_title = tk.StringVar()

        book_title_entry = tk.Entry(container, textvariable=self.book_title)
        book_title_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                                background='AntiqueWhite3')
        book_title_entry.grid(row=0, column=1, padx=(0, 100), pady=(70, 0))

        # Book author fields
        book_author_label = tk.Label(container, text='Book Author:')
        book_author_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=15,
                                 background='AntiqueWhite3')
        book_author_label.grid(row=1, column=0, padx=(100, 0), pady=(10, 0))

        self.book_author = tk.StringVar()

        book_author_entry = tk.Entry(container, textvariable=self.book_author)
        book_author_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=12,
                                 background='AntiqueWhite3')
        book_author_entry.grid(row=1, column=1, padx=(0, 100), pady=(10, 0))

        # Number of copies fields
        number_of_copies_label = tk.Label(container, text='Number of Copies:')
        number_of_copies_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=15,
                                      background='AntiqueWhite3')
        number_of_copies_label.grid(row=2, column=0, padx=(100, 0), pady=(10, 0))

        self.number_of_copies = tk.StringVar()

        number_of_copies_spinbox = tk.Spinbox(container, from_=1, to=100, textvariable=self.number_of_copies)
        number_of_copies_spinbox.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=11,
                                        background='AntiqueWhite3')
        number_of_copies_spinbox.grid(row=2, column=1, padx=(0, 100), pady=(10, 0))

        # Related course fields
        related_course_label = tk.Label(container, text='Related Course:')
        related_course_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=15,
                                    background='AntiqueWhite3')
        related_course_label.grid(row=3, column=0, padx=(100, 0), pady=(10, 0))

        self.selected_course = tk.StringVar()

        self.related_course_combobox = ttk.Combobox(container, textvariable=self.selected_course, state='readonly',
                                                    postcommand=self.update_combo_box)
        self.related_course_combobox.config(font=('Arial', 18, 'bold'), width=11, background='AntiqueWhite3')
        self.related_course_combobox.grid(row=3, column=1, padx=(0, 100), pady=(10, 0))

        # Add book button
        add_book_button = tk.Button(container, text='Add Book', width='10', height='1', command=self.add_course)
        add_book_button.config(font=('Arial', 20, 'bold'), width=12, borderwidth=3, relief="raised",
                               background='SpringGreen3')
        add_book_button.grid(row=4, columnspan=2, pady=(10, 0))

        # Cancel button
        cancel_button = tk.Button(container, text='Cancel', width='10', height='1',
                                  command=lambda: controller.show_frame('AddToLibraryFrame'))
        cancel_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        cancel_button.grid(row=5, columnspan=2, pady=(10, 10))

    def update_combo_box(self):
        if self.library.courses is None:
            self.related_course_combobox['values'] = None
        else:
            self.related_course_combobox['values'] = [course.COURSE_ID for course in self.library.courses]

    def add_course(self):
        book_title = self.book_title.get()
        book_author = self.book_author.get()
        number_of_copies = self.number_of_copies.get()
        selected_course = self.selected_course.get()

        if not book_title or not book_author:
            messagebox.showerror('Invalid Info Error', 'Book title or author can not be empty!')
            return

        if not selected_course:
            selected_course = None
        else:
            selected_course = self.library.search_course_id(selected_course)

        book_id = self.library.add_book(book_title, book_author, number_of_copies, selected_course)

        messagebox.showinfo('Book Add', f'The Book ID is: {book_id}')

        self.controller.show_frame('AddToLibraryFrame')

        self.book_title.set('')
        self.book_author.set('')
        self.number_of_copies.set('1')
