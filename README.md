# LibrarySystem

Library System
The project is a library system that is controlled by librarian which take the part of the admin. The librarians control information within the library (courses and books) and can add users that are lecturers and students. Librarians give service to the users as their requests, for example a lecturer can ask what his salary is or how many hours a week he works, and the library can pull out that information. 
The GUI of the project was built as one main window and several frames that are set on top of each other in a container when only one at a time is set to the top. 
There are several entities within the project for example “Book”, “Course”, and “Person” which are all handled by a class called Library that saves a list of each of them and has functions to handle them and communicate with the GUI.


How the project works:
Login Screen: the first screen the user runs into is the login screen. It is possible to login with a librarian ID which is set defined as “Librarian” and a number at the end of it. In case the regex of the librarian is incorrect the text will be red, if it is correct, it will be green. In case there are no librarians in the system it is possible to sign up by using the “Register” button.
 
![image](https://user-images.githubusercontent.com/92099051/158687948-e316c86f-cf7f-4e9e-93e3-4885a92d09cd.png)

Register Screen: In the register screen the user (librarian) must fill all the text fields which are ID (9 digits), Name and Surname (starts with upper case letter, end with lower case letter). Once all is complete and the register button has been pressed, a message box will appear with the new librarians “Librarian ID”.
 
![image](https://user-images.githubusercontent.com/92099051/158687925-ffb423f9-9926-4ff7-9174-a95d11dd1211.png)

Library Hub Screen: the librarian can choose 3 options, add things into the library, get info about things in the library, or manage things in the library.
 
![image](https://user-images.githubusercontent.com/92099051/158687911-f7d33da0-8e35-4877-af31-5fed007e5ccd.png)

Add To Library Screen: the librarian can add users, courses and books to the library.
 
![image](https://user-images.githubusercontent.com/92099051/158688041-00dfc702-4010-42a7-ae6c-4f0056465c7d.png)

Add User Screen: the librarian can choose to add a new lecturer or student to the library by filling the required fields and choose courses to sign them up. Once the “Add User” button has been pressed the “Student ID” or ”Lecturer ID” will appear in a message box.

![image](https://user-images.githubusercontent.com/92099051/158688071-674cae6c-be4c-440a-a10e-4224cf12d506.png)
![image](https://user-images.githubusercontent.com/92099051/158688101-3ba1bfa4-8765-440e-b31a-1084c11e4824.png)
 
Add Course Screen: fill the required fields and add a lecturer if it is desired. Once added the “Course ID” will appear in a message box.
 
![image](https://user-images.githubusercontent.com/92099051/158688131-01ae6599-4899-4774-be4b-3fb1dcb8add0.png)

Add Book Screen: fill the required and add a course to relate to if desired. Once added the “Book ID” will appear in a message box.

![image](https://user-images.githubusercontent.com/92099051/158688154-fec22f85-7be0-4e65-bcb8-81236035adeb.png)

Get Info Screen: the librarian can get information about the library. 
“Get All Users” button returns a list of all the librarians, lecturers, and students in the library.
“Get All Courses” button returns a list of all the courses in the library that are assorted according to which lecturer teaches them.
“Get All Books” button returns a list of all the books in the library that are assorted according to which course they belong.
 
 ![image](https://user-images.githubusercontent.com/92099051/158688197-2be97337-4ed6-4a97-972f-35a98ebe2c14.png)
![image](https://user-images.githubusercontent.com/92099051/158688208-4e3dcec6-1e3d-451e-b83f-fb8a65eeb6b6.png)
![image](https://user-images.githubusercontent.com/92099051/158688212-033d76e0-0762-43f5-a348-378080fc2eec.png)
![image](https://user-images.githubusercontent.com/92099051/158688219-179315a6-d785-4933-89a0-9813f8cf74bb.png)
 
Lecturer Salary Screen: the librarian can get the lecturers salary by choosing a lecturer from the combo box and pressing the calculate salary button. The salary is calculated by the number of students the lecturer teaches per hour.

![image](https://user-images.githubusercontent.com/92099051/158688238-e7c66ed2-7559-4c60-9040-79c37f24bc1f.png)

User Courses Screen: the librarian can choose a student or lecturer and get a list of the number of course they are assigned to.

![image](https://user-images.githubusercontent.com/92099051/158688296-7f9f2ed0-8007-4f7c-89a3-a5145a6101a9.png)
![image](https://user-images.githubusercontent.com/92099051/158688271-4845d113-d4bb-4f1b-9db2-8a2bca2501f4.png)

Manage Library Screen: the librarian can manage the library with the buttons seen in the picture.
  
![image](https://user-images.githubusercontent.com/92099051/158688313-a2a45f89-6853-45bc-9fbe-89b656739277.png)

Edit Course Screen: the librarian can edit the number of weekly hours of a course and the lecturer that teaches it.

![image](https://user-images.githubusercontent.com/92099051/158688336-47dba988-8f43-46da-8011-118e937848b2.png)

Edit Book Screen: the librarian can edit the number of copies of a book and the course it is related to.

![image](https://user-images.githubusercontent.com/92099051/158688361-0b5ae70e-abc2-4657-8d31-76bab492f59a.png)

Sign User to Course Screen: the librarian can assign students and lecturers to courses which are selected with check boxes.
 
 ![image](https://user-images.githubusercontent.com/92099051/158688377-ddedae58-1bba-4720-8f00-fe649aec750b.png)
 ![image](https://user-images.githubusercontent.com/92099051/158688412-5e58290d-41b4-4b1a-9520-2790676123b0.png)

Lend Book Screen: the librarian can lend books to students and lecturers; students can loan a book for a week while lecturers can loan for a month.
 
![image](https://user-images.githubusercontent.com/92099051/158688426-f1f2c5a1-562c-415e-86a0-1f6289c1038c.png)

Return Book Screen: if some one has returned a book loan, then the librarian can return the book in the system. Once the button has been pressed the system will calculate if the user must pay a fine for being late, if the user is late the fine will be calculated by a dollar a day.

![image](https://user-images.githubusercontent.com/92099051/158688456-fbcef247-0f1f-449b-ad11-70045926ff11.png)
