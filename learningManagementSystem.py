# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 01:01:18 2019

@author: hplaw
"""

from tkinter import *

root = Tk()
root.geometry("280x120")
root.title("LMS")

def login(event):
    print("Logging in")
    if(usernameEntry.get()=='admin' and passwordEntry.get()=='1234'):
        print("Admin Login")
        viewProfileAdmin()
    elif(usernameEntry.get()=='student' and passwordEntry.get()=='password'):
        print("Student Login")
        viewProfile()
    else:
        print("Invalid login please try again")
 
def displayStudentInfo(entries, studentInfo, root2):
    for i in range(2):
        label = Label(root2, text = entries[i])
        label.grid(row = i, sticky = E)
        label = Label(root2, text = studentInfo[i])
        label.grid(row = i, column = 1, sticky = W)

def displayStudentCourses(entries, studentCourses, root2):
    label = Label(root2, text = "Registered Courses:")
    label.grid(row = 2, sticky = E)
    for i in range(len(studentCourses)):
        label = Label(root2, text = studentCourses[i])
        label.grid(row = 2+i, column = 1, sticky = W)
        
def displayGPA(root2, adjust):
    label = Label(root2, text = "Semester GPA:")
    label.grid(row = 3 + adjust, sticky = E)
    label = Label(root2, text = "some calculated value")
    label.grid(row = 3 + adjust, column = 1, sticky = W)
       
def viewProfile():
    root2 = Tk()
    root2.geometry("450x450")
    root2.title("Student Profile")
    #student’s name, student’s ID, 
    #registered courses in the current semester, 
    #each exam’s score in one course, 
    #GPA calculation in the current semester
    entries = 'Student Name:', 'Student ID:'
    studentInfo = 'UHD Student', '12345'
    studentCourses = 'Intro to computing with python', 'Statistics', 'Database Systems', 'Speech'
    
    displayStudentInfo(entries,studentInfo,root2)
    displayStudentCourses(entries, studentCourses,root2)
    displayGPA(root2,len(studentCourses))
        
        
def viewProfileAdmin():
    root2 = Tk()
    root2.geometry("450x450")
    root2.title("Student Profile")
    #student’s name, student’s ID, 
    #registered courses in the current semester, 
    #each exam’s score in one course, 
    #GPA calculation in the current semester
    entries = 'Student Name:', 'Student ID:','Registered Courses:','Semester GPA:'
    for i in range(len(entries)):
        label = Label(root2, text = entries[i])
        label.grid(row=i, sticky=E)
        entry = Entry(root2)
        entry.grid(row=i, column = 1)
        print(entries[i])
        

mFrame = Frame(root, width=500, height=450)
mFrame.pack()

usernameLabel = Label(mFrame, text= "Username:")
usernameLabel.grid(row=0, sticky=E)
usernameEntry= Entry(mFrame)
usernameEntry.grid(row=0,column=1)
passwordLabel = Label(mFrame, text= "Password:")
passwordLabel.grid(row=1, sticky=E)
passwordEntry = Entry(mFrame)
passwordEntry.grid(row=1,column=1)



loginButton = Button(mFrame, text = "Login")
loginButton.bind("<Button-1>",login)
loginButton.grid(row=3,column=1)


root.mainloop()