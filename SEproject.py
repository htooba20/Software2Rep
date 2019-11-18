# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 04:02:16 2019

@author: hplaw
"""

from tkinter import *
import sqlite3


class LoginWindow:
    
    def __init__(self, master):
        frame = Frame(master, width=500, height=450)
        frame.pack()

        self.usernameLabel = Label(frame, text= "Username:")
        self.usernameLabel.grid(row=0, sticky=E)
        self.usernameEntry= Entry(frame)
        self.usernameEntry.grid(row=0,column=1)
        self.passwordLabel = Label(frame, text= "Password:")
        self.passwordLabel.grid(row=1, sticky=E)
        self.passwordEntry = Entry(frame)
        self.passwordEntry.grid(row=1,column=1)
        self.passwordEntry.bind("<Return>",self.loginEnterKey)
#        loginButton = Button(frame, text = "Login")
#        loginButton.bind("<Button-1>",login)
#        loginButton.grid(row=3,column=1)       
        self.loginButton = Button(frame, text = "Login", command=self.login)
        #self.loginButton.bind("<Button-1>",self.login)
        self.loginButton.grid(row=3,column=1)
        
    def printMessage(self):
        print("Function works")
    
    def login(self):
        print("Logging in")
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        
        with sqlite3.connect("student.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM users WHERE username = ? AND password = ?")      #from users table in student.db
        cursor.execute(findUser,[(username),(password)])                #two entries so far in users:
        results = cursor.fetchall()                                     #username: "student1", password:"password", access:"student"
        if results:                                                     #username: "admin1", password:"1234", access:"admin"
            for i in results:
                if i[3] == "student":
                    print("Student Login")
                elif i[3] == "admin":
                    print("Admin Login")
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

        
root = Tk()
root.title("LMS")
root.geometry("240x120")
login = LoginWindow(root)
root.mainloop()