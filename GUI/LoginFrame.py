import re
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginFrame(tk.Frame):
    def __init__(self, parent, controller, library):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.library = library

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Login.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(self, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        librarian_id_vcmd = (self.register(self.librarian_id_validate), '%P')

        self.default_entry_text = 'Librarian#'
        self.librarian_id = tk.StringVar()

        librarian_id_label = tk.Label(self, text='Librarian ID:')
        librarian_id_label.config(font=('Helvetica', 30, 'bold'), borderwidth=5, relief="ridge",
                                  background='light grey')
        librarian_id_label.pack(side='top', pady=(160, 10))

        self.librarian_id_entry = tk.Entry(self, textvariable=self.librarian_id, validate='key',
                                           validatecommand=librarian_id_vcmd)
        self.librarian_id_entry.config(font=('Arial', 12, 'bold'), borderwidth=3, relief="ridge",
                                       background='light grey')
        self.librarian_id_entry.insert(0, self.default_entry_text)
        self.librarian_id_entry.pack()

        login_button = tk.Button(self, text='Log In', command=self.login)
        login_button.config(font=('Arial', 20, 'bold'), width='8', borderwidth=3, relief="raised",
                            background='SpringGreen3')
        login_button.pack(pady=(180, 20))

        register_button = tk.Button(self, text='Register', command=lambda: controller.show_frame('RegisterFrame'))
        register_button.config(font=('Arial', 20, 'bold'), width='8', borderwidth=3, relief="raised",
                               background='SkyBlue2')
        register_button.pack()

    def librarian_id_validate(self, librarian_id):
        if re.fullmatch('Librarian[0-9]{1,100}', librarian_id):
            self.librarian_id_entry['foreground'] = 'green'
        else:
            self.librarian_id_entry['foreground'] = 'red'

        return True

    def login(self):
        librarian = self.library.search_librarian_id(self.librarian_id.get())

        if librarian is None:
            messagebox.showerror('Login Error', 'Librarian ID does not exist!')
            return

        messagebox.showinfo('Login Success', f'Welcome {librarian.name} {librarian.surname}')

        self.controller.show_frame('LibraryHubFrame')

        self.librarian_id.set('')
        self.librarian_id_entry.insert(0, self.default_entry_text)
