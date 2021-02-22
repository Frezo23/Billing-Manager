import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
import datetime
import webbrowser
import pyperclip
import random
import time

### variables

password = ''
email = ''
a = 1
itme_list = {}
item = ''
item_to_select = ''
child = 0


discord_link = 'https://discord.gg/hsMpeuw5qe'
github_link = 'https://github.com/Frezo23'
email_link = 'wilczewski.dominik@gmail.com'
donate_link = 'https://tipply.pl/u/frezo'


### Functions 

def open_discord():
    webbrowser.open(discord_link)

def open_github():
    webbrowser.open(github_link)

def donate():
    webbrowser.open(donate_link)

def copy_mail():
    pyperclip.copy(email_link)

    link_copied_lbl = tk.Label(root, image=link_copied_img,bg='#212838',borderwidth=0)
    link_copied_lbl.place(x=800,y=960)

    root.update()
    link_copied_lbl.after(2000, link_copied_lbl.destroy())
    root.update()

def copy_discord():
    pyperclip.copy(discord_link)

    link_copied_lbl = tk.Label(root, image=link_copied_img,bg='#212838',borderwidth=0)
    link_copied_lbl.place(x=800,y=960)

    root.update()
    link_copied_lbl.after(2000, link_copied_lbl.destroy())
    root.update()

def copy_github():
    pyperclip.copy(github_link)

    link_copied_lbl = tk.Label(root, image=link_copied_img,bg='#212838',borderwidth=0)
    link_copied_lbl.place(x=800,y=960)

    root.update()
    link_copied_lbl.after(2000, link_copied_lbl.destroy())
    root.update()

def copy_donate():
    pyperclip.copy(donate_link)

    link_copied_lbl = tk.Label(root, image=link_copied_img,bg='#212838',borderwidth=0)
    link_copied_lbl.place(x=800,y=960)

    root.update()
    link_copied_lbl.after(2000, link_copied_lbl.destroy())
    root.update()

def MainPage():
    global a, item, item_text, item_to_select, child

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

    ## Left tab

    user_info_lbl = tk.Label(root,text='User Info:',bg='#212838',fg='#e4e4e4',font=('AcmeFont',20))
    user_info_lbl.place(x=75,y=160)

    name_lbl = tk.Label(root, text='Email:',bg='#212838',fg='#e4e4e4',font=('AcmeFont',17))
    name_lbl.place(x=65,y=230)

    email_show_lbl = tk.Label(root, text=email,bg='#212838',fg='#e4e4e4',font=('AcmeFont',15))
    email_show_lbl.place(x=65,y=265)

    contacts_lbl = tk.Label(root, text='Contact me:',bg='#212838',fg='#e4e4e4',font=('AcmeFont',20))
    contacts_lbl.place(x=65,y=547)

    contact_email_image = tk.Button(root,image=contact_mail_img,bg='#212838',borderwidth=0,command=copy_mail)
    contact_email_image.place(x=65,y=610)

    contact_email_lbl = tk.Button(root,text=email_link,bg='#212838',fg='#e4e4e4',borderwidth=0,font=('AcmeFont',15),command=copy_mail)
    contact_email_lbl.place(x=110,y=610)

    contact_discord_image = tk.Button(root,image=contact_discord_img,bg='#212838',borderwidth=0,command=open_discord)
    contact_discord_image.place(x=65,y=660)

    contact_discord_lbl = tk.Button(root,text=discord_link,bg='#212838',fg='#e4e4e4',borderwidth=0,font=('AcmeFont',15),command=copy_discord)
    contact_discord_lbl.place(x=110,y=660)

    contact_github_image = tk.Button(root,image=contact_github_img,bg='#212838',borderwidth=0,command=open_github)
    contact_github_image.place(x=65,y=710)

    contact_github_lbl = tk.Button(root,text=github_link,bg='#212838',fg='#e4e4e4',borderwidth=0,font=('AcmeFont',15),command=copy_github)
    contact_github_lbl.place(x=110,y=710)

    support_lbl = tk.Label(root, text='Support me:',bg='#212838',fg='#e4e4e4',font=('AcmeFont',20))
    support_lbl.place(x=65,y=793)

    donate_btn = tk.Button(root, image=donate_img,bg='#212838',borderwidth=0,command=donate,activebackground='#212838')
    donate_btn.place(x=65,y=855)

    donate_lbl = tk.Button(root, text=donate_link,bg='#212838',fg='#e4e4e4',font=('AcmeFont',15),borderwidth=0,command=copy_donate,activebackground='#212838')
    donate_lbl.place(x=110,y=855)


    ### Right tab

    style = ttk.Style(root)

    style.configure('Treeview',border=0,background='#363c4e',foreground='#e4e4e4',font=('Titillium',15), rowheight=45)
    style.map('Treeview', background=[('selected', '#212874')])

    bills_tree = ttk.Treeview(root)
    bills_tree.place(x=1000,y=400)


    bills_tree['columns'] = ('Currency','Spend','Date')
    bills_tree.column('#0', width=100)
    bills_tree.column('Currency',width=70)
    bills_tree.column('Spend',width=300)
    bills_tree.column('Date',width=300)

    bills_tree.heading('#0',text='Billing List',anchor=tk.W)
    bills_tree.heading('Currency',text='Currency',anchor=tk.W)
    bills_tree.heading('Spend',text='Spend',anchor=tk.W)
    bills_tree.heading('Date',text='Date',anchor=tk.W)

    for x in range(20):
        bills_tree.insert('', 'end',text=str(a) + '.', values=('PLN',str(random.randint(1,10)), str(datetime.datetime.today().strftime('%Y-%m-%d-%H:%M'))))
        a += 1
        root.update()


    ### Find your bill

    Search_lbl = tk.Label(root, text='Search options:',bg='#212838',fg='#e4e4e4',font=('AcmeFont',20))
    Search_lbl.place(x=560,y=413)

    search_lbl1 = tk.Label(root,bg='#212838',fg='#e4e4e4',font=('AcmeFont',10),borderwidth=0,text='_____________________________________')
    search_lbl1.place(x=560,y=510)
    
    search_ent = tk.Entry(root,bg='#212838',fg='#e4e4e4',font=('AcmeFont',15),highlightthickness=0,borderwidth=0)
    search_ent.place(x=560,y=490)

    search_lbl2 = tk.Label(root, text='Search:',bg='#212838',fg='#e4e4e4',font=('AcmeFont',10))
    search_lbl2.place(x=560,y=470)

    default = StringVar(root)
    default.set('Spend')

    select_lbl = tk.Label(root, text='Search by:',bg='#212838',fg='#e4e4e4',font=('AcmeFont',15))
    select_lbl.place(x=560,y=530)

    select_to_find = tk.OptionMenu(root, default,'Spend','Currency','Date')
    select_to_find.place(x=675,y=532)

    select_to_find.config(bg='#212838',fg='#e4e4e4',font=('AcmeFont',10),borderwidth=0)


    ### search function for main screen


    def search():          ### searches treeview

        global item, item_text, item_to_select, child

        child = 0
        itme_list = {}
        item = ''
        item_to_select = ''
        search_value = []
        search_value.append(search_ent.get())

        # item = bills_tree.selection()[0]
        # item_text = bills_tree.item(item,'values')

        for child in bills_tree.get_children():
            if len(bills_tree.selection()) > 0:
                bills_tree.selection_remove(bills_tree.selection()[0])

        for child in bills_tree.get_children():

            print(child)
            item = bills_tree.item(child)
            item_text = bills_tree.item(child,'values',)

            item_text = list(item_text)
            print(item_text)

            if default.get() == 'Spend':
                item_text.remove(item_text[0])
                item_text.remove(item_text[1])
                print(item_text)
                print('Spend')
            elif default.get() == 'Currency':
                item_text.remove(item_text[1])
                item_text.remove(item_text[1])
                print(item_text)
            elif default.get() == 'Date':
                item_text.remove(item_text[0])
                item_text.remove(item_text[0])
                print(item_text)

            if str(search_value) in str(item_text):
                print('found in:', child)
            
                item_to_select = child
                bills_tree.selection_add(item_to_select)

        print(item_text)
        print(item)



    search_btn = tk.Button(root, image=search_btn_img,borderwidth=0,activebackground='#212838',bg='#212838',command=search)
    search_btn.place(x=860,y=485)

    # selected_item = bills_tree.get_children()[0]
    # bills_tree.delete(selected_item)


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
        MainPage()
        root.update()
    else:
        error_lbl = tk.Label(root,text='Error Check your email or password',bg='#212838',fg='#e02838',font=('AcmeFont',10))
        error_lbl.place(x=850,y=620)
        error_lbl.after(2000, error_lbl.destroy)





root = Tk()

root.geometry('1920x1080')
root.resizable(False,False)
root.iconphoto(False, tk.PhotoImage(file='assets/logo.png'))



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

### contact icons

contact_mail_img = Image.open('assets/contact_mail.png')
contact_mail_img = contact_mail_img.resize((40, 40), Image.ANTIALIAS)
contact_mail_img = ImageTk.PhotoImage(contact_mail_img)

contact_discord_img = Image.open('assets/contact_discord.png')
contact_discord_img = contact_discord_img.resize((40, 40), Image.ANTIALIAS)
contact_discord_img = ImageTk.PhotoImage(contact_discord_img)

contact_github_img = Image.open('assets/contact_github.png')
contact_github_img =contact_github_img.resize((40, 40), Image.ANTIALIAS)
contact_github_img = ImageTk.PhotoImage(contact_github_img)

donate_img = Image.open('assets/donate.png')
donate_img = donate_img.resize((40, 40), Image.ANTIALIAS)
donate_img = ImageTk.PhotoImage(donate_img)

link_copied_img = Image.open('assets/link_copied.png')
link_copied_img = link_copied_img.resize((300, 85), Image.ANTIALIAS)
link_copied_img = ImageTk.PhotoImage(link_copied_img)


### Main screen widgets
 

search_btn_img = Image.open('assets/search_btn.png')
search_btn_img = search_btn_img.resize((100, 40), Image.ANTIALIAS)
search_btn_img = ImageTk.PhotoImage(search_btn_img)


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