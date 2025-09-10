from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import qrcode
import pyqrcode
from pyqrcode import QRCode
root=Tk()
root.geometry('1280x720+50+50')
bgimage=ImageTk.PhotoImage(file="Slide2.jpg")
bgLabel=Label(root,image=bgimage)
bgLabel.place(x=0, y=0)

g_logo=PhotoImage(file='scan.png')
fblabel=Label(root,image=g_logo,bg='white')
fblabel.place(x=790,y=0)

p_logo=PhotoImage(file='scan2.png')
fblabel=Label(root,image=p_logo,bg='white')
fblabel.place(x=790,y=450)

'''payment_logo=PhotoImage(file='Payment_qr.png')
fblabel=Label(root,image=payment_logo,bg='white')
fblabel.place(x=900,y=200)'''
signButton=Button(root,text='Procced',font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='green',cursor='hand2')
signButton.place(x=980,y=640)



upi_id="6398119652@ybl"
amount=500000
Payment_url=f'upi://pay?pa={upi_id}&pn=ReceiverName&am={amount}'

#create qr code for each code
Payment_qr=qrcode.make(Payment_url)

#save the qr code 
Payment_qr.save('Payment_qr.png')


#showing qrsatyamjha88anand-1@okicici
#Payment_qr.show()
payment_logo=PhotoImage(file='Payment_qr.png')
fblabel=Label(root,image=payment_logo,bg='white')
fblabel.place(x=825,y=100)


root.mainloop()
