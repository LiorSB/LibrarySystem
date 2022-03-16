import tkinter as tk
from PIL import Image, ImageTk


class LibraryHubFrame(tk.Frame):
    def __init__(self, parent, controller, library):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.library = library

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Hub.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(self, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        # Add
        add_to_library_button = tk.Button(self, text='Add to Library',
                                          command=lambda: controller.show_frame('AddToLibraryFrame'))
        add_to_library_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                     background='AntiqueWhite3')
        add_to_library_button.pack(side='top', pady=(150, 0))

        # Info
        get_info_button = tk.Button(self, text='Get Info',
                                    command=lambda: controller.show_frame('GetInfoFrame'))
        get_info_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                               background='AntiqueWhite3')
        get_info_button.pack(pady=(10, 0))

        # Manage
        manage_library_button = tk.Button(self, text='Manage Library',
                                          command=lambda: controller.show_frame('ManageLibraryFrame'))
        manage_library_button.config(font=('Arial', 20, 'bold'), width='16', borderwidth=3, relief="raised",
                                     background='AntiqueWhite3')
        manage_library_button.pack(pady=(10, 0))

        # Log out
        log_out_button = tk.Button(self, text='Log Out',
                                   command=lambda: controller.show_frame('LoginFrame'))
        log_out_button.config(font=('Arial', 20, 'bold'), width='10', borderwidth=3, relief="raised",
                              background='IndianRed1')
        log_out_button.pack(pady=(100, 0))
