import pandas as pd
from tkinter import *
from datetime import date

def commit_changes(file_name,append_df):
    append_df.to_csv(file_name,mode='a',header=False,index=False)

def clerk_page(window,Database,locality):
    new_complaints_df = pd.read_csv('https://drive.google.com/uc?id='+Database[2]["new "+locality])
    prob_type = StringVar()
    prob_type.set("--")
    street_name = StringVar()
    street_name.set("")
    def register_entries():
        entry_list = [{"Locality":str(locality),"Street":street_name.get(),"Problem":prob_type.get(),"Reporting Date":str(date.today())}]
        nonlocal new_complaints_df
        new_complaints_df = pd.concat([new_complaints_df,pd.DataFrame(entry_list)], ignore_index=True)
        prob_type.set('--')
        street_name.set('')
    clerk_frame = Frame(window)
    Label(clerk_frame, text="Choose the type of Problem ", font=('Courier New Greek',18)).pack(pady=20)
    prob_menu = OptionMenu(clerk_frame,prob_type,"Pothole","Broken Curb","Others")
    prob_menu.config(font=('Courier New Greek',15), width=18)
    prob_menu.pack(anchor=CENTER, padx=70)
    Label(clerk_frame, text="Enter the Street Name :", font=('Courier New Greek',18)).pack(pady=15)
    street_entry = Entry(clerk_frame, textvariable=street_name, font=('Courier New Greek',15))
    street_entry.pack()
    Button(clerk_frame, text="Register", font=('Poppins bold', 18), command=register_entries).pack()
    clerk_frame.pack()

    def exit():
        new_complaints_df.to_csv('temp.csv', index=False)
        file_obj = Database[0].CreateFile({'parents': [{'id': Database[1]}], 'id': Database[2]['new '+locality]})
        file_obj.SetContentFile(filename='temp.csv')
        file_obj.Upload()
        clerk_frame.destroy()
    Button(clerk_frame, text="Log Out", command=exit).pack()