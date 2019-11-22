# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 04:02:16 2019

@author: hplaw
"""

from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import sqlite3

conn = sqlite3.connect("student.db")
c = conn.cursor()

class Student:
    
    def __init__(self,sFirstName,sLastName,sID,sCourses):
        self.firstName = sFirstName
        self.lastName = sLastName
        self.studentID = sID
        self.courses = sCourses
    
    def addStudent(self):
        newStudent = Student()
        newStudent.name = sName
        newStudent.studentID = sID
        newStudent.courses = sCourses
        studentList.append(newStudent)
    
    def display(self, s):
        print("Name: ", s.name)
        print("ID: ", s.studentID)
        print("Courses: ", s.courses)
    
    def search(self, sID): 
        for i in range(studentList.__len__()): 
            if(studentList[i].studentID == sID): 
                return i        
                                  
    def delete(self, sID): 
        i = search(sID)   
        del studentList[i] 
    
    def update(self, sID, sName, sCourses): 
        i = search(sID) 
        studentList[i].name = sName
        studentList[i].courses = sCourses

class AdminWindow:
    
    def __init__(self):
#        frame = Frame(master, width=500, height=450)
#        frame.pack()
        frame = Toplevel()
#        
        self.addStudentButton = Button(frame,text="Add a student",command=lambda: self.addStudentPopUp())
        self.addStudentButton.grid(row=0,column=1)
        
        self.searchEntry = Entry(frame)
        self.searchEntry.grid(row=1,column=1)
        self.searchStudentButton = Button(frame,text="Search Student",command=lambda:self.search_student(frame))
        self.searchStudentButton.grid(row=1,column=2)
        
        self.logoutButton = Button(frame, text="Logout",command=lambda: frame.destroy())
        self.logoutButton.grid(row=0,column=2)
        
        
        
    def addStudentPopUp(self):
        frame = Toplevel()
        self.nameLabel = Label(frame,text="Student Name: ")
        self.passLabel = Label(frame,text="Student Password: ")
        self.idLabel = Label(frame,text="Student ID: ")
        self.nameEntry = Entry(frame)
        self.passEntry = Entry(frame)
        self.idEntry = Entry(frame)
        self.saveButton = Button(frame,text="Save",width=7,command=lambda: [self.updateRecords(),frame.destroy()])     #save to database,print message, close window
        self.cancelButton = Button(frame, text = "Cancel",width=7,command=frame.destroy)
        
        self.nameLabel.grid(row=2,column=1)
        self.nameEntry.grid(row=2,column=2)
        self.passLabel.grid(row=3,column=1)
        self.passEntry.grid(row=3,column=2)
        self.idLabel.grid(row=4,column=1)
        self.idEntry.grid(row=4,column=2)
        self.saveButton.grid(row=5,column=2,sticky=W)
        self.cancelButton.grid(row=5,column=2,sticky=E)
        

    def search_student(self,frame):
        self.listbox = Listbox(frame, width=30, height=10,)
        self.listbox.grid(row=6, column=1)
        self.listbox.config(state=NORMAL)
        self.listbox.delete('0',END)
        with conn:
            s_id=self.searchEntry.get()
            c.execute("SELECT * FROM student WHERE student_id= ?",(s_id,))
          
            conn.commit()
            records = c.fetchone()
            
            c.execute("SELECT * FROM courses WHERE student_id= ?",(s_id,))
            
            conn.commit()
            courses = c.fetchall()
            
            print(courses)
#            query_label=Label(frame,text= print_record)
#            query_label.grid(row=6, column=1)
            
            #f_name.delete(0,END)
            print(records[0])
            print(records[1])
            print(records[2])
            print_record=''
            label = []
            labels = ['Student ID: ','First Name: ','Last Name: ']
            course_list = []
            
            
            for i in range (len(records)):
#               print_record+=(record)+"\n"
                self.listbox.insert('end',labels[i]+records[i])
            self.listbox.insert('end',"Courses: ")
            
            for i in range (len(courses)):
                self.listbox.insert('end',courses[i][1] +" " +courses[i][2])
                course_list.append(courses[i][1] +" " +courses[i][2])
            print(course_list)    
            
            #s = Student(records[1],records[2],records[0],course_list)
            
            view_grades_button = Button(frame,text="View Grades",command=lambda: self.view_grades_window(course_list,records[0]))
            view_grades_button.grid(row = 6,column=2,sticky=S)
            #l_name.delete(0,END)
            #student_id.delete(0,END)
            #course_id.delete(0,END)
            #add_grade.delete(0,END)
            #return records
    
    def view_grades_window(self,records,courses):
        frame = Toplevel()
        self.course_label = Label(frame,text="Course ID: ")
        self.course_combobox = ttk.Combobox(frame,value=courses)
        self.course_label.grid(row=0,column=0)
        self.course_combobox.grid(row=0,column=1)
        self.addCourseButton = Button(frame,text="Add Course",command=lambda: add_grades(combobox.get(),student_id,))
        
        #assignment entry
        self.assignmentLabel = Label(frame,text="")
    
    #def add_grades_window(self,courses,student_id):
        
        #grade entry
    def add_grades(student_id,course_id):
    
        with conn:
            s_id=student_id
            c_id=course_id
            g= int(add_grade.get())
            
    
            #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
            c.execute("INSERT INTO grades (student_id,course_id,grades) values (?,?,?)",
                    (s_id,c_id,g))
            
            conn.commit()
            
    
    def updateRecords(self):
        print("updating records")


        
class StudentWindow:
    
    def __init__(self, master):
        frame = Frame(master, width=500, height=450)
        frame.pack()
        
                     
class LoginWindow:
    
    def __init__(self, master):
        frame = Frame(master, width=500, height=450)
        frame.pack()

        self.usernameLabel = Label(frame, text= "Username:")
        self.usernameLabel.grid(row=0, sticky=E)
        self.usernameEntry= Entry(frame)
        self.usernameEntry.grid(row=0,column=1)
        self.usernameEntry.bind("<Return>",self.loginEnterKey)
        
        self.passwordLabel = Label(frame, text= "Password:")
        self.passwordLabel.grid(row=1, sticky=E)
        self.passwordEntry = Entry(frame)
        self.passwordEntry.grid(row=1,column=1)
        self.passwordEntry.bind("<Return>",self.loginEnterKey)  
        
        self.loginButton = Button(frame, text = "Login", command=self.loginButton)
        self.loginButton.grid(row=3,column=1)
    
    def loginButton(self):
        print("Logging in")
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        
        with sqlite3.connect("student.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM users WHERE id= ? AND password = ?")      #from users table in student.db
        cursor.execute(findUser,[(username),(password)])                #two entries so far in users:
        results = cursor.fetchall()                                     #username: "student1", password:"password", access:"student"
        
        if results:                                                     #username: "admin1", password:"1234", access:"admin"
            for i in results:
                if i[3] == "student":
                    print("Student Login")
                    studentWindow = StudentWindow(Tk())
                elif i[3] == "admin":
                    print("Admin Login")
                    adminWindow = AdminWindow()
        else:
            print("Invalid login please try again")
 
        
    def loginEnterKey(self,event):
        print("Logging in")
        
        if(self.usernameEntry.get()=='admin' and self.passwordEntry.get()=='1234'):
            print("Admin Login")     
            #viewProfileAdmin()
        elif(self.usernameEntry.get()=='student' and self.passwordEntry.get()=='password'):
            print("Student Login")
            #viewProfile()
        else:
            print("Invalid login please try again")    

    
def main():

    root = Tk()
    root.title("LMS")
    root.geometry("240x120")
    login = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()