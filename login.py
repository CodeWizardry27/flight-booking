from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
import mysql.connector
def clear():
    
    UsernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
def login():
    root.destroy()
    import front
def connect_database():
    if  UsernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
        
            con=mysql.connector.connect(host='localhost',password='1234',user='root',database='userdata')    
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','connectivity error')
            return
    query='use userdata;'
    mycursor.execute(query)
    query='select * from data where username=%s and password=%s;'
    mycursor.execute(query,(UsernameEntry.get(),passwordEntry.get()))
    row=mycursor.fetchone()
    if row==None:
        messagebox.showerror('Error','invalid user name or password')
        clear()
    else:
        messagebox.showinfo('Success','login successfully')
        login()
def signup_page():
    root.destroy()
    import signup
def hide():
    openeye.config(file='download (1).png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='download.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
def on_enter(event):
    if UsernameEntry.get()=='Owner name':
        UsernameEntry.delete(0,END)
def user_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
root=Tk()
root.geometry('1300x850+50+50')

bgimage=ImageTk.PhotoImage(file="Slide1.jpg")
bgLabel=Label(root,image=bgimage)
bgLabel.place(x=0 , y=0)



heading=Label(root,text='*  LOGIN *',font=('Microsoft Yahei UI Light',23,'bold','underline'),bg='white',fg='green')
heading.place(x=800,y=320)
UsernameEntry=Entry(root,width=25,font=('Microsoft Yahei UI Light',11,'bold','underline'),bg='white',fg='black')
UsernameEntry.place(x=800,y=380)
UsernameEntry.insert(0,'User Name')
UsernameEntry.bind('<FocusIn>',on_enter)


passwordEntry=Entry(root,width=25,font=('Microsoft Yahei UI Light',11,'bold','underline'),bg='white',bd=0,fg='black')
passwordEntry.place(x=800,y=440)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',user_enter)
openeye=PhotoImage(file='download.png') 
eyeButton=Button(root,image=openeye,bd=0,activebackground='skyblue',cursor='hand2',command=hide )
eyeButton.place(x=1000,y=440)


loginButton=Button(root,text='Login',font=('Microsoft Yahei UI Light',14,'bold'),fg='white',bg='green',cursor='hand2',bd=0,width='25',command=connect_database)
loginButton.place(x=800,y=480)
orlabel=Label(root,text='------------------ continue with ---------------------',font=('Microsoft Yahei UI Light',11,'bold'),fg='black',bd=0 )
orlabel.place(x=800,y=560)
f_logo=PhotoImage(file='f.png')
fblabel=Label(root,image=f_logo,bg='white')
fblabel.place(x=800,y=600)

i_logo=PhotoImage(file='i.png')
fblabel=Label(root,image=i_logo,bg='white')
fblabel.place(x=900,y=600)
g_logo=PhotoImage(file='g.png')
fblabel=Label(root,image=g_logo,bg='white')
fblabel.place(x=1000,y=600)

t_logo=PhotoImage(file='Twitter-1140x694.png')
fblabel=Label(root,image=t_logo,bg='white')
fblabel.place(x=1100,y=600)


dolabel=Label(root,text='Do not have an account',font=('Microsoft Yahei UI Light',10,'bold','underline'),fg='black',bd=0 )
dolabel.place(x=800,y=640)
signButton=Button(root,text='sign up',font=('Microsoft Yahei UI Light',9,'bold'),fg='blue',bg='white',cursor='hand2',command=signup_page)
signButton.place(x=980,y=640)


root.mainloop()