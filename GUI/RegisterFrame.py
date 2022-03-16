import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
import re
from PIL import Image, ImageTk
import datetime


class RegisterFrame(tk.Frame):
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

        id_vcmd = (self.register(self.id_validate), '%P')
        name_vcmd = (self.register(self.name_validate), '%P')
        surname_vcmd = (self.register(self.surname_validate), '%P')

        # ID fields
        self.person_id = tk.StringVar()

        id_label = tk.Label(container, text='ID:')
        id_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8, background='AntiqueWhite3')
        id_label.grid(row=0, column=0, padx=(100, 0), pady=(50, 0))

        self.id_entry = tk.Entry(container, textvariable=self.person_id, validate='key', validatecommand=id_vcmd)
        self.id_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        self.id_entry.grid(row=0, column=1, padx=(0, 100), pady=(50, 0))

        # Name fields
        self.name = tk.StringVar()

        name_label = tk.Label(container, text='Name:')
        name_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8,
                          background='AntiqueWhite3')
        name_label.grid(row=1, column=0, padx=(100, 0))

        self.name_entry = tk.Entry(container, textvariable=self.name, validate='key', validatecommand=name_vcmd)
        self.name_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        self.name_entry.grid(row=1, column=1, padx=(0, 100))

        # Surname fields
        self.surname = tk.StringVar()

        surname_label = tk.Label(container, text='Surname:')
        surname_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8,
                             background='AntiqueWhite3')
        surname_label.grid(row=2, column=0, padx=(100, 0))

        self.surname_entry = tk.Entry(container, textvariable=self.surname, validate='key',
                                      validatecommand=surname_vcmd)
        self.surname_entry.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", background='AntiqueWhite3')
        self.surname_entry.grid(row=2, column=1, padx=(0, 100))

        # Birthdate fields
        birthdate_label = tk.Label(container, text='Birthdate:')
        birthdate_label.config(font=('Arial', 18, 'bold'), borderwidth=3, relief="ridge", width=8,
                               background='AntiqueWhite3')
        birthdate_label.grid(row=3, column=0, padx=(100, 0))

        # Max age 21 years, leap years weren't taken into consideration.
        self.max_birthdate = datetime.date.today() - datetime.timedelta(days=365 * 21)

        self.date_entry = DateEntry(container, date_pattern='dd/mm/yyyy', maxdate=self.max_birthdate)
        self.date_entry.config(width=40, background='AntiqueWhite4')
        self.date_entry.grid(row=3, column=1, padx=(0, 100))

        # Register button
        register_button = tk.Button(container, text='Register', width=10, height='1', command=self.registration)
        register_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                               background='SpringGreen3')
        register_button.grid(row=4, columnspan=2, pady=(80, 0))

        # Cancel button
        cancel_button = tk.Button(container, text='Cancel', width=10, height='1',
                                  command=lambda: controller.show_frame('LoginFrame'))
        cancel_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        cancel_button.grid(row=5, columnspan=2, pady=(0, 50))

    def id_validate(self, id_person):
        if re.fullmatch('[0-9]{9}', id_person):
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

    def registration(self):
        person_id = self.person_id.get()
        name = self.name.get()
        surname = self.surname.get()
        birthdate = self.date_entry.get_date()

        if re.fullmatch('[0-9]{9}', person_id) is None \
                or re.fullmatch('[A-Z][a-z]{1,20}', name) is None \
                or re.fullmatch('[A-Z][a-z]{1,20}(-[A-Z][a-z]{1,20}){0,2}', surname) is None:
            messagebox.showerror('Invalid Info Error', 'Please correct your info to match the format!')
            return

        librarian_id = self.library.add_librarian(person_id, name, surname, birthdate)
        messagebox.showinfo('Registration Complete', 'Your Librarian ID is: ' + str(librarian_id))

        self.controller.show_frame('LoginFrame')

        self.person_id.set('')
        self.name.set('')
        self.surname.set('')
        self.date_entry.set_date(self.max_birthdate)
