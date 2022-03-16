import tkinter as tk
from Entities.Library import Library

from GUI.LoginFrame import LoginFrame
from GUI.RegisterFrame import RegisterFrame

from GUI.LibraryHubFrame import LibraryHubFrame

from GUI.Add.AddToLibraryFrame import AddToLibraryFrame
from GUI.Add.AddUserFrame import AddUserFrame
from GUI.Add.AddCourseFrame import AddCourseFrame
from GUI.Add.AddBookFrame import AddBookFrame

from GUI.Info.GetInfoFrame import GetInfoFrame
from GUI.Info.GetLecturerSalaryFrame import GetLecturerSalaryFrame
from GUI.Info.GetUsersCoursesFrame import GetUsersCoursesFrame

from GUI.Manage.ManageLibraryFrame import ManageLibraryFrame
from GUI.Manage.EditCourseFrame import EditCourseFrame
from GUI.Manage.EditBookFrame import EditBookFrame
from GUI.Manage.SignUserToCourseFrame import SignUserToCourseFrame
from GUI.Manage.LendBookFrame import LendBookFrame
from GUI.Manage.ReturnBookLoanFrame import ReturnBookLoanFrame


class LibraryWindow(tk.Tk):
    def __init__(self, library=None):
        super().__init__()

        self.library = Library() if library is None else library

        self.title('Library System')
        self.geometry('700x600')
        self.resizable(width=False, height=False)

        self.set_window_to_center_of_screen()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others with tkraise().
        container = tk.Frame(self)
        container.pack(expand=True, fill="both", side="top")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frame in (LoginFrame, RegisterFrame, LibraryHubFrame, AddToLibraryFrame, GetInfoFrame, ManageLibraryFrame,
                      AddUserFrame, AddCourseFrame, AddBookFrame, GetLecturerSalaryFrame, GetUsersCoursesFrame,
                      EditCourseFrame, EditBookFrame, SignUserToCourseFrame, LendBookFrame, ReturnBookLoanFrame):
            frame_name = frame.__name__
            self.frames[frame_name] = frame(parent=container, controller=self, library=self.library)

            # Put all the pages in the same location.
            # The one on the top of the stacking order will be the one that is visible.
            self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

        self.show_frame('LoginFrame')

        self.mainloop()

    def set_window_to_center_of_screen(self):
        self.update_idletasks()

        # Get the window values of width and height.
        window_width = self.winfo_width()
        window_height = self.winfo_height()

        # Get the screen values of width and height.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Get the position of the window according to screen size and window size
        position_right = int(screen_width / 2 - window_width / 2)
        position_down = int(screen_height / 2 - window_height / 2)

        # Position the window at the center of the screen.
        self.geometry('+{}+{}'.format(position_right, position_down))

    def show_frame(self, frame_name):
        # Show a frame for the given page name
        self.frames[frame_name].tkraise()

        match frame_name:
            case 'LoginFrame':
                self.title('Login')
            case 'RegisterFrame':
                self.title('Registration')
            case 'LibraryHubFrame':
                self.title('Library Hub')
            case 'AddToLibraryFrame':
                self.title('Add To Library')
            case 'GetInfoFrame':
                self.title('Get Info')
            case 'ManageLibraryFrame':
                self.title('Manage Library')
            case 'AddUserFrame':
                self.title('Add User')
            case 'AddCourseFrame':
                self.title('Add Course')
            case 'AddBookFrame':
                self.title('Add Book')
            case 'GetLecturerSalaryFrame':
                self.title('Lecturer Salary')
            case 'GetUsersCoursesFrame':
                self.title('Users Courses')
            case 'EditCourseFrame':
                self.title('Edit Course')
            case 'EditBookFrame':
                self.title('Edit Book')
            case 'SignUserToCourseFrame':
                self.title('Sign User to Course')
            case 'LendBookFrame':
                self.title('Lend Book')
            case 'ReturnBookLoanFrame':
                self.title('Return Book')
            case _:
                self.title('Library System')
