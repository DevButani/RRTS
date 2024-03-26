from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
import re
import pandas as pd
from time import strftime
import datetime
import Clerk
import Supervisor
import Admin
import Mayor

gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.json")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("credentials.json")

drive = GoogleDrive(gauth)

database_folder = '1H5CUI-DRExlAleJwr0P_jlwh5c_GUJem'
links_file = '1i-PIzY2z8a0V7QKijE5zBI4bqPng749O'
links_df = pd.read_csv('https://drive.google.com/uc?id='+links_file)
database_file = {}
for col in links_df.columns:
    database_file[col] = links_df[col][0]

Database = (drive,database_folder,database_file)

login_info_df=pd.read_csv('https://drive.google.com/uc?id='+database_file['Login Info'])

# Get today's date
today = datetime.date.today()

# Get the day of the week
day_of_week = today.strftime("%A")

# Get the month
month = today.strftime("%B")

# Get the day of the month
day_of_month = today.strftime("%d")

# Get the year
year = today.strftime("%Y")

def update_time1():
    #Updates the label's text with the current time.
    string_time = strftime('%H:%M:%S %p')
    clock_label1.config(text=string_time)
    window.after(1000, update_time1)

def update_time2():
    #Updates the label's text with the current time.
    string_time = strftime('%H:%M:%S %p')
    clock_label2.config(text=string_time)
    window.after(1000, update_time2)


window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
window.resizable(0, 0)
window.title('Road Repair and Tracking Software')


LoginPage = Frame(window)
SignupPage = Frame(window)

for frame in (LoginPage, SignupPage):
    frame.grid(row=0, column=0, sticky='nsew')

def show_page(frame):
    frame.tkraise()

#login page 
    
login_listbox1=Listbox(LoginPage, bg="white", width=window.winfo_screenwidth(), height=window.winfo_screenheight(), highlightthickness=0, borderwidth=0)
login_listbox1.place(x=0,y=0)

side_bar1=Frame(LoginPage, bg="#5cdb95", height=window.winfo_screenheight(), width=int(window.winfo_screenwidth()*0.2), highlightthickness=0, borderwidth=0)
side_bar1.place(x=0,y=0)

central_frame1=Frame(LoginPage, bg="white", height=window.winfo_screenheight(), width=window.winfo_screenwidth()*0.8)
central_frame1.place(x=window.winfo_screenwidth()*0.2, y=0)

bg_img1 = Image.open('Images/bg0.png')
bg_pic1 = ImageTk.PhotoImage(bg_img1)

bg_label1=Label(side_bar1, image=bg_pic1, bg="black", width=window.winfo_screenwidth()*0.2, height=window.winfo_screenheight())
bg_label1.image=bg_pic1
bg_label1.place(x=0, y=0)

login_box1=Listbox(central_frame1, bg="#05386B", width=int(window.winfo_screenwidth()*0.08), height=int(window.winfo_screenheight()*0.04), highlightthickness=2, borderwidth=0, highlightbackground="#05386B", highlightcolor="#05386B")
login_box1.place(x=central_frame1.winfo_screenwidth()*0.17, y=central_frame1.winfo_screenheight()*0.19)

login_button1=Button(login_box1, command=lambda: show_page(LoginPage), fg="#5cdb95", bg="#05386B", text="Login", font=("yu gothic ui bold", 15), borderwidth=0, cursor='hand2', activebackground="#05386B", activeforeground="#5cdb95", width=int(login_box1.winfo_screenwidth()*0.0225))
login_button1.place(x=0, y=0)

signup_button1=Button(login_box1, command=lambda: show_page(SignupPage), fg="#8ee4af", bg="black", text="Sign Up", font=("yu gothic ui bold", 15), borderwidth=0, cursor='hand2', activebackground="#05386B", activeforeground="#5cdb95", width=int(login_box1.winfo_screenwidth()*0.0225))
signup_button1.place(x=login_box1.winfo_screenwidth()*0.235, y=0)

welcome_label1=Label(login_box1, fg="#5cdb95", bg="#05386B", font=("yu gothic ui bold", 20), text="Welcome back!")
welcome_label1.place(x=login_box1.winfo_screenwidth()*0.15, y=login_box1.winfo_screenheight()*0.075)

clock_icon1 = Image.open('Images/time.png')
clock_pic = ImageTk.PhotoImage(clock_icon1)
clock_icon_label1 = Label(login_box1, image=clock_pic, bg='#05386B')
clock_icon_label1.image = clock_pic
clock_icon_label1.place(x=login_box1.winfo_screenwidth()*0.025, y=login_box1.winfo_screenheight()*0.195)

clock_label1 = Label(login_box1, font=('calibri', 15, 'bold'), background='#05386B', foreground='white')
clock_label1.place(x=login_box1.winfo_screenwidth()*0.05, y=login_box1.winfo_screenheight()*0.2)
update_time1()

date_icon1 = Image.open('Images/date.png')
date_pic = ImageTk.PhotoImage(date_icon1)
date_icon_label1 = Label(login_box1, image=date_pic, bg='#05386B')
date_icon_label1.image = date_pic
date_icon_label1.place(x=login_box1.winfo_screenwidth()*0.025, y=login_box1.winfo_screenheight()*0.27)

date_label1=Label(login_box1, text=day_of_week+", \n"+month+" "+day_of_month+", \n"+year, fg="white", bg="#05386B", font=('calibri', 15, 'bold'))
date_label1.place(x=login_box1.winfo_screenwidth()*0.05, y=login_box1.winfo_screenheight()*0.275)

email_icon1 = Image.open('Images/email1.png')
email_pic = ImageTk.PhotoImage(email_icon1)
emailIcon_label1 = Label(login_box1, image=email_pic, bg='#05386B')
emailIcon_label1.image = email_pic
emailIcon_label1.place(x=login_box1.winfo_screenwidth()*0.195, y=login_box1.winfo_screenheight()*0.195)

email_entry1=Entry(login_box1, fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), highlightthickness=2, width=int(login_box1.winfo_screenwidth()*0.02), highlightcolor="white")
email_entry1.place(x=login_box1.winfo_screenwidth()*0.225, y=login_box1.winfo_screenheight()*0.2)
email_label1=Label(login_box1, text="• Email Id", fg="white", bg="#05386B", font=("yu gothic ui", 15, "bold"))
email_label1.place(x=login_box1.winfo_screenwidth()*0.225, y=login_box1.winfo_screenheight()*0.16)

password_icon1 = Image.open('Images/password1.png')
password_pic = ImageTk.PhotoImage(password_icon1)
password_icon_label1 = Label(login_box1, image=password_pic, bg='#05386B')
password_icon_label1.image = password_pic
password_icon_label1.place(x=login_box1.winfo_screenwidth()*0.195, y=login_box1.winfo_screenheight()*0.32)

password_entry1=Entry(login_box1, fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2, width=int(login_box1.winfo_screenwidth()*0.02), highlightcolor="white")
password_entry1.place(x=login_box1.winfo_screenwidth()*0.225, y=login_box1.winfo_screenheight()*0.325)
password_label1=Label(login_box1, text="• Password", fg="white", bg="#05386B", font=("yu gothic ui", 15, "bold"))
password_label1.place(x=login_box1.winfo_screenwidth()*0.225, y=login_box1.winfo_screenheight()*0.285)

# function for show and hide password
def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')

show_password = Checkbutton(login_box1, bg='#05386B', command=password_command, text='show password', fg="white", activebackground="#1f2833", activeforeground="#5cdb95", selectcolor="#05386B")
show_password.place(x=login_box1.winfo_screenwidth()*0.225, y=login_box1.winfo_screenheight()*0.37)

error_label1=Label(login_box1, text="", fg="red", bg="#05386B", font=("yu gothic ui", 11, 'bold'))
error_label1.place(x=login_box1.winfo_screenwidth()*0.225, y=login_box1.winfo_screenheight()*0.4)

# On pressing Login
def loginUser():
    email=email_entry1.get()
    password=password_entry1.get()
    global validUser, login_info_df
    validUser=False
    idx=login_info_df[login_info_df['Email Id'] == email]
    if len(idx)>0:
        validUser=True
        global ind
        ind=idx.index[0]
        if password==login_info_df['Password'][ind]:
            if login_info_df['Authorized'][ind]=='N':
                error_label1.config(text="Authorization Pending.\nPlease wait.")
            else:
                userType=login_info_df['Type'][ind]
                userLocality=login_info_df['Locality'][ind]
                email_entry1.delete(0, END)
                password_entry1.delete(0, END)
                if userType=="Clerk":
                    Clerk.clerk_page(window,Database,userLocality)
                elif userType=="Supervisor":
                    Supervisor.supervisor_page(window,Database,userLocality)
                elif userType=="Admin":
                    Admin.admin_page(window,Database)
                    login_info_df=pd.read_csv('temp.csv')
                else:
                    Mayor.mayor_page(window,Database)
        else:
            error_label1.config(text="Incorrect Email-Id or Password.\nTry Again.")
            password_entry1.delete(0,END)
    else:
        error_label1.config(text='No Acount linked with given Email Id.\nPlease Sign Up.')
        email_entry1.delete(0, END)
        password_entry1.delete(0, END)

login_button_down=Button(login_box1, text="Login", bg="white", fg="#05386B", font=("yu gothic ui bold", 17), cursor="hand2", activebackground="white", activeforeground="#05386B", borderwidth=0, width=int(login_box1.winfo_screenwidth()*0.01), command=loginUser)
login_button_down.place(x=login_box1.winfo_screenwidth()*0.25, y=login_box1.winfo_screenheight()*0.5)

partition_frame1=Frame(login_box1, bg="white", width=int(login_box1.winfo_screenwidth()*0.0025), height=int(login_box1.winfo_screenheight()*0.35))
partition_frame1.place(x=login_box1.winfo_screenwidth()*0.165, y=login_box1.winfo_screenheight()*0.15)

#sign up page

login_listbox2=Listbox(SignupPage, bg="white", width=window.winfo_screenwidth(), height=window.winfo_screenheight(), highlightthickness=0, borderwidth=0)
login_listbox2.place(x=0,y=0)

side_bar2=Frame(SignupPage, bg="#5cdb95", height=window.winfo_screenheight(), width=int(window.winfo_screenwidth()*0.2), highlightthickness=0, borderwidth=0)
side_bar2.place(x=0,y=0)

central_frame2=Frame(SignupPage, bg="white", height=window.winfo_screenheight(), width=window.winfo_screenwidth()*0.8)
central_frame2.place(x=window.winfo_screenwidth()*0.2, y=0)

bg_img2 = Image.open('Images/bg0.png')
# bg_img1.resize((side_bar1.winfo_width(), side_bar1.winfo_height()))
bg_pic2 = ImageTk.PhotoImage(bg_img2)

bg_label2=Label(side_bar2, image=bg_pic2, bg="black", width=window.winfo_screenwidth()*0.2, height=window.winfo_screenheight())
bg_label2.image=bg_pic2
bg_label2.place(x=0, y=0)

login_box2=Listbox(central_frame2, bg="#05386B", width=int(window.winfo_screenwidth()*0.08), height=int(window.winfo_screenheight()*0.04), highlightthickness=2, borderwidth=0, highlightbackground="#05386B", highlightcolor="#05386B")
login_box2.place(x=central_frame2.winfo_screenwidth()*0.17, y=central_frame2.winfo_screenheight()*0.19)

login_button2=Button(login_box2, command=lambda: show_page(LoginPage), fg="#8ee4af", bg="black", text="Login", font=("yu gothic ui bold", 15), borderwidth=0, cursor='hand2', activebackground="#05386B", activeforeground="#5cdb95", width=int(login_box2.winfo_screenwidth()*0.0225))
login_button2.place(x=0, y=0)

signup_button2=Button(login_box2, command=lambda: show_page(SignupPage), fg="#5cdb95", bg="#05386B", text="Sign Up", font=("yu gothic ui bold", 15), borderwidth=0, cursor='hand2', activebackground="#05386B", activeforeground="#5cdb95", width=int(login_box2.winfo_screenwidth()*0.0225))
signup_button2.place(x=login_box2.winfo_screenwidth()*0.235, y=0)

# welcome_label2=Label(login_box2, fg="#5cdb95", bg="#05386B", font=("yu gothic ui bold", 20), text="Hello, new user!!")
# welcome_label2.place(x=login_box2.winfo_screenwidth()*0.15, y=login_box2.winfo_screenheight()*0.075)

clock_pic = ImageTk.PhotoImage(clock_icon1)
clock_icon_label2 = Label(login_box2, image=clock_pic, bg='#05386B')
clock_icon_label2.image = clock_pic
clock_icon_label2.place(x=login_box2.winfo_screenwidth()*0.025, y=login_box2.winfo_screenheight()*0.095)

clock_label2 = Label(login_box2, font=('calibri', 15, 'bold'), background='#05386B', foreground='white')
clock_label2.place(x=login_box2.winfo_screenwidth()*0.05, y=login_box2.winfo_screenheight()*0.1)
update_time2()

date_pic = ImageTk.PhotoImage(date_icon1)
date_icon_label2 = Label(login_box2, image=date_pic, bg='#05386B')
date_icon_label2.image = date_pic
date_icon_label2.place(x=login_box2.winfo_screenwidth()*0.025, y=login_box2.winfo_screenheight()*0.17)

date_label2=Label(login_box2, text=day_of_week+", \n"+month+" "+day_of_month+", \n"+year, fg="white", bg="#05386B", font=('calibri', 15, 'bold'))
date_label2.place(x=login_box2.winfo_screenwidth()*0.05, y=login_box2.winfo_screenheight()*0.175)

partition_frame2=Frame(login_box2, bg="white", width=int(login_box2.winfo_screenwidth()*0.0025), height=int(login_box2.winfo_screenheight()*0.5))
partition_frame2.place(x=login_box2.winfo_screenwidth()*0.165, y=login_box2.winfo_screenheight()*0.075)

head=Label(login_box2, text='', fg="white", bg='#05386b', font=("yu gothic ui", 11, 'bold'))
head.place(x=login_box2.winfo_screenwidth()*0.015, y=login_box2.winfo_screenheight()*0.3)
condition1=Label(login_box2, text='', fg="red", bg='#05386b', font=("yu gothic ui", 11, 'bold'))
condition1.place(x=login_box2.winfo_screenwidth()*0.015, y=login_box2.winfo_screenheight()*0.325)
condition2=Label(login_box2, text='', fg="red", bg='#05386b', font=("yu gothic ui", 11, 'bold'))
condition2.place(x=login_box2.winfo_screenwidth()*0.015, y=login_box2.winfo_screenheight()*0.35)
condition3=Label(login_box2, text='', fg="red", bg='#05386b', font=("yu gothic ui", 11, 'bold'))
condition3.place(x=login_box2.winfo_screenwidth()*0.015, y=login_box2.winfo_screenheight()*0.375)
condition4=Label(login_box2, text='', fg="red", bg='#05386b', font=("yu gothic ui", 11, 'bold'))
condition4.place(x=login_box2.winfo_screenwidth()*0.015, y=login_box2.winfo_screenheight()*0.4)
condition5=Label(login_box2, text='', fg="red", bg='#05386b', font=("yu gothic ui", 11, 'bold'))
condition5.place(x=login_box2.winfo_screenwidth()*0.015, y=login_box2.winfo_screenheight()*0.425)


#type, name, locality, password,emailid, confirm pass
# Type
type_options=["Clerk", "Supervisor"]
type_variable = StringVar()
type_variable.set(type_options[0])
type_menu = OptionMenu(login_box2, type_variable, *type_options)
type_menu.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white")
tmenu=login_box2.nametowidget(type_menu.menuname)
tmenu.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
type_menu.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.10, width=int(login_box2.winfo_screenwidth()*0.18), height=35)
type_label = Label(login_box2, text='• Type of Account', fg="white", bg='#05386B', font=("yu gothic ui", 11, 'bold'))
type_label.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.07)

name_entry1=Entry(login_box2, fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), highlightthickness=2, width=int(login_box2.winfo_screenwidth()*0.02), highlightcolor="white")
name_entry1.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.17)
name_label1=Label(login_box2, text="• Name", fg="white", bg="#05386B", font=("yu gothic ui", 11, "bold"))
name_label1.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.14)

locality_options = [x for x in links_df.columns.to_list() if(x[:3]!="new" and x!="Resources" and x!="Login Info")]
locality_variable = StringVar()
locality_variable.set(locality_options[0])
locality_menu = OptionMenu(login_box2, locality_variable, *locality_options)
locality_menu.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white")
lmenu=login_box2.nametowidget(locality_menu.menuname)
lmenu.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
locality_menu.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.24, width=int(login_box2.winfo_screenwidth()*0.18), height=35)
locality_label = Label(login_box2, text='• Locality', fg="white", bg='#05386B', font=("yu gothic ui", 11, 'bold'))
locality_label.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.21)

emailId2=StringVar()

email_entry2=Entry(login_box2, text=(emailId2), fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), highlightthickness=2, width=int(login_box2.winfo_screenwidth()*0.02), highlightcolor="white")
email_entry2.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.31)
email_label2=Label(login_box2, text="• Email Id", fg="white", bg="#05386B", font=("yu gothic ui", 11, "bold"))
email_label2.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.28)

# UserIdChecker

def userIdCheck(*args):
    str2=emailId2.get()
    condition1.config(text='')
    global userIdValid
    if re.match(r"^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9_\-.]+\.[a-zA-Z]{2,}$", str2):
        userIdValid=True
    else:
        condition1.config(text='Invalid Email Id', fg="red")
        userIdValid=False
    if userIdValid:
        if str2 in login_info_df['Email Id']:
            condition1.config(text='Email Id Already Exists', fg="red")
            userIdValid=False
        else:
            condition1.config(text='')


def userIdActive():
    emailId2.trace('w', userIdCheck)

def userIdInactive():
    condition1.config(text='')
    

email_entry2.bind('<Enter>', lambda event: userIdActive())
email_entry2.bind('<Leave>', lambda event: userIdInactive())


password2=StringVar()

password_entry2=Entry(login_box2, text=(password2), fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2, width=int(login_box2.winfo_screenwidth()*0.02), highlightcolor="white")
password_entry2.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.38)
password_label2=Label(login_box2, text="• Password", fg="white", bg="#05386B", font=("yu gothic ui", 11, "bold"))
password_label2.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.35)


#password checker
req=list((False, False, False, False, False, True))

def passwordCheck(*args):
    str1=password2.get()
    head.config(text='• Password must contain:')
    condition1.config(text='• 8-12 characters')
    condition4.config(text='• At least one number')
    condition3.config(text='• At least one lowercase letter')
    condition2.config(text='• At least one uppercase letter')
    condition5.config(text='• At least one special character')
    condition1.config(fg='red')
    condition2.config(fg='red')
    condition3.config(fg='red')
    condition4.config(fg='red')
    condition5.config(fg='red')
    specialCharacter=list(('!','@','#','$','%','&','*'))
    for i in range(len(str1)):
        if(i>=7):
            condition1.config(fg='green')
            
            req[0]=True
        if(i>11):
            condition1.config(fg='red')

            req[0]=False
        if(str1[i]>='0' and str1[i]<='9'):
            condition4.config(fg='green')
            
            req[3]=True
        elif(str1[i]>='a' and str1[i]<='z'):
            condition3.config(fg='green')
            
            req[2]=True
        elif(str1[i]>='A' and str1[i]<='Z'):
            condition2.config(fg='green')
            
            req[1]=True
        elif str1[i] in specialCharacter:
            condition5.config(fg='green')
            
            req[4]=True
        req[5]=True
        for j in range(5):
            if(req[j]==False):
                req[j]=False
                break

    

def passwordActive():
    password2.trace('w', passwordCheck)

def passwordInactive():
    head.config(text='')
    condition1.config(text='')
    condition4.config(text='')
    condition3.config(text='')
    condition2.config(text='')
    condition5.config(text='')



password_entry2.bind('<Enter>', lambda event: passwordActive())
password_entry2.bind('<Leave>', lambda event: passwordInactive())

# function for show and hide password
def password_command2():
    if password_entry2.cget('show') == '•':
        password_entry2.config(show='')
    else:
        password_entry2.config(show='•')

show_password2= Checkbutton(login_box2, bg='#05386B', command=password_command2, text='show password', fg="white", activebackground="#1f2833", activeforeground="#5cdb95", selectcolor="#05386B")
show_password2.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.42)

confirm_password=StringVar()

confirm_password_entry2=Entry(login_box2, text=(confirm_password), fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2, width=int(login_box2.winfo_screenwidth()*0.02), highlightcolor="white")
confirm_password_entry2.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.48)
confirm_password_label2=Label(login_box2, text="• Password", fg="white", bg="#05386B", font=("yu gothic ui", 11, "bold"))
confirm_password_label2.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.45)

def confirmPasswordCheck(*args):
    condition1.config(text='Confirm Password must be \nsame as Password')
    condition1.config(fg='red')
    str3=confirm_password.get()
    global pEqual
    if(str3==password1):
        condition1.config(fg='green')
        pEqual=True
    else:
        condition1.config(fg='red')
        pEqual=False

def confirmPasswordActive():
    global password1
    password1=password2.get()
    confirm_password.trace('w', confirmPasswordCheck)

def confirmPasswordInactive():
    head.config(text='')
    condition1.config(text='')
    condition4.config(text='')
    condition3.config(text='')
    condition2.config(text='')
    condition5.config(text='')
    


confirm_password_entry2.bind('<Enter>', lambda event: confirmPasswordActive())
confirm_password_entry2.bind('<Leave>', lambda event: confirmPasswordInactive())

# function for show and hide password
def confirm_password_command2():
    if confirm_password_entry2.cget('show') == '•':
        confirm_password_entry2.config(show='')
    else:
        confirm_password_entry2.config(show='•')

show_confirm_password2= Checkbutton(login_box2, bg='#05386B', command=confirm_password_command2, text='show password', fg="white", activebackground="#1f2833", activeforeground="#5cdb95", selectcolor="#05386B")
show_confirm_password2.place(x=login_box2.winfo_screenwidth()*0.225, y=login_box2.winfo_screenheight()*0.52)

def signUp():
    global login_info_df
    head.config(text="")
    condition1.config(text="")
    condition2.config(text="")
    condition3.config(text="")
    if not userIdValid:
        head.config(text="Error")
        condition1.config(text="• Invalid Email Id.", fg="red")
    if not req[5]:
        head.config(text="Error")
        condition2.config(text="• Password not satisfying\n all conditions.", fg="red")
    if not pEqual:
        head.config(text="Error")
        condition3.config(text="• Confirm password not \nsame as Password.", fg="red")
    if userIdValid and req[5] and pEqual:
        temp_dict=[{'Type': type_variable.get(), 'Name': name_entry1.get(), 'Locality': locality_variable.get(), 'Email Id': emailId2.get(), 'Password': password2.get(), 'Authorized': 'N'}]
        temp_df=pd.DataFrame(temp_dict)
        login_info_df=pd.concat([login_info_df,temp_df], ignore_index=True)
        login_info_df.to_csv('temp.csv', index=False)
        file_obj = drive.CreateFile({'parents': [{'id': database_folder}], 'id': database_file['Login Info']})
        file_obj.SetContentFile(filename='temp.csv')
        file_obj.Upload()
        name_entry1.delete(0,END)
        type_variable.set(type_options[0])
        email_entry2.delete(0,END)
        password_entry2.delete(0,END)
        locality_variable.set(locality_options[0])
        confirm_password_entry2.delete(0,END)
        head.config(text="Account details sent\nto Admin for\nAuthorization.\nPlease wait.")
        condition1.config(text="")
        condition2.config(text="")
        condition3.config(text="")
        condition4.config(text="")
        condition5.config(text="")
        


signup_button_down=Button(login_box2, text="Sign Up", bg="white", fg="#05386B", font=("yu gothic ui bold", 17), cursor="hand2", activebackground="white", activeforeground="#05386B", borderwidth=0, width=int(login_box2.winfo_screenwidth()*0.01), command=signUp)
signup_button_down.place(x=login_box2.winfo_screenwidth()*0.25, y=login_box2.winfo_screenheight()*0.56)

show_page(SignupPage)

window.mainloop()