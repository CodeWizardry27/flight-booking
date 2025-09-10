from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import mysql.connector

def clear():
    emailEntry.delete(0,END)
    UsernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
def signup_page():
    signup_window.destroy()
    import login

def connect_database():
    if emailEntry.get()=='' or UsernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
        
            con=mysql.connector.connect(host='localhost',password='1234',user='root',database='userdata')    
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','connectivity error')
            return
        try:
            query='use userdata;'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20));'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata;')
        
        query='insert into data(email,username,password) values(%s,%s,%s);'
        mycursor.execute(query,(emailEntry.get(),UsernameEntry.get(),passwordEntry.get()))
        con.commit()            
        con.close()
        messagebox.showinfo('Success','registration successfully')
        clear()
        signup_page()

signup_window=Tk()
signup_window.geometry('1300x850+50+50')
def on_enter(event):
    if UsernameEntry.get()=='Owner name':
        UsernameEntry.delete(0,END)
def user_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
def email_enter(event):
    if emailEntry.get()=='e Mail':
        emailEntry.delete(0,END)
def login_database():
    signup_window.destroy()
    import login

bgimage=ImageTk.PhotoImage(file="Slide1.jpg")
bgLabel=Label(signup_window,image=bgimage)
bgLabel.place(x=0 , y=0)
heading=Label(signup_window,text='* CREATE NEW ACCOUNT *',font=('Microsoft Yahei UI Light',23,'bold','underline'),bg='white',fg='blue')
heading.place(x=700,y=320)
emailEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',11,'bold','underline'),bg='white',fg='black')
emailEntry.place(x=750,y=370)
emailEntry.insert(0,'E-Mail')
emailEntry.bind('<FocusIn>',email_enter)


UsernameEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',11,'bold','underline'),bg='white',fg='black')
UsernameEntry.place(x=750,y=400)
UsernameEntry.insert(0,'User name')
UsernameEntry.bind('<FocusIn>',on_enter)


passwordEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',11,'bold','underline'),bg='white',bd=0,fg='black')
passwordEntry.place(x=750,y=440)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',user_enter)
signupButton=Button(signup_window,text='SIGN UP',font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='blue',cursor='hand2',bd=0,width='25',command=connect_database)
signupButton.place(x=750,y=480)
dolabel=Label(signup_window,text=' Have an account',font=('Microsoft Yahei UI Light',10,'bold','underline'),fg='black',bd=0 )
dolabel.place(x=750,y=560)
signupButton=Button(signup_window,text='login',font=('Microsoft Yahei UI Light',9,'bold'),fg='blue',bg='white',cursor='hand2',command=login_database)
signupButton.place(x=930,y=560)


signup_window.mainloop()