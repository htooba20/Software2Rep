
# coding: utf-8

# In[1]:


#creation of relational database
#creation of relational database
import sqlite3

conn = sqlite3.connect("student.db")
c = conn.cursor()

try:
    
    c.execute('''CREATE TABLE student (
        student_id text PRIMARY KEY NOT NULL,
        first_name text NOT NULL,
        last_name text NOT NULL,
       FOREIGN KEY (student_id) REFERENCES course(student_id) )''')
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])  # table already exists

conn.commit()

try:
    c.execute('''CREATE TABLE course (
        course_id text PRIMARY KEY NOT NULL,
        course_name text NOT NULL,
        credit_hour int NOT NULL,
        instructor_name test NOT NULL,
       FOREIGN KEY (instructor_name) REFERENCES instructor(instructor_name),
       FOREIGN KEY (course_id) REFERENCES enrollment(course_id))''')
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])  # table already exists

conn.commit()

try:
    c.execute('''CREATE TABLE enrollment (
        student_id text NOT NULL,
        course_id text NOT NULL,
        grade text NOT NULL,
        FOREIGN KEY (student_id) REFERENCES student (student_id),
       fOREIGN KEY (course_id) REFERENCES enrollment(course_id))''')
    
        
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])  # table already exists

conn.commit()

try:
    c.execute('''CREATE TABLE instructor (
        instructor_name text PRIMARY KEY NOT NULL,
        instructor_lastname NOT NULL,
       FOREIGN KEY (instructor_name) REFERENCES course(instructor_name) )''')
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])  # table already exists

conn.commit()

try:
    c.execute('''CREATE TABLE grades (
        student_id text  NOT NULL,
        course_id NOT NULL,
       grades REAL )''')
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])  # table already exists

conn.commit()

try:
    c.execute('''CREATE TABLE passwordS (
        student_id text PRIMARY KEY NOT NULL,
        password NOT NULL )''')
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])  # table already exists

conn.commit()

try:
    c.execute('''CREATE TABLE passwordI (
        instructor_name text PRIMARY KEY NOT NULL,
        password NOT NULL )''')
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])  # table already exists

conn.commit()


# In[ ]:


def add_newStudent():
    with conn:
        s_id= input("please enter new id number")
        firstName= input("enter first name")
        lastName= input("enter last name")
        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO STUDENT (student_id,first_name, last_name) values (?, ?, ?)",
                (s_id, firstName, lastName))
    
def search_student():
    with conn:
        student_id=input("enter student ID you want to search")
        c.execute("SELECT * FROM student WHERE student_id= ?",(student_id,))
        conn.commit()
        return c.fetchone()
    
def tabletest():
    c.execute("SELECT* FROM student")
    rows=c.fetchall()
    
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
        fname= input("please enter instructor first name")
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
        
def add_grades2():
    
    with conn:
        s_id= input("enter student id u want ot add grade for")
        c_id =input("insert course number for the grade")
        g=input("insert grade ")
        

        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO grades (student_id,course_id,grades) values (?,?,?)",
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
    c.execute("SELECT* FROM enrollment")
    rows=c.fetchall()
    
    for row in rows:
        print(row)
        
def tabletestG():
    c.execute("SELECT* FROM grades")
    rows=c.fetchall()
    
    for row in rows:
        print(row)
        
def add_passwordS():
    with conn:
        s_id= input("please enter student_id")
        passwords= input("enter password")
        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO passwordS (student_id, password) values (?, ?)",
                (s_id,passwords))
        
def add_passwordI():
    with conn:
        s_id= input("please enter instrucor name")
        passwords= input("enter password")
        #c.execute("INSERT INTO students VALUES('studentId', 'firstName', 'lastName')")
        c.execute("INSERT INTO passwordI (instructor_name, password) values (?, ?)",
                (s_id,passwords))

def tabletestPS():
    c.execute("SELECT* FROM passwordS")
    rows=c.fetchall()
    
    for row in rows:
        print(row)
        
def tabletestPI():
    c.execute("SELECT* FROM passwordI")
    rows=c.fetchall()
    
    for row in rows:
        print(row)


#print(c.fetchone())
#tabletest()
#update_studentinfo()
#tabletest()

#add_newStudent()
#add_newclass()
tabletest()
print("----classes next")
tabletestClass()
print('-----instructor table')
#add_instructor()
#add_grades()
tabletestI()
print('----enrollment table')
tabletestE()

testvar='s1'
#.execute('''SELECT enrollment.student_id, enrollment.course_id, grade FROM student INNER JOIN enrollment
 #  ON student.student_id= enrollment.student_id WHERE enrollment.student_id =?''',(testvar,))
    
    
#c.execute("""SELECT* FROM student INNER JOIN enrollment
 #ON student.student_id= enrollment.student_id WHERE enrollment.student_id= s1 """)
c.execute("""SELECT*
FROM Student
INNER JOIN enrollment ON student.student_id = enrollment.student_id """)
    
    
conn.commit()
#c.fetchone()


rows=c.fetchall()
#print(rows)
print("joint tables..........")
for row in rows:
     print(row)

print('------45454545454-----')
join='s1'
c.execute("SELECT * FROM enrollment WHERE student_id= ?",(join,))

print("password student")
tabletestPS()

print("password INSTRUCTOR")
tabletestPI()
    
conn.commit()
#c.fetchone()


rows=c.fetchall()
    
for row in rows:
     print(row)

        


tabletestG()
#add_newStudent()
#add_newclass()
#add_instructor()
#add_grades2()
add_passwordS()
add_passwordI() 



