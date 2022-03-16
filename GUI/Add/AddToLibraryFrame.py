import tkinter as tk
from PIL import Image, ImageTk


class AddToLibraryFrame(tk.Frame):
    def __init__(self, parent, controller, library):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.library = library

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Add.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(self, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        # Add User
        add_user_button = tk.Button(self, text='Add User',
                                    command=lambda: controller.show_frame('AddUserFrame'))
        add_user_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                               background='AntiqueWhite4')
        add_user_button.pack(side='top', pady=(150, 0))

        # Add Course
        add_course_button = tk.Button(self, text='Add Course',
                                      command=lambda: controller.show_frame('AddCourseFrame'))
        add_course_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                 background='AntiqueWhite4')
        add_course_button.pack(pady=(10, 0))

        # Add Book
        add_book_button = tk.Button(self, text='Add Book',
                                    command=lambda: controller.show_frame('AddBookFrame'))
        add_book_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                               background='AntiqueWhite4')
        add_book_button.pack(pady=(10, 0))

        # Return to Hub
        return_to_hub_button = tk.Button(self, text='Return to Hub',
                                         command=lambda: controller.show_frame('LibraryHubFrame'))
        return_to_hub_button.config(font=('Arial', 20, 'bold'), width='12', borderwidth=3, relief="raised",
                                    background='IndianRed1')
        return_to_hub_button.pack(pady=(100, 0))
