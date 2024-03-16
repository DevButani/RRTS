import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import *

def clerk_page(window):
    #clerk_db=pd.read_csv("File_name.csv")

    prob_type=StringVar()
    prob_type.set("--")
    street_name=StringVar()
    street_name.set("--")
    clerk_frame=Frame(window)
    Label(clerk_frame,text="Choose the type of Problem ",font=('Courier New Greek',18)).pack(pady=20)
    prob_menu=OptionMenu(clerk_frame,prob_type,"Pothole","Broken Curb","Others")
    prob_menu.config(font=('Courier New Greek',15),width=18)
    prob_menu.pack(anchor=CENTER,padx=70)
    Label(clerk_frame,text="Enter the Street Name :",font=('Courier New Greek',18)).pack(pady=15)
    street_entry=Entry(clerk_frame,textvariable=street_name,font=('Courier New Greek',15))
    street_entry.pack()