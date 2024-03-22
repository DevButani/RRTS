import pandas as pd
#import numpy as np
import tkinter as tk
from tkinter import *
from datetime import date


def update_resources_page(window):
    resources_file="test.csv"
    
    resource_name=StringVar()
    resource_name.set("--")
    resource_type=StringVar()
    resource_type.set("--")
    resource_count=IntVar()
    resource_count.set(0)

    def register_entries():
        resource_df=pd.read_csv(resources_file)
        # print(resource_df.head())
        # print(resource_name.get(),resource_type.get(),resource_count.get())
        resource_df.iloc[((resource_df['Resource Type']==resource_name.get()) & (resource_df['Name']==resource_type.get())),2]=resource_count.get()
        # print(((resource_df['Resource_name']==resource_name.get()) & (resource_df['Type']==resource_type.get())))
        # print(resource_df.head())
        # resource_df.loc[[(resource_df['Resource_name']==resource_name.get()) & (resource_df['Type']==resource_type.get())],['Available_units']]==resource_count.get()
        resource_df.to_csv(resources_file,index=False)
        resource_name.set("--")
        resource_type.set("--")
        resource_count.set(0)


    resource_frame=Frame(window)
    Label(resource_frame,text="Choose Resource ",font=('Courier New Greek',18)).pack(pady=20)
    resource_menu=OptionMenu(resource_frame,resource_name,"Manpower","Machinery","Others")
    resource_menu.config(font=('Courier New Greek',15),width=18)
    resource_menu.pack(anchor=CENTER,padx=70)

    '''Get the different types of the chosen resources using a function.
    FUNCTION TO BE DEFINED LATER ......basically finds unique entries in the column'''
    type_list=['1','2','3']


    Label(resource_frame,text="Choose Type ",font=('Courier New Greek',18)).pack(pady=20)
    type_menu=OptionMenu(resource_frame,resource_type,*type_list,'others')
    type_menu.config(font=('Courier New Greek',15),width=18)
    type_menu.pack(anchor=CENTER,padx=70)


    Label(resource_frame,text="Enter the total number of units :",font=('Courier New Greek',18)).pack(pady=15)
    street_entry=Entry(resource_frame,textvariable=resource_count,font=('Courier New Greek',15))
    street_entry.pack()
    Button(resource_frame,text="Register", font=('Poppins bold', 18),command=register_entries).pack()
    resource_frame.pack()



def check_resources_page(window):
    resources_file='test.csv'
    page_frame=Frame(window)
    display_df=pd.read_csv(resources_file)
    display_frame=Frame(page_frame)
    Label(display_frame,text="Resource Utilisation  Information ",font=('Courier New Greek',22,'underline','bold')).grid(row=0,column=0,columnspan=4,pady=(0,10))
    resource_list_var=[StringVar()]
    resource_list_var[0].set("Resource Type")
    resource_list_entry=[Entry(display_frame,textvariable=resource_list_var[0])]
    resource_list_entry[0].config(state='disabled')
    resource_list_entry[0].grid(row=1,column=0)
    type_list_var=[StringVar()]
    type_list_var[0].set("Resource Name")
    type_list_entry=[Entry(display_frame,textvariable=type_list_var[0])]
    type_list_entry[0].config(state='disabled')
    type_list_entry[0].grid(row=1,column=1)
    num_available_var=[StringVar()]
    num_available_var[0].set("Total Number Available")
    num_available_entry=[Entry(display_frame,textvariable=num_available_var[0])]
    num_available_entry[0].config(state='disabled')
    num_available_entry[0].grid(row=1,column=2)
    num_in_use_var=[StringVar()]
    num_in_use_var[0].set("Number In Use")
    num_in_use_entry=[Entry(display_frame,textvariable=num_in_use_var[0])]
    num_in_use_entry[0].config(state='disabled')
    num_in_use_entry[0].grid(row=1,column=3)
    for i in display_df.index:
        resource_list_var.append(StringVar())
        resource_list_var[i+1].set(str(display_df.iat[i,0]))
        resource_list_entry.append(Entry(display_frame,textvariable=resource_list_var[i+1]))
        resource_list_entry[i+1].config(state='disabled')
        resource_list_entry[i+1].grid(row=i+2,column=0)
        type_list_var.append(StringVar())
        type_list_var[i+1].set(str(display_df.iat[i,1]))
        type_list_entry.append(Entry(display_frame,textvariable=type_list_var[i+1]))
        type_list_entry[i+1].config(state='disabled')
        type_list_entry[i+1].grid(row=i+2,column=1)
        num_available_var.append(StringVar())
        num_available_var[i+1].set(str(display_df.iat[i,2]))
        num_available_entry.append(Entry(display_frame,textvariable=num_available_var[i+1]))
        num_available_entry[i+1].config(state='disabled')
        num_available_entry[i+1].grid(row=i+2,column=2)
        num_in_use_var.append(StringVar())
        num_in_use_var[i+1].set(str(display_df.iat[i,3]))
        num_in_use_entry.append(Entry(display_frame,textvariable=num_in_use_var[i+1]))
        num_in_use_entry[i+1].config(state='disabled')
        num_in_use_entry[i+1].grid(row=i+2,column=3)
    display_frame.pack()
    page_frame.pack()




    