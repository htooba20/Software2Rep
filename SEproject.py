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

#class Student:
#    
#    def __init__(self,sFirstName,sLastName,sID,sCourses):
#        self.firstName = sFirstName
#        self.lastName = sLastName
#        self.studentID = sID
#        self.courses = sCourses
#    
#    def addStudent(self):
#        newStudent = Student()
#        newStudent.name = sName
#        newStudent.studentID = sID
#        newStudent.courses = sCourses
#        studentList.append(newStudent)
#    
#    def display(self, s):
#        print("Name: ", s.name)
#        print("ID: ", s.studentID)
#        print("Courses: ", s.courses)
#    
#    def search(self, sID): 
#        for i in range(studentList.__len__()): 
#            if(studentList[i].studentID == sID): 
#                return i        
#                                  
#    def delete(self, sID): 
#        i = search(sID)   
#        del studentList[i] 
#    
#    def update(self, sID, sName, sCourses): 
#        i = search(sID) 
#        studentList[i].name = sName
#        studentList[i].courses = sCourses

class AdminWindow:
    
    
    student_id = ""
    course_id = ""
    courses=[]
    assignments=[]
    grades = []
    
    
    def __init__(self):
#        frame = Frame(master, width=500, height=450)
#        frame.pack()
        frame = Toplevel()
#        
        self.addStudentButton = Button(frame,text="Add a student",command=lambda: self.add_student_window())
        self.addStudentButton.grid(row=0,column=1)
        
        self.add_course_button = Button(frame,text="Add a course",command=lambda: self.add_course_window())
        self.add_course_button.grid(row=1,column=1)
        
        self.searchEntry = Entry(frame)
        self.searchEntry.grid(row=2,column=1)
        self.searchStudentButton = Button(frame,text="Search Student",command=lambda:self.search_student(frame))
        self.searchStudentButton.grid(row=2,column=2)
        
        self.logoutButton = Button(frame, text="Logout",command=lambda: frame.destroy())
        self.logoutButton.grid(row=0,column=2)
    
        
    def set_student_id(self,s_id):
        self.student_id = s_id
        
    def set_course_id(self,c_id):
        self.course_id = c_id
    
    def set_assignments(self,s_id,c_id):
        c.execute("SELECT * FROM grades WHERE student_id= ? AND course_id = ?",(s_id,c_id))
        conn.commit()
        results = c.fetchall()
        assignments=[]
        print(results)
        for i in range(len(results)):
            assignments.append(results[i][3])
        return assignments
    def get_grades(self,s_id,c_id):
        c.execute("SELECT * FROM grades WHERE student_id= ? AND course_id = ?",(s_id,c_id))
        conn.commit()
        results = c.fetchall()
        return results
    
    def get_courses(self,s_id):
        c.execute("SELECT * FROM enrollment WHERE student_id= ?",(s_id,))
        conn.commit()
        results = c.fetchall()
        return results
    
    def get_univ_courses(self):
        c.execute("SELECT * FROM courses")
        conn.commit()
        results = c.fetchall()
        return results
        
        
    def add_student_window(self):
        frame = Toplevel()
        self.first_name_label = Label(frame,text="First Name: ")
        self.last_name_label = Label(frame,text="Last Name: ")
        self.pass_label = Label(frame,text="Student Password: ")
        self.id_label = Label(frame,text="Student ID: ")
        self.first_name_entry = Entry(frame)
        self.last_name_entry = Entry(frame)
        self.pass_entry = Entry(frame)
        self.id_entry = Entry(frame)
        self.saveButton = Button(frame,text="Save",width=7,command=lambda: [self.check_student_entries("a","b","c","d"),
                                                                            frame.destroy()])    
        self.cancelButton = Button(frame, text = "Cancel",width=7,command=frame.destroy)
        
        self.first_name_label.grid(row=2,column=1)
        self.first_name_entry.grid(row=2,column=2)
        self.last_name_label.grid(row=3,column=1)
        self.last_name_entry.grid(row=3,column=2)
        self.pass_label.grid(row=4,column=1)
        self.pass_entry.grid(row=4,column=2)
        self.id_label.grid(row=5,column=1)
        self.id_entry.grid(row=5,column=2)
        self.saveButton.grid(row=6,column=2,sticky=W)
        self.cancelButton.grid(row=6,column=2,sticky=E)
    
    def check_student_entries(self,f_name,l_name,s_id,password):
        #this funciton will check entries and call another function to add values to database under student and users
        print("checking function call")
        print(f_name,l_name,s_id,password)
        
        
    
    def add_course_window(self):
        frame = Toplevel()
        self.c_name_label = Label(frame,text="Course Name: ")
        self.c_id_label = Label(frame,text="Course ID: ")
        self.c_hr_label = Label(frame,text="Credit Hours: ")
        self.instructor_label = Label(frame,text="Instructor: ")
        self.c_name_entry = Entry(frame)
        self.c_hr_entry = Entry(frame)
        self.c_id_entry = Entry(frame)
        self.instructor_entry= Entry(frame)
        self.saveButton = Button(frame,text="Save",width=7,command=lambda: [self.updateRecords(),frame.destroy()])     #save to database,print message, close window
        self.cancelButton = Button(frame, text = "Cancel",width=7,command=frame.destroy)
        
        self.c_name_label.grid(row=2,column=1)
        self.c_name_entry.grid(row=2,column=2)
        self.c_id_label.grid(row=3,column=1)
        self.c_id_entry.grid(row=3,column=2)
        self.c_hr_label.grid(row=4,column=1)
        self.c_hr_entry.grid(row=4,column=2)
        self.instructor_label.grid(row=5,column=1)
        self.instructor_entry.grid(row=5,column=2)
        self.saveButton.grid(row=6,column=2,sticky=W)
        self.cancelButton.grid(row=6,column=2,sticky=E)
    
        

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
            
            c.execute("SELECT * FROM enrollment WHERE student_id= ?",(s_id,))
            
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
                course_list.append(courses[i][1])
            print(course_list)    
            
            #s = Student(records[1],records[2],records[0],course_list)
            
            view_grades_button = Button(frame,text="View Grades",command=lambda: self.view_grades_window(records[0],course_list))
            view_grades_button.grid(row = 6,column=2,sticky=S)
            
            view_courses_button = Button(frame,text="View Courses",command=lambda: self.view_courses_window(records[0]))
            view_courses_button.grid(row=6,column=2)
            #l_name.delete(0,END)
            #student_id.delete(0,END)
            #course_id.delete(0,END)
            #add_grade.delete(0,END)
            #return records
    def view_courses_window(self,student_id):
        frame = Toplevel()
        coursesLabel = Label(frame,text="Courses")
        coursesLabel.grid(row=0,column=0,sticky=N)
        self.show_courses(frame,student_id)
        
        
        drop_course_button = Button(frame,text="Drop Course",command=lambda: [self.drop_course(student_id,self.listbox.index(ACTIVE)),self.show_courses(frame,student_id),self.listbox.select_set(0)])
        drop_course_button.grid(row=0,column=0)
        
        courses = []
        courses = self.get_univ_courses()
        courselist_label = Label(frame,text="Course list:")
        course_combobox= ttk.Combobox(frame,value = courses,width=40)
        enroll_button = Button(frame,text = "Enroll",command=lambda: [self.enroll(student_id,courses[course_combobox.current()]),self.show_courses(frame,student_id)])
        
        courselist_label.grid(row=0,column=2,sticky=N)
        course_combobox.grid(row=0,column=2)
        enroll_button.grid(row=0,column=2,sticky=S)
        
    def drop_course(self,student_id,i):
        courses = []
        courses = self.get_courses(student_id)
        course_id = courses[i][1]
        with conn:
            c.execute("DELETE FROM enrollment WHERE student_id = ? and course_id = ?",
                    (student_id,course_id))
            conn.commit()
        #self.show_grades(frame,student_id,course_id)
        
    def enroll(self,student_id,course):
        with conn:
            c_id = course[0]
            c_name = course[1]
            c_hour = course[2]
            c_instructor = course[3]
            
            c.execute("INSERT INTO enrollment (student_id,course_id,course_name,credit_hour,instructor) values (?,?,?,?,?)",
                    (student_id,c_id,c_name,c_hour,c_instructor))
            
            conn.commit()
            
                
    def show_courses(self,frame,student_id):
        self.listbox = Listbox(frame, width=50,height=10,)
        self.listbox.grid(row=0, column=1)
        self.listbox.config(state=NORMAL)
        self.listbox.delete('0',END)
        
        courses = []
        courses = self.get_courses(student_id)
        print(courses)
        
        for i in range (len(courses)):
#               print_record+=(record)+"\n"
                self.listbox.insert('end',courses[i][1] + "    "+(courses[i][2]) + "    "+str(courses[i][3]) +"    "+courses[i][4])
        self.listbox.select_set(0)
        return self.listbox
                
        
        
    
    def view_grades_window(self,student_id,course_list):
        frame = Toplevel()
        self.course_label = Label(frame,text="Course ID: ")
        self.course_combobox = ttk.Combobox(frame,value=course_list)
        self.course_label.grid(row=0,column=0)
        self.course_combobox.grid(row=0,column=1)
        self.add_grade_button = Button(frame,text="Add/Remove Grades",command=lambda: self.add_grades_window(self.course_combobox.get(),student_id))
        self.add_grade_button.grid(row=1,column=1)
        
        #assignment entry
    def add_grades_window(self,course_id,student_id):
        frame = Toplevel()
        self.set_course_id(course_id)
        self.a_label = Label(frame,text="Assignment Name")
        self.a_entry = Entry(frame)
        self.g_label = Label(frame,text = "Grade: ")
        self.g_entry = Entry(frame)
        self.add_button = Button(frame,text="Add Grade",command=lambda: [self.add_grades(course_id,student_id,self.a_entry.get(),self.g_entry.get()),self.show_grades(frame,student_id,course_id)])
        
        self.a_label.grid(row=0,column=0)
        self.a_entry.grid(row=0,column=1)
        self.g_label.grid(row=1,column=0)
        self.g_entry.grid(row=1,column=1)
        self.add_button.grid(row=2,column=1)
        self.show_grades(frame,student_id,course_id)
    #def add_grades_window(self,courses,student_id):
    
        self.r_label = Label(frame,text="Remove Grades: ")
        self.set_assignments(student_id,course_id)
        #self.g_combobox = ttk.Combobox(frame,value = self.assignments)
        self.remove_button = Button(frame, text="Delete",command=lambda: [self.remove_grades(frame,student_id,course_id,self.L.index(ACTIVE))])
        self.r_label.grid(row=4,column=0,stick=N)
        #self.g_combobox.grid(row=3,column=1)
        self.remove_button.grid(row=4,column=0)
        
        #grade entry
        
    def show_grades(self,frame,student_id,course_id):
        
#        self.listbox = Listbox(frame, width=30, height=10,)
#        self.listbox.grid(row=7, column=1)
#        self.listbox.config(state=NORMAL)
#        self.listbox.delete('0',END)   
        grades = []
        grades = self.get_grades(student_id,course_id)
        
        self.s = Scrollbar(frame)
        self.L = Listbox(frame)
        
        self.s.grid(row=4,column=2,sticky=NS)
        self.L.grid(row=4,column=1,sticky=E)
        self.L.config(state=NORMAL)
        self.L.delete('0',END)
        
        
        self.s['command'] = self.L.yview
        self.L['yscrollcommand'] = self.s.set
        
        for i in range(len(grades)): 
           self.L.insert(END, grades[i][3]+":\t"+str(grades[i][2]) )
        print(grades)
        return self.L
    
    def add_grades(self,course_id,student_id,assignment,grade):
    
        with conn:
            s_id = student_id
            c_id = course_id
            g = grade
            a = assignment
            
            c.execute("INSERT INTO grades (student_id,course_id,grades,assignment) values (?,?,?,?)",
                    (s_id,c_id,g,a))
            
            conn.commit()
            
            
    def remove_grades(self,frame,student_id,course_id,i):
        
        grades = []
        grades = self.get_grades(student_id,course_id)
        print("printing grades table")
        print(grades)
        assignment = grades[i][3]
        with conn:
            c.execute("DELETE FROM grades WHERE assignment = ? and student_id = ?",
                    (assignment,student_id))
            conn.commit()
        self.show_grades(frame,student_id,course_id)


        
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