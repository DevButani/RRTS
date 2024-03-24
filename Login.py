from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
from tkinter import *
import Clerk
import Supervisor
import Admin

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

window=Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
window.resizable(0, 0)
window.title('Road Repair and Tracking Software')
#Clerk.clerk_page(window,Database,"Andheri")
#Supervisor.supervisor_page(window,Database,"Andheri")
Admin.admin_page(window,Database)
window.mainloop()