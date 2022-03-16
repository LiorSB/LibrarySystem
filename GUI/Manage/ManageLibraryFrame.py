import tkinter as tk
from PIL import Image, ImageTk


class ManageLibraryFrame(tk.Frame):
    def __init__(self, parent, controller, library):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.library = library

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Manage.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(self, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        # Edit Course
        edit_course_button = tk.Button(self, text='Edit Course',
                                       command=lambda: controller.show_frame('EditCourseFrame'))
        edit_course_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                  background='AntiqueWhite4')
        edit_course_button.pack(side='top', pady=(50, 0))

        # Edit Book
        edit_book_button = tk.Button(self, text='Edit Book',
                                     command=lambda: controller.show_frame('EditBookFrame'))
        edit_book_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                background='AntiqueWhite4')
        edit_book_button.pack(pady=(10, 0))

        # Sign User to Course
        sign_user_to_course_button = tk.Button(self, text='Sign User to Course',
                                               command=lambda: controller.show_frame('SignUserToCourseFrame'))
        sign_user_to_course_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                          background='AntiqueWhite4')
        sign_user_to_course_button.pack(pady=(10, 0))

        # Lend Book
        lend_book_button = tk.Button(self, text='Lend Book',
                                     command=lambda: controller.show_frame('LendBookFrame'))
        lend_book_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                background='AntiqueWhite4')
        lend_book_button.pack(pady=(10, 0))

        # Return Book Loan
        return_book_loan_button = tk.Button(self, text='Return Book Loan',
                                            command=lambda: controller.show_frame('ReturnBookLoanFrame'))
        return_book_loan_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                       background='AntiqueWhite4')
        return_book_loan_button.pack(pady=(10, 0))

        # Return to Hub
        return_to_hub_button = tk.Button(self, text='Return to Hub',
                                         command=lambda: controller.show_frame('LibraryHubFrame'))
        return_to_hub_button.config(font=('Arial', 20, 'bold'), width='12', borderwidth=3, relief="raised",
                                    background='IndianRed1')
        return_to_hub_button.pack(pady=(100, 0))
