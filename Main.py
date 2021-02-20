import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import datetime
import time

### variables

password = ''
email = ''




### Functions 

class GoTo:

    def MainPage():

        ### destroying widgets from window
        
        pass_ent.destroy()
        pass_lbl.destroy()
        pass_lbl1.destroy()
        pass_image.destroy()
        login_btn.destroy()
        email_ent.destroy()
        email_lbl.destroy()
        email_lbl1.destroy()
        email_image.destroy()

        bg_lbl.configure(image=bg_img)

        ### creating widgets for main screen

        name_lbl = tk.Label(root, text='Email:',bg='#212838',fg='#e4e4e4',font=('AcmeFont',20))
        name_lbl.place(x=65,y=200)

        email_show_lbl = tk.Label(root, text=email,bg='#212838',fg='#e4e4e4',font=('AcmeFont',15))
        email_show_lbl.place(x=150,y=205)


def login():
    global password, email

    password = pass_ent.get()
    email = email_ent.get()

    if len(password) >= 6 and '@' in email and '.' in email:
        error_lbl = tk.Label(root,text='Logging successful',bg='#212838',fg='#49c240',font=('AcmeFont',10))
        error_lbl.place(x=900,y=620)
        error_lbl.after(2500, error_lbl.destroy)
        root.update()
        time.sleep(2.6)
        GoTo.MainPage()
        root.update()
    else:
        error_lbl = tk.Label(root,text='Error Check your email or password',bg='#212838',fg='#e02838',font=('AcmeFont',10))
        error_lbl.place(x=850,y=620)
        error_lbl.after(2000, error_lbl.destroy)





root = Tk()

root.geometry('1920x1080')
root.resizable(False,False)



### loading assets



bg_login_img = PhotoImage(file='assets/bg_login.png')
bg_img = PhotoImage(file='assets/bg.png')
login_button_img = Image.open('assets/login_btn.png')
login_button_img = login_button_img.resize((400, 105), Image.ANTIALIAS)
login_button_img = ImageTk.PhotoImage(login_button_img)

password_img = Image.open('assets/password_img.png')
password_img = password_img.resize((30, 30), Image.ANTIALIAS)
password_img = ImageTk.PhotoImage(password_img)
email_img = Image.open('assets/user_img.png')
email_img = email_img.resize((30, 30), Image.ANTIALIAS)
email_img = ImageTk.PhotoImage(email_img)



### setting background



bg_lbl = tk.Label(root,image=bg_login_img)
bg_lbl.place(x=-2,y=-2)



### login widgets



email_lbl1 = tk.Label(root,bg='#212838',fg='#e4e4e4',font=('AcmeFont',10),text='___________________________________________________________')
email_lbl1.place(x=750,y=270)

email_image = tk.Label(root,image=email_img,bg='#212838',borderwidth=0)
email_image.place(x=750,y=251)

email_lbl = tk.Label(root,bg='#212838',fg='#e4e4e4',font=('AcmeFont',10),text='Email Address')
email_lbl.place(x=750,y=230)

email_ent = tk.Entry(root,bg='#212838',fg='#e4e4e4',font=('AcmeFont',20),highlightthickness=0,borderwidth=0)
email_ent.place(x=790,y=250)


pass_lbl1 = tk.Label(root,bg='#212838',fg='#e4e4e4',font=('AcmeFont',10),text='___________________________________________________________')
pass_lbl1.place(x=750,y=350)

pass_image = tk.Label(root,bg='#212838',image=password_img,borderwidth=0)
pass_image.place(x=750,y=331)

pass_lbl = tk.Label(root,bg='#212838',fg='#e4e4e4',font=('AcmeFont',10),text='Password')
pass_lbl.place(x=750,y=310)

pass_ent = tk.Entry(root,bg='#212838',fg='#e4e4e4', show="*",font=('AcmeFont',20),highlightthickness=0,borderwidth=0)
pass_ent.place(x=790,y=330)

login_btn = tk.Button(root,image=login_button_img,font=('AcmeFont',40),bg='#212838',fg='#e4e4e4',border=0,activebackground='#212838', command=login)
login_btn.place(x=760,y=650)

root.mainloop()