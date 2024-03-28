import pandas as pd
#import numpy as np
from tkinter import *
from functools import partial
from datetime import date

def admin_page(window,Database):
    admin_frame=Frame(window)
    admin_frame.grid(row=0, column=0, sticky='nsew')

    resources_df=pd.read_csv('https://drive.google.com/uc?id='+Database[2]["Resources"])
    login_info_df=pd.read_csv('temp.csv')
    unauthorized_df=login_info_df[login_info_df['Authorized']=='N']
    authorized_df=login_info_df[login_info_df['Authorized']=='Y']
    login_info_df.drop(login_info_df[login_info_df['Authorized']!='-'].index, inplace=True)
    unauthorized_df.reset_index(inplace=True, drop=True)
    authorized_df.reset_index(inplace=True, drop=True)
    unauthorized_df=pd.concat([unauthorized_df,authorized_df], ignore_index=True)

    resource_frame=Frame(admin_frame)
    display_frame=Frame(admin_frame)
    authorization_frame=Frame(admin_frame)

    resources_updated=False
    login_info_updated=False

    rsrc_not_packed=True
    auth_not_packed=True

    def update_resources_page():
        display_frame.pack_forget()
        authorization_frame.pack_forget()

        nonlocal rsrc_not_packed
    
        resource_type=StringVar()
        resource_type.set("[select]")
        resource_name=StringVar()
        resource_name.set("[select]")
        resource_count=IntVar()
        resource_count.set(0)

        def register_entries():
            nonlocal resources_updated
            resources_updated = True
            resources_df.iloc[((resources_df['Resource Type']==resource_type.get()) & (resources_df['Name']==resource_name.get())),2]=resource_count.get()
            resource_type.set("[select]")
            resource_name.set("[select]")
            resource_count.set(0)

        def set_resource_names(type):
            menu=resource_name_menu["menu"]
            menu.delete(0,"end")
            for string in name_list[type]:
                menu.add_command(label=string, command=lambda value=string: resource_name.set(value))
            resource_name.set("[select]")

        if rsrc_not_packed:
            Label(resource_frame,text="Choose Resource ",font=('Courier New Greek',18)).pack(pady=20)
            type_list=["Raw Materials","Machines","Personnel"]
            resource_type_menu=OptionMenu(resource_frame,resource_type,*type_list, command=set_resource_names)
            resource_type_menu.config(font=('Courier New Greek',15),width=18)
            resource_type_menu.pack(anchor=CENTER,padx=70)

            name_list={
                "Raw Materials": ["Asphalt", "Bitumen", "Concrete"],
                "Machines": ["Bulldozer", "Road Roller", "Concrete Mixer", "Jackhammer"],
                "Personnel": ["Engineer", "Worker", "Machine Operator"]
            }

            Label(resource_frame,text="Choose Type ",font=('Courier New Greek',18)).pack(pady=20)
            resource_name_menu=OptionMenu(resource_frame,resource_name,"[select]")
            resource_name_menu.config(font=('Courier New Greek',15),width=18)
            resource_name_menu.pack(anchor=CENTER,padx=70)

            Label(resource_frame,text="Enter the total number of units :",font=('Courier New Greek',18)).pack(pady=15)
            street_entry=Entry(resource_frame,textvariable=resource_count,font=('Courier New Greek',15))
            street_entry.pack()
            Button(resource_frame,text="Register", font=('Poppins bold', 18),command=register_entries).pack()
            
            rsrc_not_packed=False

        resource_frame.pack()

    Button(admin_frame, text="Update Resources", command=update_resources_page).pack()


    def check_resources_page():
        resource_frame.pack_forget()
        authorization_frame.pack_forget()

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

    Button(admin_frame, text="Check Resources", command=check_resources_page).pack()


    def authorize_registrations():
        resource_frame.pack_forget()
        display_frame.pack_forget()

        nonlocal login_info_df, unauthorized_df, auth_not_packed
        authorization_canvas = Canvas(authorization_frame, width=500)

        records = []
        def change_status(row):
            nonlocal unauthorized_df, login_info_updated
            login_info_updated = True
            if unauthorized_df['Authorized'][row]=="Y": unauthorized_df.at[row, 'Authorized'] = "N"
            elif unauthorized_df['Authorized'][row]=="N": unauthorized_df.at[row, 'Authorized'] = "Y"
            records[row].config(text=unauthorized_df['Locality'][row] + " | " + unauthorized_df['Type'][row] + " | " + unauthorized_df['Name'][row] + " | " + unauthorized_df['Email Id'][row] + " | Status: " + unauthorized_df['Authorized'][row])
        y = 0
        row_count=len(unauthorized_df.index)
        for row in range(row_count):
            records.append(Label(authorization_canvas, text=unauthorized_df['Locality'][row] + " | " + unauthorized_df['Type'][row] + " | " + unauthorized_df['Name'][row] + " | " + unauthorized_df['Email Id'][row] + " | Status: " + unauthorized_df['Authorized'][row]))
            authorization_canvas.create_window(0, y, window=records[row], anchor=NW)
            status_button=Button(authorization_canvas, text="Change Status", command=partial(change_status, row))
            authorization_canvas.create_window(400, y, window=status_button, anchor=NW)
            y += 20

        scrollbar = Scrollbar(authorization_canvas, orient=VERTICAL, command=authorization_canvas.yview)
        scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
        authorization_canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))
        
        if auth_not_packed:
            authorization_canvas.pack()
            auth_not_packed=False

        authorization_frame.pack()

    Button(admin_frame, text="Authorize New Registrations", command=authorize_registrations).pack()


    admin_frame.tkraise()

    def exit():
        nonlocal login_info_df, unauthorized_df
        if resources_updated:
            resources_df.to_csv('temp.csv', index=False)
            file_obj = Database[0].CreateFile({'parents': [{'id': Database[1]}], 'id': Database[2]["Resources"]})
            file_obj.SetContentFile(filename='temp.csv')
            file_obj.Upload()

        login_info_df = pd.concat([login_info_df,unauthorized_df], ignore_index=True)
        login_info_df.to_csv('temp.csv', index=False)
        if login_info_updated:
            file_obj = Database[0].CreateFile({'parents': [{'id': Database[1]}], 'id': Database[2]["Login Info"]})
            file_obj.SetContentFile(filename='temp.csv')
            file_obj.Upload()
        
        admin_frame.destroy()

    Button(admin_frame, text="Log Out", command=exit).pack()