from tkinter  import *
import pandas as pd
from PIL import Image,ImageTk
from tkinter import messagebox
#from gtts import gTTS
import os
import  tkinter.messagebox
import mysql.connector


###----------------------------------HOME-PAGE-------------------------------------------------------------------------------------------------------
def main():
    R1=Tk()
    R1.geometry('800x600+100+100')
    R1.title('Student Database Management System')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R1,image=photo_image)
    label.place(x=0,y=0)
   
   
    
    l1=Label(R1,text="Student Database Management System",font=('Candara',20,'bold'),bg='Light Blue',justify='center')
    l1.place(x=200,y=100)
    Registerbtn = Button(R1,text = "REGISTER",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=signup)
    loginbtn = Button(R1,text = "LOGIN",width=17,height=2,font=('Candara',15,'bold'),bg='Light Blue',justify='center',command=login)
    Registerbtn.place(x =300 ,y=200)
    loginbtn.place( x =300,y=300)
    R1.mainloop()
    

###------------------------------------REGISTER------------------------------------------------------------------------------------------------------------
    
def signup():
    def Signups():
        Name=name.get()
        Password=pswd.get()

    
        aa= mysql.connector.connect(host='localhost',port= 3300,user="root",passwd="123",db="student_database")
        mm = aa.cursor()
        mm.execute("""INSERT INTO login VALUES (%s,%s)""",(Name,Password))

        aa.commit()

        if name.get() == '' or pswd.get() == '':
             tkinter.messagebox.showinfo("Sorry","Please fill the required information correctly")
        else:
            tkinter.messagebox.showinfo("Welcome %s" %Name, "Lets Login")
            login()
            
    global R2
    R2=Toplevel()
    R2.geometry('800x600+100+100')
    R2.title('REGISTER NOW')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R2,image=photo_image)
    label.place(x=0,y=0)
   



    lblInfo=Label(R2,text="Name",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    lblInfo=Label(R2,text="Password",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    
    name=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    name.place(x=300,y= 140 )
    
    pswd=Entry(R2,show='*',width=20,font=("bold",15),highlightthickness=2)
    pswd.place(x=300,y= 190 )

    submitbtn= Button(R2,text = "Submit",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Signups)

    submitbtn.place(x =350,y=340)
      
    R2.mainloop()
###----------------------------------------------LOGIN---------------------------------------------------------------------------------------------------------
def login():
    def logininto():
        aa = mysql.connector.connect(host='localhost', port=3300, user="root", passwd="123", db="Student_database")
        mm = aa.cursor()
        Name = e1.get()
        Password = e2.get()
        if e1.get() == "" or e2.get() == "":
            tkinter.messagebox.showinfo("Sorry", "Please complete the required field correctly")
        else:
            mm.execute('SELECT * FROM login WHERE Name = %s AND Password = %s',(Name,Password))
            for i in Name:
                print( 0 )
            if mm.fetchall():
                tkinter.messagebox.showinfo("Welcome %s" % Name, "Logged in successfully")
                home()
            else:
                tkinter.messagebox .showinfo("Sorry", "Wrong password")
  
    global R3
    R3 = Toplevel()
    R3.geometry('800x600+100+100')
    R3.title("LOGIN NOW")

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R3,image=photo_image)
    label.place(x=0,y=0)
   


    lblInfo=Label(R3,text="Name",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=230,y=200)
   
    lblInfo=Label(R3,text="Password",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=230,y=250)
    
    e1= Entry(R3,width=15,font=("bold",17),highlightthickness=2,bg="WHITE")
    e1.place(x=330, y=190)

    e2= Entry(R3,width=15,font=("bold",17),show="*",highlightthickness=2,bg="WHITE")
    e2.place(x=330, y=240)

    loginbtn = Button(R3, text="LOGIN", width=10, height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=logininto)
    loginbtn.place(x=380, y=400)
    
    R3.mainloop()
    

###--------------------------------------------------MAIN-PAGE--------------------------------------------------------------------------------------

def home():    
    global R4
    R4=Tk()
    R4.geometry('800x600')
    R4.title('HOME PAGE1')

    '''image=Image.open('image4.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R4,image=photo_image)
    label.place(x=0,y=0)'''
   
    one=Label(R4,text="",bg="blue")             
    two=Label(R4,text="",bg="light blue")
    three=Label(R4,text="",bg="blue")

    one.pack(fill=X)
    two.pack(fill=X)
    three.pack(fill=X)

    
    one1=Label(R4,text="",bg="blue")             
    two2=Label(R4,text="",bg="light blue")
    three3=Label(R4,text="",bg="blue")

    one1.pack(fill=X,side=BOTTOM)
    two2.pack(fill=X,side=BOTTOM)
    three3.pack(fill=X,side=BOTTOM)

   
    Abtn = Button(R4,text = "STUDENT",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=stud)
    Bbtn = Button(R4,text = "DEPARTMENT",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=dept)
    Cbtn = Button(R4,text = "COURSE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=cours)
    Dbtn = Button(R4,text = "GRADE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=grad)
    
    Abtn.place(x =300 ,y=100)
    Bbtn.place(x =300,y=200)
    
    Cbtn.place(x =300 ,y=300)
    Dbtn.place(x =300,y=400)
    R4.mainloop()
    ###---------------------------------------------------------------------STUDENT---------------------------------------------------------------------------------------

def stud():    
    global R5
    R5=Tk()
    R5.geometry('800x600')
    R5.title('STUDENT')

    '''image=Image.open('image4.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R5,image=photo_image)
    label.place(x=0,y=0)'''
   
    one=Label(R5,text="",bg="blue")             
    two=Label(R5,text="",bg="light blue")
    three=Label(R5,text="",bg="blue")

    one.pack(fill=X)
    two.pack(fill=X)
    three.pack(fill=X)

    
    one1=Label(R5,text="",bg="blue")             
    two2=Label(R5,text="",bg="light blue")
    three3=Label(R5,text="",bg="blue")

    one1.pack(fill=X,side=BOTTOM)
    two2.pack(fill=X,side=BOTTOM)
    three3.pack(fill=X,side=BOTTOM)

   
    AAbtn = Button(R5,text = "INSERT",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun11)
    BBbtn = Button(R5,text = "DELETE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun12)
    CCbtn = Button(R5,text = "UPDATE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun13)
    DDbtn = Button(R5,text = "DISPLAY",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun14)
    
    AAbtn.place(x =300 ,y=100)
    BBbtn.place(x =300,y=200)
    
    CCbtn.place(x =300 ,y=300)
    DDbtn.place(x =300,y=400)
    R5.mainloop()

    
    ###------------------------------------------------------------------STUDENT-INSERT--------------------------------------------------------------------------------------------
def fun11():
    def Student():
        Usn=usn.get()
        Name=name.get()
        Phno=phno.get()
        Dno=dno.get()
        Percentage=percentage.get()
        
        aa= mysql.connector.connect(host='localhost',port= 3300,user="root",passwd="123",db="student_database")
        mm = aa.cursor()
        mm.execute("""INSERT INTO student VALUES (%s,%s,%s,%s,%s)""",(Usn,Name,Phno,Dno,Percentage))

              
        aa.commit()

        if usn.get() == "" or name.get() == "":
            tkinter.messagebox.showinfo("Sorry", "Please complete the required field correctly")
        else:
            mm.execute('SELECT * FROM student WHERE Usn = %s AND Name = %s',(Usn,Name))
            for i in Name:
                print(0)
            if mm.fetchall():
                tkinter.messagebox.showinfo("Student %s" % Name, "Got Inserted")
                home()
         
        
    global R6
    R6=Toplevel()
    R6.geometry('800x600+100+100')
    R6.title('Student Insert')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R6,image=photo_image)
    label.place(x=0,y=0)
   
    lblInfo=Label(R6,text="USN",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    lblInfo=Label(R6,text="NAME",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    
    lblInfo=Label(R6,text="Phno",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)

    lblInfo=Label(R6,text="Dno",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=290)

    lblInfo=Label(R6,text="Percentage",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=340)
    
    
    usn=Entry(R6,width=20,font=("bold",15),highlightthickness=2)
    usn.place(x=300,y= 140 )
    
    name=Entry(R6,width=20,font=("bold",15),highlightthickness=2)
    name.place(x=300,y=190 )
    
    phno=Entry(R6,width=20,font=("bold",15),highlightthickness=2)
    phno.place(x=300,y= 240 )
    
    dno=Entry(R6,width=20,font=("bold",15),highlightthickness=2)
    dno.place(x=300,y= 290)

    percentage=Entry(R6,width=20,font=("bold",15),highlightthickness=2)
    percentage.place(x=300,y=340)

    submitbtn= Button(R6,text = "Submit",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Student)
    submitbtn.place(x =350,y=390)
    
    R6.mainloop()
###---------------------------------------------------------------------STUDENT-DELETE-------------------------------------------------------------------------------
def fun12():
    def Delete():
        Usn=usn.get()
        mydb=mysql.connector.connect(host="localhost",user="root",port=3300,password="123",database="student_database")
        mycursor=mydb.cursor()

        
        Delete="delete from student where Usn='%s'" %(Usn)
        mycursor.execute(Delete)
        mydb.commit()
        messagebox.showinfo("Information","Record Deleted")
        usn.delete(0,END)
        

    
    global R14
    R14=Toplevel()
    R14.geometry('800x600+100+100')
    R14.title('Student Delete')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R14,image=photo_image)
    label.place(x=0,y=0)
   

    lblInfo=Label(R14,text="USN",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    
    usn=Entry(R14,width=20,font=("bold",15),highlightthickness=2)
    usn.place(x=250,y= 140)


    Dbtn= Button(R14,text = "DELETE",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Delete)
    Dbtn.place(x =320,y=220)

    R14.mainloop()
#-----------------------------------------------------------------STUDENT-Update---------------------------------------------------------------------------------
def fun13():
    def Update():
        Usn=e1.get()
        Name=e2.get()
        Phno=e3.get()
        Dno=e4.get()
        Percentage=e5.get()
        
        mydb=mysql.connector.connect(host="localhost",user="root",port=3300,password="123",database="student_database")
        mycursor=mydb.cursor()
        
        Update="Update student set  Name='%s', Phno='%s', Dno='%s',Percentage='%s' where Usn='%s'" %(Name,Phno,Dno,Percentage,Usn)
        mycursor.execute(Update)
        mydb.commit()
        messagebox.showinfo("Info","Record Update")

    global R16
    R16=Toplevel()
    R16.geometry('800x600+100+100')
    R16.title('Student Update')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R16,image=photo_image)
    label.place(x=0,y=0)
   
    
    lblInfo=Label(R16,text="USN",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)
    lblInfo=Label(R16,text="Name",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    lblInfo=Label(R16,text="PhoneNo",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)
    lblInfo=Label(R16,text="DeptNo",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=290)
    lblInfo=Label(R16,text="Percent",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=340)

    
    e1=Entry(R16,width=20,font=("bold",15),highlightthickness=2)
    e1.place(x=300,y= 140)
    e2=Entry(R16,width=20,font=("bold",15),highlightthickness=2)
    e2.place(x=300,y= 190)
    e3=Entry(R16,width=20,font=("bold",15),highlightthickness=2)
    e3.place(x=300,y= 240)
    e4=Entry(R16,width=20,font=("bold",15),highlightthickness=2)
    e4.place(x=300,y= 290)
    e5=Entry(R16,width=20,font=("bold",15),highlightthickness=2)
    e5.place(x=300,y= 340)


    Dbtn= Button(R16,text = "UPDATE",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Update)
    Dbtn.place(x =300,y=400)

    R16.mainloop()

    
    
###--------------------------------------------------------------------STUDENT-Display--------------------------------------------------------------------------------
def fun14():
    import mysql.connector 
	
# connecting to the database 
    dataBase = mysql.connector.connect( 
					host = "localhost", 
					user = "root",
                                        port=3300,
					passwd = "123", 
					database = "student_database" ) 
	
# preparing a cursor object 
    cursorObject = dataBase.cursor() 
	
    print("Displaying STUDENTS table:") 

# selecting query 
    query = "SELECT * FROM STUDENT"
    cursorObject.execute(query) 

    myresult = cursorObject.fetchall() 

    for x in myresult:
        print(x) 

# disconnecting from server 
    dataBase.close() 


###-----------------------------------------------------------DEPARTMENT------------------------------------------------------------------------------------------------
def dept():    
    global R7
    R7=Tk()
    R7.geometry('800x600')
    R7.title('DEPARTMENT')

    '''image=Image.open('image4.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R7,image=photo_image)
    label.place(x=0,y=0)'''
   
    one=Label(R7,text="",bg="blue")             
    two=Label(R7,text="",bg="light blue")
    three=Label(R7,text="",bg="blue")

    one.pack(fill=X)
    two.pack(fill=X)
    three.pack(fill=X)

    
    one1=Label(R7,text="",bg="blue")             
    two2=Label(R7,text="",bg="light blue")
    three3=Label(R7,text="",bg="blue")

    one1.pack(fill=X,side=BOTTOM)
    two2.pack(fill=X,side=BOTTOM)
    three3.pack(fill=X,side=BOTTOM)

   
    AAbtn = Button(R7,text = "INSERT",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun21)
    BBbtn = Button(R7,text = "DELETE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun22)
    CCbtn = Button(R7,text = "UPDATE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun23)
    DDbtn = Button(R7,text = "DISPLAY",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun24)
    
    AAbtn.place(x =300 ,y=100)
    BBbtn.place(x =300,y=200)
    
    CCbtn.place(x =300 ,y=300)
    DDbtn.place(x =300,y=400)
    R7.mainloop()

###-------------------------------------------------DEPARTMENT INSERT--------------------------------------------------------------------------------------- 

def fun21():
    def Department():
        Dno=dno.get()
        Dname=dname.get()
        Dlocation=dloc.get()

    
        aa= mysql.connector.connect(host='localhost',port= 3300,user="root",passwd="123",db="student_database")
        mm = aa.cursor()
        mm.execute("""INSERT INTO department VALUES (%s,%s,%s)""",(Dno,Dname,Dlocation))

        aa.commit()
        home()
        
              
    global R8
    R8=Toplevel()
    R8.geometry('800x600+100+100')
    R8.title('Department Insert')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R8,image=photo_image)
    label.place(x=0,y=0)
   

    lblInfo=Label(R8,text="DNO",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    lblInfo=Label(R8,text="DNAME",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    
    lblInfo=Label(R8,text="DLOC",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)
    
    
    dno=Entry(R8,width=20,font=("bold",15),highlightthickness=2)
    dno.place(x=300,y= 140 )
    
    dname=Entry(R8,width=20,font=("bold",15),highlightthickness=2)
    dname.place(x=300,y=190 )
    
    dloc=Entry(R8,width=20,font=("bold",15),highlightthickness=2)
    dloc.place(x=300,y= 240 )
    
    submitbtn= Button(R8,text = "Submit",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Department)
    submitbtn.place(x =350,y=390)
      
    R8.mainloop()
#-------------------------------------------------------------DEPARTMENT-DELETE----------------------------------------------------------------------------------------
def fun22():
    def Delete():
        Dname=dname.get()
        mydb=mysql.connector.connect(host="localhost",user="root",port=3300,password="123",database="student_database")
        mycursor=mydb.cursor()

        
        Delete="delete from department where Dname='%s'" %(Dname)
        mycursor.execute(Delete)
        mydb.commit()
        messagebox.showinfo("Information","Record Deleted")
        dname.delete(0,END)
        

    
    global R13
    R13=Toplevel()
    R13.geometry('800x600+100+100')
    R13.title('Department Delete')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R13,image=photo_image)
    label.place(x=0,y=0)
   

    lblInfo=Label(R13,text="DeptName",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    
    dname=Entry(R13,width=20,font=("bold",15),highlightthickness=2)
    dname.place(x=300,y= 140)


    Dbtn= Button(R13,text = "DELETE",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Delete)
    Dbtn.place(x =320,y=250)

    R13.mainloop()
#-------------------------------------------------------DEPARTMENT-Update-----------------------------------------------------------------------------------------
def fun23():
    def Update():
        Dno=e1.get()
        Dname=e2.get()
        Dloc=e3.get()
        
        mydb=mysql.connector.connect(host="localhost",user="root",port=3300,password="123",database="student_database")
        mycursor=mydb.cursor()
        
        Update="Update department set  Dname='%s', Dloc='%s' where Dno='%s'" %(Dname,Dloc,Dno)
        mycursor.execute(Update)
        mydb.commit()
        messagebox.showinfo("Info","Record Update")

    global R17
    R17=Toplevel()
    R17.geometry('800x600+100+100')
    R17.title('Department Update')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R17,image=photo_image)
    label.place(x=0,y=0)
   
    
    lblInfo=Label(R17,text="DeptNo",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)
    lblInfo=Label(R17,text="Dname",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    lblInfo=Label(R17,text="DeptLoc",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)

    
    e1=Entry(R17,width=20,font=("bold",15),highlightthickness=2)
    e1.place(x=300,y= 140)
    e2=Entry(R17,width=20,font=("bold",15),highlightthickness=2)
    e2.place(x=300,y= 190)
    e3=Entry(R17,width=20,font=("bold",15),highlightthickness=2)
    e3.place(x=300,y= 240)
    

    Dbtn= Button(R17,text = "UPDATE",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Update)
    Dbtn.place(x =300,y=300)

    R17.mainloop()


    
###----------------------------------------------------------DEPARTMENT-DISPLAY-------------------------------------------------------------------------------------
def fun24():
    import mysql.connector 
	
# connecting to the database 
    dataBase = mysql.connector.connect( 
					host = "localhost", 
					user = "root",
                                        port=3300,
					passwd = "123", 
					database = "student_database" ) 
	
# preparing a cursor object 
    cursorObject = dataBase.cursor() 
	
    print("Displaying DEPARTMENT table:") 

# selecting query 
    query = "SELECT * FROM DEPARTMENT"
    cursorObject.execute(query) 

    myresult = cursorObject.fetchall() 

    for x in myresult:
        print(x) 

# disconnecting from server 
    dataBase.close() 

    
###------------------------------------------------------------Course--------------------------------------------------------------------------------------------    

def cours():    
    global R9
    R9=Tk()
    R9.geometry('800x600')
    R9.title('COURSE')

    '''image=Image.open('image4.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R9,image=photo_image)
    label.place(x=0,y=0)'''
   
    one=Label(R9,text="",bg="blue")             
    two=Label(R9,text="",bg="light blue")
    three=Label(R9,text="",bg="blue")

    one.pack(fill=X)
    two.pack(fill=X)
    three.pack(fill=X)

    
    one1=Label(R9,text="",bg="blue")             
    two2=Label(R9,text="",bg="light blue")
    three3=Label(R9,text="",bg="blue")

    one1.pack(fill=X,side=BOTTOM)
    two2.pack(fill=X,side=BOTTOM)
    three3.pack(fill=X,side=BOTTOM)

   
    AAbtn = Button(R9,text = "INSERT",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun31)
    BBbtn = Button(R9,text = "DELETE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun32)
    CCbtn = Button(R9,text = "UPDATE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun33)
    DDbtn = Button(R9,text = "DISPLAY",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun34)
    
    AAbtn.place(x =300 ,y=100)
    BBbtn.place(x =300,y=200)
    
    CCbtn.place(x =300 ,y=300)
    DDbtn.place(x =300,y=400)
    R9.mainloop()
###--------------------------------------------------------Course-Insert-----------------------------------------------------------------------------------------

def fun31():
    def Course():
        Cno=cno.get()
        Cname=cname.get()
        Credits=cred.get()

    
        aa= mysql.connector.connect(host='localhost',port= 3300,user="root",passwd="123",db="student_database")
        mm = aa.cursor()
        mm.execute("""INSERT INTO course VALUES (%s,%s,%s)""",(Cno,Cname,Credits))

        aa.commit()
        home()

              
    global R10
    R10=Toplevel()
    R10.geometry('800x600+100+100')
    R10.title('Course Insert')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R10,image=photo_image)
    label.place(x=0,y=0)
   

    lblInfo=Label(R10,text="CNO",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    lblInfo=Label(R10,text="CNAME",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    
    lblInfo=Label(R10,text="CREDITS",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)
    
    
    cno=Entry(R10,width=20,font=("bold",15),highlightthickness=2)
    cno.place(x=300,y= 140 )
    
    cname=Entry(R10,width=20,font=("bold",15),highlightthickness=2)
    cname.place(x=300,y=190 )
    
    cred=Entry(R10,width=20,font=("bold",15),highlightthickness=2)
    cred.place(x=300,y= 240 )
    
    submitbtn= Button(R10,text = "Submit",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Course)
    submitbtn.place(x =350,y=390)
      
    R10.mainloop()
#-------------------------------------------------------------Course-Delete----------------------------------------------------------------------------------
def fun32():
    def Delete():
        Cname=cname.get()
        mydb=mysql.connector.connect(host="localhost",user="root",port=3300,password="123",database="student_database")
        mycursor=mydb.cursor()

        
        Delete="delete from course where Cname='%s'" %(Cname)
        mycursor.execute(Delete)
        mydb.commit()
        messagebox.showinfo("Information","Record Deleted")
        cname.delete(0,END)
        

    
    global R15
    R15=Toplevel()
    R15.geometry('800x600+100+100')
    R15.title('Course Delete')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R15,image=photo_image)
    label.place(x=0,y=0)
   

    lblInfo=Label(R15,text="CName",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    
    cname=Entry(R15,width=20,font=("bold",15),highlightthickness=2)
    cname.place(x=280,y= 140)


    Dbtn= Button(R15,text = "DELETE",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Delete)
    Dbtn.place(x =320,y=220)

    R15.mainloop()
#-----------------------------------------------------------Course-Update--------------------------------------------------------------------------------------------------
def fun33():
    def Update():
        Cno=e1.get()
        Cname=e2.get()
        Credits=e3.get()
        
        mydb=mysql.connector.connect(host="localhost",user="root",port=3300,password="123",database="student_database")
        mycursor=mydb.cursor()
        
        Update="Update course set  Cname='%s', Credits='%s' where Cno='%s'" %(Cname,Credits,Cno)
        mycursor.execute(Update)
        mydb.commit()
        messagebox.showinfo("Info","Record Update")
        
    global R18
    R18=Toplevel()
    R18.geometry('800x600+100+100')
    R18.title('Course Update')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R18,image=photo_image)
    label.place(x=0,y=0)
   
    
    lblInfo=Label(R18,text="CourseNo",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)
    lblInfo=Label(R18,text="Cname",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    lblInfo=Label(R18,text="Credits",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)

    
    e1=Entry(R18,width=20,font=("bold",15),highlightthickness=2)
    e1.place(x=300,y= 140)
    e2=Entry(R18,width=20,font=("bold",15),highlightthickness=2)
    e2.place(x=300,y= 190)
    e3=Entry(R18,width=20,font=("bold",15),highlightthickness=2)
    e3.place(x=300,y= 240)
    

    Dbtn= Button(R18,text = "UPDATE",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Update)
    Dbtn.place(x =300,y=300)

    R18.mainloop()
    
#-----------------------------------------------------------Course-Display------------------------------------------------------------------------------------
def fun34():
    import mysql.connector 
	
# connecting to the database 
    dataBase = mysql.connector.connect( 
					host = "localhost", 
					user = "root",
                                        port=3300,
					passwd = "123", 
					database = "student_database" ) 
	
# preparing a cursor object 
    cursorObject = dataBase.cursor() 
	
    print("Displaying COURSE table:") 

# selecting query 
    query = "SELECT * FROM Course"
    cursorObject.execute(query) 

    myresult = cursorObject.fetchall() 

    for x in myresult:
        print(x) 

# disconnecting from server 
    dataBase.close() 

    
#-------------------------------------------------------------Grade---------------------------------------------------------------------------------------------

def grad():    
    global R12
    R12=Tk()
    R12.geometry('800x600')
    R12.title('GRADE')

    '''image=Image.open('image4.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R12,image=photo_image)
    label.place(x=0,y=0)'''
   
    one=Label(R12,text="",bg="blue")             
    two=Label(R12,text="",bg="light blue")
    three=Label(R12,text="",bg="blue")

    one.pack(fill=X)
    two.pack(fill=X)
    three.pack(fill=X)

    
    one1=Label(R12,text="",bg="blue")             
    two2=Label(R12,text="",bg="light blue")
    three3=Label(R12,text="",bg="blue")

    one1.pack(fill=X,side=BOTTOM)
    two2.pack(fill=X,side=BOTTOM)
    three3.pack(fill=X,side=BOTTOM)

   
    AAbtn = Button(R12,text = "INSERT",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun41)
    CCbtn = Button(R12,text = "UPDATE",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun43)
    DDbtn = Button(R12,text = "DISPLAY",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun44)
    
    AAbtn.place(x =300 ,y=100)
    
    CCbtn.place(x =300 ,y=200)
    DDbtn.place(x =300,y=300)
    R12.mainloop()

###---------------------------------------------------------Grade-Insert-------------------------------------------------------------------------------------------

def fun41():
    def Grade():
        Usn=usn.get()
        Cno=cno.get()
        Grade=grade.get()

    
        aa= mysql.connector.connect(host='localhost',port= 3300,user="root",passwd="123",db="student_database")
        mm = aa.cursor()
        mm.execute("""INSERT INTO grade VALUES (%s,%s,%s)""",(Usn,Cno,Grade))

        aa.commit()
        home()

              
    global R11
    R11=Toplevel()
    R11.geometry('800x600+100+100')
    R11.title('grade')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R11,image=photo_image)
    label.place(x=0,y=0)
   

    lblInfo=Label(R11,text="USN",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    lblInfo=Label(R11,text="CNO",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    
    lblInfo=Label(R11,text="GRADE",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)
    
    
    usn=Entry(R11,width=20,font=("bold",15),highlightthickness=2)
    usn.place(x=300,y= 140 )
    
    cno=Entry(R11,width=20,font=("bold",15),highlightthickness=2)
    cno.place(x=300,y=190 )
    
    grade=Entry(R11,width=20,font=("bold",15),highlightthickness=2)
    grade.place(x=300,y= 240 )
    
    submitbtn= Button(R11,text = "Submit",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Grade)
    submitbtn.place(x =350,y=390)
      
    R11.mainloop()
#---------------------------------------------------------------Grade-Update-------------------------------------------------------------------------------------
def fun43():
    def Update():
        Usn=e1.get()
        Cno=e2.get()
        Grade=e3.get()
        
        mydb=mysql.connector.connect(host="localhost",user="root",port=3300,password="123",database="student_database")
        mycursor=mydb.cursor()
        
        Update="Update grade set  Grade='%s' where Usn='%s' and Cno='%s' " %(Grade,Usn,Cno)
        mycursor.execute(Update)
        mydb.commit()
        messagebox.showinfo("Info","Record Update")
        
    global R19
    R19=Toplevel()
    R19.geometry('800x600+100+100')
    R19.title('Grade Update')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R19,image=photo_image)
    label.place(x=0,y=0)
   
    
    lblInfo=Label(R19,text="USN",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)
    lblInfo=Label(R19,text="CourseNo",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    lblInfo=Label(R19,text="Grade",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)

    
    e1=Entry(R19,width=20,font=("bold",15),highlightthickness=2)
    e1.place(x=300,y= 140)
    e2=Entry(R19,width=20,font=("bold",15),highlightthickness=2)
    e2.place(x=300,y= 190)
    e3=Entry(R19,width=20,font=("bold",15),highlightthickness=2)
    e3.place(x=300,y= 240)
    

    Dbtn= Button(R19,text = "UPDATE",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Update)
    Dbtn.place(x =300,y=300)

    R19.mainloop()
    

    
#-----------------------------------------------------------Grade-Display-----------------------------------------------------------------------------------------
def fun44():
    import mysql.connector 
	
# connecting to the database 
    dataBase = mysql.connector.connect( 
					host = "localhost", 
					user = "root",
                                        port=3300,
					passwd = "123", 
					database = "student_database" ) 
	
# preparing a cursor object 
    cursorObject = dataBase.cursor() 
	
    print("Displaying GRADE table:") 

# selecting query 
    query = "SELECT * FROM grade"
    cursorObject.execute(query) 

    myresult = cursorObject.fetchall() 

    for x in myresult:
        print(x) 

# disconnecting from server 
    dataBase.close() 
#----------------------------------------------------------------------------------------------------------------------------------------------------------

main()   






    
            

    
    
