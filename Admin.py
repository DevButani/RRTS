import pandas as pd
#import numpy as np
from tkinter import *
from datetime import date

def admin_page(window,Database):
    admin_frame=Frame(window)
    admin_frame.pack()
    resources_df=pd.read_csv('https://drive.google.com/uc?id='+Database[2]["Resources"])

    def update_resources_page():
        resource_type=StringVar()
        resource_type.set("--")
        resource_name=StringVar()
        resource_name.set("--")
        resource_count=IntVar()
        resource_count.set(0)

        def register_entries():
            resources_df.iloc[((resources_df['Resource Type']==resource_type.get()) & (resources_df['Name']==resource_name.get())),2]=resource_count.get()
            resource_type.set("--")
            resource_name.set("--")
            resource_count.set(0)

        def set_resource_names(type):
            menu=resource_name_menu["menu"]
            menu.delete(0,"end")
            for string in name_list[type]:
                menu.add_command(label=string, command=lambda value=string: resource_name.set(value))
        resource_frame=Frame(admin_frame)
        Label(resource_frame,text="Choose Resource ",font=('Courier New Greek',18)).pack(pady=20)
        name_list=["Raw Materials","Machines","Personnel"]
        resource_type_menu=OptionMenu(resource_frame,resource_type,*name_list, command=set_resource_names)
        resource_type_menu.config(font=('Courier New Greek',15),width=18)
        resource_type_menu.pack(anchor=CENTER,padx=70)

        name_list={
            "--": ["--"],
            "Raw Materials": ["Asphalt", "Bitumen", "Concrete"],
            "Machines": ["Bulldozer", "Road Roller", "Concrete Mixer", "Jackhammer"],
            "Personnel": ["Engineer", "Worker", "Machine Operator"]
        }

        Label(resource_frame,text="Choose Type ",font=('Courier New Greek',18)).pack(pady=20)
        resource_name_menu=OptionMenu(resource_frame,resource_name,"--")
        resource_name_menu.config(font=('Courier New Greek',15),width=18)
        resource_name_menu.pack(anchor=CENTER,padx=70)

        Label(resource_frame,text="Enter the total number of units :",font=('Courier New Greek',18)).pack(pady=15)
        street_entry=Entry(resource_frame,textvariable=resource_count,font=('Courier New Greek',15))
        street_entry.pack()
        Button(resource_frame,text="Register", font=('Poppins bold', 18),command=register_entries).pack()
        resource_frame.pack()

    #Button(admin_frame, text="Update Resources", command=update_resources_page).pack()

    def check_resources_page():
        page_frame=Frame(admin_frame)
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
        num_available_var[0].set("Total Available")
        num_available_entry=[Entry(display_frame,textvariable=num_available_var[0])]
        num_available_entry[0].config(state='disabled')
        num_available_entry[0].grid(row=1,column=2)
        num_in_use_var=[StringVar()]
        num_in_use_var[0].set("In Use")
        num_in_use_entry=[Entry(display_frame,textvariable=num_in_use_var[0])]
        num_in_use_entry[0].config(state='disabled')
        num_in_use_entry[0].grid(row=1,column=3)
        for i in resources_df.index:
            resource_list_var.append(StringVar())
            resource_list_var[i+1].set(str(resources_df.iat[i,0]))
            resource_list_entry.append(Entry(display_frame,textvariable=resource_list_var[i+1]))
            resource_list_entry[i+1].config(state='disabled')
            resource_list_entry[i+1].grid(row=i+2,column=0)
            type_list_var.append(StringVar())
            type_list_var[i+1].set(str(resources_df.iat[i,1]))
            type_list_entry.append(Entry(display_frame,textvariable=type_list_var[i+1]))
            type_list_entry[i+1].config(state='disabled')
            type_list_entry[i+1].grid(row=i+2,column=1)
            num_available_var.append(StringVar())
            num_available_var[i+1].set(str(resources_df.iat[i,2]))
            num_available_entry.append(Entry(display_frame,textvariable=num_available_var[i+1]))
            num_available_entry[i+1].config(state='disabled')
            num_available_entry[i+1].grid(row=i+2,column=2)
            num_in_use_var.append(StringVar())
            num_in_use_var[i+1].set(str(resources_df.iat[i,3]))
            num_in_use_entry.append(Entry(display_frame,textvariable=num_in_use_var[i+1]))
            num_in_use_entry[i+1].config(state='disabled')
            num_in_use_entry[i+1].grid(row=i+2,column=3)
        display_frame.pack()
        page_frame.pack()
    
    #Button(admin_frame, text="Check Resources", command=check_resources_page).pack()

    update_resources_page()
    check_resources_page()

    def exit():
        resources_df.to_csv('temp.csv', index=False)
        file_obj = Database[0].CreateFile({'parents': [{'id': Database[1]}], 'id': Database[2]["Resources"]})
        file_obj.SetContentFile(filename='temp.csv')
        file_obj.Upload()
        admin_frame.destroy()
    Button(admin_frame, text="Log Out", command=exit).pack()