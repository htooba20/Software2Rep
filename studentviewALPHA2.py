# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
import sqlite3

conn = sqlite3.connect("student.db")
c = conn.cursor()


def search_student():
   
   with conn:
        s_id=student_id.get()
        c.execute("SELECT * FROM student WHERE student_id= ?",(s_id,))
      
        conn.commit()
        records= c.fetchone()
        print(records)
        print_record=''
        
        for record in records:
           print_record+=(record)+"\n"
           
        listbox.insert('end', records)
           
           
        #query_label=Label(root2,text= print_record)
        #query_label.grid(row=6, column=1)
        
        f_name.delete(0,END)
        l_name.delete(0,END)
        student_id.delete(0,END)
        course_id.delete(0,END)
        add_grade.delete(0,END)



def add_newStudent():
    
    
    with conn:
        s_id= student_id.get()
        firstName= f_name.get()
        lastName= l_name.get()
        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO STUDENT (student_id,first_name, last_name) values (?, ?, ?)",
                (s_id, firstName, lastName))
        
        #query_label=Label(root2,text= "student records added")
        #query_label.grid(row=6, column=1)
        
        f_name.delete(0,END)
        l_name.delete(0,END)
        student_id.delete(0,END)
        course_id.delete(0,END)
        add_grade.delete(0,END)
    
def search_student():
   listbox.delete('0',END)
   with conn:
        s_id=student_id.get()
        c.execute("SELECT * FROM student WHERE student_id= ?",(s_id,))
      
        conn.commit()
        records= c.fetchone()
        print(records)
        print_record=''
        
        for record in records:
           print_record+=(record)+"\n"
           
        listbox.insert('end', records)
           
           
        #query_label=Label(root2,text= print_record)
        #query_label.grid(row=6, column=1)
        
        f_name.delete(0,END)
        l_name.delete(0,END)
        student_id.delete(0,END)
        course_id.delete(0,END)
        add_grade.delete(0,END)
        
        
        return records
    
def census():
   listbox.delete('0',END)
  
   with conn:
        var=course_id.get()
        records=c.execute("""SELECT student.student_id, first_name, last_name
        FROM Student
        INNER JOIN enrollment ON student.student_id = enrollment.student_id where course_id=? """,(var,))
      
        conn.commit()
        records= c.fetchall()
        print(records)
        print_record=''
    
        
        for record in records:
            print_record+=str(record[0])+" "+str(record[1])+" "+str(record[2])+"\n"
            listbox.insert('end', print_record)
            print_record=''
        
      #  print(print_record)
       # listbox.insert('end', print_record)
        
       # for record in records:
        #   print_record+=str(record[0])+" "+str(record[1])+"\n"
           
        #query_label=Label(root2,text= print_record)
        #query_label.grid(row=6, column=1)
        
        
        f_name.delete(0,END)
        l_name.delete(0,END)
        student_id.delete(0,END)
        course_id.delete(0,END)
        add_grade.delete(0,END)
        
        
        return records
    
def view_grades_A():
   listbox.delete('0',END)
   with conn:
        var=course_id.get()
        records=c.execute("""SELECT student.student_id, first_name, last_name,grades
        FROM Student
        INNER JOIN grades ON student.student_id = grades.student_id WHERE course_id=?
        order by student.student_id""",(var,))
      
        conn.commit()
        records= c.fetchall()
        print(records)
        print_record=''
        
        for record in records:
            print_record+=str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+"\n"
            listbox.insert('end', print_record)
            print_record=''
        
      
       
           
        
        
        f_name.delete(0,END)
        l_name.delete(0,END)
        student_id.delete(0,END)
        course_id.delete(0,END)
        add_grade.delete(0,END)
        
        
        return records
      
        
def tabletest():
   
    
    for row in rows:
        print(row)
        
def delete_student():
    with conn:
        student_id=input("enter studentID to delete student records")
        c.execute('DELETE FROM student WHERE student_id=?',(student_id,))
        conn.commit()
        
def update_studentinfo():
    with conn:
        student_id= input("enter student id of the student you want to update information on")
        new_value= input("enter new value?")
        #c.execute('''UPDATE student SET first_name = ? WHERE student_id = ?''', (newPrice, book_id))
        c.execute('''UPDATE student SET first_name = ? WHERE student_id = ?''', (new_value, student_id))
        conn.commit()
        
def add_newclass():
    with conn:
        c_id= input("please enter class id number")
        className= input("enter class name")
        credits=input("enter amount of hours for this class")
        instructorName= input("enter instructor name")
        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO course (course_id,course_name, credit_hour, instructor_name) values (?, ?, ?,?)",
                (c_id, className, credits, instructorName))
        
def tabletestClass():
    c.execute("SELECT* FROM course")
    rows=c.fetchall()
    
    for row in rows:
        print(row)
        
def add_instructor():
    with conn:
        fname= input("please enter instructor name")
        lname= input("instructor last name")
        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO instructor (instructor_name, instructor_lastname) values (?, ?)",
                (fname,lname))
        

def tabletestI():
    c.execute("SELECT* FROM instructor")
    rows=c.fetchall()
    
    for row in rows:
        print(row)
        
def add_grades():
    
    with conn:
        s_id= input("enter student id u want ot add grade for")
        c_id =input("insert course number for the grade")
        g=input("insert grade letter")
        if g == 'a' or g == 'A':
            g='A'
        if g == 'B' or g == 'b':
            g='B'
        if g == 'c' or g == 'C':
            g='C'
        if g == 'd' or g == 'D':
            g='D'
        if g == 'c' or g == 'C':
            g='C'

        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO enrollment (student_id,course_id,grade) values (?,?,?)",
                  (s_id,c_id,g))
        


        
def obtain_grades():
    
    with conn:
        s_id= input("enter student id u want to obtain grades from")
        c_id =input("insert course number for course u want to look grades for")
        

        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("SELECT student_id, course_id, grades FROM grades WHERE student_id =? AND course_id=?",(s_id,c_id,))
               
        grades= c.fetchall()
        return grades
    
def obtain_finalGrade():
    
    with conn:
        s_id= input("enter student id u want to obtain finalgrade from")
        c_id =input("insert course number you want for final grade")
        

        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("SELECT SUM(grades) FROM grades WHERE student_id =? AND course_id=?",(s_id,c_id,))
               
        tupels= c.fetchone()
        finalGrade=tupels[0]
        grade=finalGrade
        return grade/3
    
def obtain_finalLetter():
    
    with conn:
        s_id= input("enter student id u want to obtain final letter from")
        c_id =input("insert course number you want final letter from")
        

        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("SELECT SUM(grades) FROM grades WHERE student_id =? AND course_id=?",(s_id,c_id,))
               
        tupels= c.fetchone()
        finalGrade=tupels[0]
        grade=finalGrade/3
        
        if grade >= 89.5:
            grade_letter='A'
        if grade >= 79.5 and grade < 89.5:
            grade_letter='B'
        if grade >= 69.5 and grade <79.5:
            grade_letter='C'
        if grade >= 59. and grade <59.5:
            grade_letter='D'
            
        return grade_letter
        
    
def tabletestE():
    c.execute("SELECT* FROM grades")
    rows=c.fetchall()
    
    for row in rows:
        print(row)
        
def tabletestG():
    c.execute("SELECT* FROM grades")
    rows=c.fetchall()
    
    for row in rows:
        print(row)
        
        
def add_grades2():
    
    with conn:
        s_id=student_id.get()
        c_id=course_id.get()
        g= int(add_grade.get())
        

        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO grades (student_id,course_id,grades) values (?,?,?)",
                (s_id,c_id,g))
        
        conn.commit()
        
        #conn.close()
        
        f_name.delete(0,END)
        student_id.delete(0,END)
        course_id.delete(0,END)
        add_grade.delete(0,END)
        
        
        
def add_view_grades_window():
    root3=Tk()
    root3.title('test//')
    root3.geometry("450x450")
   
    global student_id3
    global course_id3
    global add_grade3
        
        ## TEXT BOXES

    
    student_id3= Entry(root3)
    student_id3.grid(row=0,column=1)
    
    course_id3= Entry(root3)
    course_id3.grid(row=1,column=1)
    
    add_grade3= Entry(root3)
    add_grade3.grid(row=2,column=1)
    
    ### TEXT BOXES LABELS

    student_id_label3=Label(root3, text="Student ID")
    student_id_label3.grid(row=0,column=0)
    course_id_label3=Label(root3, text="Course ID")
    course_id_label3.grid(row=1,column=0)
    grade_label3=Label(root3, text="grade to add")
    grade_label3.grid(row=2,column=0)
    
    

        
        ##BUTTONS 
    view_student_gradesbtn=Button(root3, text="view student grade", command=view_grades_A)
    view_student_gradesbtn.grid(row=5, column=3)
    
    view_student_gradesbtna=Button(root3, text="view all grades", command=view_grades_A)
    view_student_gradesbtna.grid(row=5, column=2)

        
    addGrades_btn=Button(root3, text="add grades",command=add_grades2)
    addGrades_btn.grid(row=5, column=0)
        
tabletestE()
#search_student()

def student():
   listbox.delete('0',END)
  
   with conn:
        var=student_id.get()
        records=c.execute("""SELECT student.student_id, first_name, last_name
        FROM Student
        INNER JOIN grades ON student.student_id = enrollment.student_id where student_id=? """,(var,))
      
        conn.commit()
        records= c.fetchone()
        print(records)
        print_record=''
    
        
        for record in records:
            print_record+=str(record[0])+" "+str(record[1])+" "+str(record[2])+"\n"
            listbox.insert('end', print_record)
            print_record=''
            
        var=student_id.get()
        records=c.execute("""SELECT course_id, grades
        FROM Student
        INNER JOIN grades ON student.student_id = enrollment.student_id where student_id=? order by course_id """,(var,))
      
        conn.commit()
        
        
        for record in records:
            print_record+=str(record[0])+" "+str(record[1])+" "+str(record[2])+"\n"
            listbox.insert('end', print_record)
            print_record=''
        
    
        
        
        f_name.delete(0,END)
        l_name.delete(0,END)
        student_id.delete(0,END)
        course_id.delete(0,END)
        add_grade.delete(0,END)
        
        
        return records
    
def student_select():
   listbox.delete('0',END)
  
   with conn:
       ##hard coded right here
        var='s1'
        var2=course_id.get()
        records=c.execute("""SELECT grades
        FROM grades where student_id=? AND course_id =?""",(var,var2,))
      
        conn.commit()
        records= c.fetchall()
        print(records)
        print_record=''
    
        listbox.insert('end',"the following are you grades in "+course_id.get())
        for record in records:
            print_record+=str(record[0])+"\n"
            listbox.insert('end', print_record)
            print_record=''
            
        listbox.insert('end',"you're final grade is ")
       
        
        c.execute("SELECT SUM(grades) FROM grades WHERE student_id =? AND course_id=?",(var,var2,))
        
        str_total=""
        tupels= c.fetchone()
        finalGrade=tupels[0]
        grade=finalGrade
        total= grade/3
        print(total)
        str_total= str(total)
        
        listbox.insert('end',str_total)
        grade_letter=''
        
        if total >= 89.5:
            grade_letter='A'
        if total >= 79.5 and grade < 89.5:
            grade_letter='B'
        if total >= 69.5 and grade <79.5:
            grade_letter='C'
        if total >= 59. and grade <59.5:
            grade_letter='D'
            
        print(grade_letter)
            
        listbox.insert('end',"your grade letter is: ")
        listbox.insert('end',grade_letter)
        
      
       
        
        
        
    
       
     
    
        
        f_name.delete(0,END)
        l_name.delete(0,END)
        student_id.delete(0,END)
        course_id.delete(0,END)
        add_grade.delete(0,END)
        
        
        return records
    

####################################GUI##############################################root = Tk()



   
root2=Tk()
root2.title('test')
root2.geometry("400x300")
   

        
        
        ##williams code###
        
        
        ## TEXT BOXES
f_name= Entry(root2)
f_name.grid(row=0,column=1)


l_name= Entry(root2)
l_name.grid(row=1,column=1)
    
student_id= Entry(root2)
student_id.grid(row=2,column=1)
    
course_id= Entry(root2)
course_id.grid(row=3,column=1)
    
add_grade= Entry(root2)
add_grade.grid(row=4,column=1)
    
    ### TEXT BOXES LABELS
f_name_label=Label(root2, text="First name", padx=20)
f_name_label.grid(row=0,column=0)
l_name_label=Label(root2, text="last name")
l_name_label.grid(row=1,column=0)
student_id_label=Label(root2, text="Student ID")
student_id_label.grid(row=2,column=0)
course_id_label=Label(root2, text="Course ID")
course_id_label.grid(row=3,column=0)
grade_label=Label(root2, text="grade to add")
grade_label.grid(row=4,column=0)
    
    

        
        ##BUTTONS 
add_student_btn=Button(root2, text="view grades", command=student_select)
add_student_btn.grid(row=0, column=3)

        


# create the listbox (height/width in char)
listbox = Listbox(root2, width=36, height=10,)
listbox.grid(row=6, column=1)
listbox.config(state=NORMAL)

# create a vertical scrollbar to the right of the listbox
#yscroll = Scrollbar(command=listbox.yview, orient=VERTICAL)
#yscroll.grid(row=12, column=1, sticky='ns')
#listbox.configure(yscrollcommand=yscroll.set)

# student profile
with conn:
        s_id='s1'
        c.execute("SELECT * FROM student WHERE student_id= ?",(s_id,))
      
        conn.commit()
        records= c.fetchone()
        print(records)
        print_record=''
        
        for record in records:
           print_record+=(record)+"\n"
        listbox.insert('end','welcome')  
        listbox.insert('end', records)
        listbox.insert('end',"you're currently enrolled in")
        
     
       ##hard coded right here
        var='s1'
        records=c.execute("""SELECT course_id
        FROM enrollment
        where student_id=? """,(var,))
      
        conn.commit()
        records= c.fetchall()
        print(records)
        print_record=''
    
        
        for record in records:
            print_record+=str(record[0])+"\n"
            listbox.insert('end', print_record)
            print_record=''
            
      
            
        





root2.mainloop()