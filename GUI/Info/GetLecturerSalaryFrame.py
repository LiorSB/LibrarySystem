import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class GetLecturerSalaryFrame(tk.Frame):
    def __init__(self, parent, controller, library):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.library = library

        window_width = self.controller.winfo_width()
        window_height = self.controller.winfo_height()

        # Display image on a Label widget.
        image_path = 'Images/Book.jpg'
        image = ImageTk.PhotoImage(Image.open(image_path).resize((window_width, window_height), Image.ANTIALIAS))
        image_label = tk.Label(self, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor='center')

        # Lecturer fields
        lecturer_label = tk.Label(self, text='Lecturer:')
        lecturer_label.config(font=('Helvetica', 36, 'bold'), borderwidth=5, relief="ridge", background='AntiqueWhite3')
        lecturer_label.pack(side='top', pady=(120, 0))

        self.selected_lecturer = tk.StringVar()

        self.lecturer_combobox = ttk.Combobox(self, textvariable=self.selected_lecturer, state='readonly',
                                              postcommand=self.update_combo_box)
        self.lecturer_combobox.config(font=('Arial', 14, 'bold'), width=24, background='AntiqueWhite3')
        self.lecturer_combobox.pack(pady=(30, 0))

        # Calculate salary button
        calculate_salary_button = tk.Button(self, text='Calculate Salary', command=self.calculate_salary)
        calculate_salary_button.config(font=('Arial', 20, 'bold'), width=13, borderwidth=3, relief="raised",
                                       background='SpringGreen3')
        calculate_salary_button.pack(pady=(200, 0))

        # Return to get info button
        return_button = tk.Button(self, text='Return', command=lambda: controller.show_frame('GetInfoFrame'))
        return_button.config(font=('Arial', 20, 'bold'), width=8, borderwidth=3, relief="raised",
                             background='IndianRed1')
        return_button.pack(pady=(20, 15))

    def update_combo_box(self):
        if self.library.lecturers is None:
            self.lecturer_combobox['values'] = None
        else:
            self.lecturer_combobox['values'] = [f'{lecturer.LECTURER_ID} {lecturer.name} {lecturer.surname}'
                                                for lecturer in self.library.lecturers]

    def calculate_salary(self):
        lecturer = self.selected_lecturer.get()

        if not lecturer:
            messagebox.showerror('No Lecturer Error', 'Please select a lecturer!')
            return

        lecturer_id = lecturer.split(' ')[0]
        lecturer_salary = self.library.get_lecturer_salary(lecturer_id)

        messagebox.showinfo('Lecturer\'s Salary', f'{lecturer} salary is: {lecturer_salary}$')
