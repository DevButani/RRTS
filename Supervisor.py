from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
import pandas as pd
from functools import partial

def supervisor_page(window,Database,locality):
    new_complaints_df=pd.read_csv('https://drive.google.com/uc?id='+Database[2]["new "+locality])

    complaints_df=pd.read_csv('https://drive.google.com/uc?id='+Database[2][locality])

    display_df = complaints_df[(complaints_df['Status']=='In Progress')]
    complaints_df.drop(complaints_df[(complaints_df['Status']=='In Progress')].index, inplace=True)
    display_df.reset_index(inplace=True, drop=True)

    current_complaint_no=0
    temp_dict={}

    schedule_report_frame=Frame(window)
    complaints_frame=Frame(window)

    for frame in (complaints_frame, schedule_report_frame):
        frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(frame):
        frame.tkraise()

    #schedule report frame

    def exit():
        nonlocal complaints_df, new_complaints_df
        complaints_df = pd.concat([complaints_df, display_df], ignore_index=True)
        complaints_df.to_csv('temp.csv', index=False)
        file_obj = Database[0].CreateFile({'parents': [{'id': Database[1]}], 'id': Database[2][locality]})
        file_obj.SetContentFile(filename='temp.csv')
        file_obj.Upload()
        new_complaints_df.to_csv('temp.csv', index=False)
        file_obj = Database[0].CreateFile({'parents': [{'id': Database[1]}], 'id': Database[2]['new '+locality]})
        file_obj.SetContentFile(filename='temp.csv')
        file_obj.Upload()
        schedule_report_frame.destroy()
        complaints_frame.destroy()

    logout_img=Image.open('Images/logout1.png')
    logout_pic=ImageTk.PhotoImage(logout_img)

    header1=Listbox(schedule_report_frame, bg="#5cdb95", width=schedule_report_frame.winfo_screenwidth(), height=int(schedule_report_frame.winfo_screenheight()*0.01), borderwidth=0, highlightthickness=0)
    header1.place(x=0,y=0)

    title1=Label(header1, text="SUPERVISOR", bg="#5cdb95", fg="#05386b", font=("yu gothic ui bold", 30))
    title1.place(x=header1.winfo_screenwidth()*0.4, y=header1.winfo_screenheight()*0.01)

    logout_button1=Button(header1, text="Logout  ", image=logout_pic, bg="#5cdb95", fg="#05386b", font=("yu gothic ui", 15), borderwidth=0, highlightthickness=0, activebackground="#5cdb95", activeforeground="#05386b", cursor="hand2", compound="right", command=exit)
    logout_button1.image=logout_pic
    logout_button1.place(x=header1.winfo_screenwidth()*0.9, y=header1.winfo_screenheight()*0.01)

    new_complaints_button1=Button(header1, text="New Complaints", bg="#5cdb95", fg="#05386b", cursor="hand2", font=("yu gothic ui bold", 15), command=lambda: show_frame(complaints_frame), borderwidth=0, highlightthickness=0, activebackground="white", activeforeground="#05386b")
    new_complaints_button1.place(x=header1.winfo_screenwidth()*0.01, y=header1.winfo_screenheight()*0.055)

    schedule_report_button1=Button(header1, text="Schedule Report", bg="white", fg="#05386b", cursor="hand2", font=("yu gothic ui bold", 15), borderwidth=0, highlightthickness=0, activebackground="#5cdb95", activeforeground="#05386b")
    schedule_report_button1.place(x=header1.winfo_screenwidth()*0.12, y=header1.winfo_screenheight()*0.055)

    centre1=Listbox(schedule_report_frame, bg="white", width=schedule_report_frame.winfo_screenwidth(), height=int(schedule_report_frame.winfo_screenheight()), borderwidth=0, highlightthickness=0)
    centre1.place(x=0,y=schedule_report_frame.winfo_screenheight()*0.1)

    box1=Frame(centre1, bg="#05386B", borderwidth=0, highlightthickness=0, width=int(schedule_report_frame.winfo_screenwidth()*0.7), height=int(schedule_report_frame.winfo_screenheight()*0.7))
    box1.place(x=schedule_report_frame.winfo_screenwidth()*0.15, y=schedule_report_frame.winfo_screenheight()*0.1)

    status_canvas = Canvas(box1, width=int(box1.winfo_screenwidth()*0.697), height=int(box1.winfo_screenheight()*0.697), bg="#05386b")
    status_canvas.place(x=0, y=0)

    problems = []

    def change_status(row):
        nonlocal display_df
        if(display_df['Status'][row]=="In Progress"): display_df.at[row, 'Status'] = "Completed"
        elif(display_df['Status'][row]=="Completed"): display_df.at[row, 'Status'] = "In Progress"
        problems[row].config(text=display_df['Problem'][row] + " at " + display_df['Street'][row] + " | " + display_df['Reporting Date'][row] + " | Status: " + display_df['Status'][row])

        
    y = 0
    row_count=len(display_df.index)
    for row in range(row_count):

        if row%2==0:
            problems.append(Label(status_canvas, text=display_df['Problem'][row] + " at " + display_df['Street'][row] + " | " + display_df['Reporting Date'][row] + " | Status: " + display_df['Status'][row], bg="#05386b", fg="white", font=("yu gothic ui", 15)))
        else:
            problems.append(Label(status_canvas, text=display_df['Problem'][row] + " at " + display_df['Street'][row] + " | " + display_df['Reporting Date'][row] + " | Status: " + display_df['Status'][row], bg="#05386b", fg="white", font=("yu gothic ui", 15)))
        status_canvas.create_window(25, y+10, window=problems[row], anchor=NW)
        status_button=Button(status_canvas, text="Change Status", bg="#05386b", fg="white", command=partial(change_status, row), activebackground="#05386b", activeforeground="#5cdb95", font=("yu gothic ui", 15))
        status_canvas.create_window(675, y+2.5, window=status_button, anchor=NW)
        line_separator=Frame(status_canvas, width=int(status_canvas.winfo_screenheight()*1.5), height=2, bg="white")
        status_canvas.create_window(0, y+56, window=line_separator, anchor=NW)
        y += 60

    scrollbar = Scrollbar(status_canvas, orient=VERTICAL, command=status_canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
    status_canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))

    header2=Listbox(complaints_frame, bg="#5cdb95", width=complaints_frame.winfo_screenwidth(), height=int(complaints_frame.winfo_screenheight()*0.01), borderwidth=0, highlightthickness=0)
    header2.place(x=0,y=0)

    title2=Label(header2, text="SUPERVISOR", bg="#5cdb95", fg="#05386b", font=("yu gothic ui bold", 30))
    title2.place(x=header2.winfo_screenwidth()*0.4, y=header2.winfo_screenheight()*0.01)

    logout_button2=Button(header2, text="Logout  ", image=logout_pic, bg="#5cdb95", fg="#05386b", font=("yu gothic ui", 15), borderwidth=0, highlightthickness=0, activebackground="#5cdb95", activeforeground="#05386b", cursor="hand2", compound="right", command=exit)
    logout_button2.image=logout_pic
    logout_button2.place(x=header2.winfo_screenwidth()*0.9, y=header2.winfo_screenheight()*0.01)

    new_complaints_button2=Button(header2, text="New Complaints", bg="white", fg="#05386b", cursor="hand2", font=("yu gothic ui bold", 15), borderwidth=0, highlightthickness=0, activebackground="#5cdb95", activeforeground="#05386b")
    new_complaints_button2.place(x=header2.winfo_screenwidth()*0.01, y=header2.winfo_screenheight()*0.055)

    schedule_report_button2=Button(header2, text="Schedule Report", bg="#5cdb95", fg="#05386b", cursor="hand2", font=("yu gothic ui bold", 15), command= lambda: show_frame(schedule_report_frame), borderwidth=0, highlightthickness=0, activebackground="white", activeforeground="#05386b")
    schedule_report_button2.place(x=header2.winfo_screenwidth()*0.12, y=header2.winfo_screenheight()*0.055)    

    centre2=Listbox(complaints_frame, bg="white", width=complaints_frame.winfo_screenwidth(), height=int(complaints_frame.winfo_screenheight()), borderwidth=0, highlightthickness=0)
    centre2.place(x=0,y=complaints_frame.winfo_screenheight()*0.1)

    side_bar1=Frame(centre2, bg="#5cdb95", height=window.winfo_screenheight(), width=int(window.winfo_screenwidth()*0.3), highlightthickness=0, borderwidth=0)
    side_bar1.place(x=0,y=centre2.winfo_screenheight()*0.01)

    fill_form=[]

    def show_form(complaint_no):
        nonlocal current_complaint_no, fill_form
        fill_form[current_complaint_no].config(bg="#5cdb95")
        current_complaint_no=complaint_no
        # show_frame(complaints_frame)
        complaint_no_label.config(text="Complaint No. XYZ123", fg="#5cdb95")
        locality_label.config(text=locality)
        street_label.config(text=new_complaints_df['Street'][complaint_no])
        problem_label.config(text=new_complaints_df['Problem'][complaint_no])
        reporting_date_label.config(text=new_complaints_df['Reporting Date'][complaint_no])
        severity_menu.config(state='normal')
        traffic_menu.config(state='normal')
        resource_type_menu.config(state='normal')
        resource_name_menu.config(state='normal')
        submit_button.config(state='normal')
        nonlocal temp_dict
        temp_dict={'Locality': locality, 'Street': new_complaints_df['Street'][complaint_no], 'Problem': new_complaints_df['Problem'][complaint_no], 'Reporting Date': new_complaints_df['Reporting Date'][complaint_no], 'Severity': "Mild", 'Traffic': "Extreme", 'Asphalt': 0, 'Bitumen': 0, 'Concrete': 0, 'Bulldozer': 0, 'Road Roller': 0, 'Concrete Mixer': 0, 'Jackhammer': 0, 'Engineer': 0, 'Worker': 0, 'Machine Operator': 0, 'Status': "Pending", 'Completion Date': ""}
        fill_form[complaint_no].config(bg="white")

    def reload_sidebar():
        nonlocal new_complaints_df
        no_of_complaints=len(new_complaints_df.index)
        if(no_of_complaints>0):
            new_complaints_canvas = Canvas(side_bar1, width=int(side_bar1.winfo_screenwidth()*0.298), height=int(side_bar1.winfo_screenheight()*0.86), bg="#5cdb95")
            new_complaints_canvas.place(x=0, y=0)
            nonlocal fill_form
            fill_form=[]
            y = 0
            for i in range(no_of_complaints):
                # problem = Label(new_complaints_canvas, text=new_complaints_df['Problem'][i]+" at "+new_complaints_df['Street'][i], bg="yellow", fg="red")
                # new_complaints_canvas.create_window(0, y, window=problem, anchor=NW)
                fill_form.append(Button(new_complaints_canvas, text=new_complaints_df['Problem'][i]+" at "+new_complaints_df['Street'][i], bg="#5cdb95", fg="black", activebackground="black", activeforeground="white", borderwidth=0, highlightthickness=0, font=("yu gothic ui", 15), width=int(side_bar1.winfo_screenwidth()*0.025), anchor=W, command=partial(show_form, i)))
                new_complaints_canvas.create_window(0, y, window=fill_form[i], anchor=NW)
                y += 40

            scrollbar = Scrollbar(new_complaints_canvas, orient=VERTICAL, command=new_complaints_canvas.yview)
            scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
            new_complaints_canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))
        else:
            no_more_label=Label(side_bar1, text="No More Complaints Remaining.", bg="#5cdb95", fg="#05386b", font=("yu gothic ui", 20))
            no_more_label.place(x=side_bar1.winfo_screenwidth()*0.015,y=side_bar1.winfo_screenheight()*0.4)
        show_frame(complaints_frame)

    form_box=Listbox(centre2, bg="#05386B", width=int(window.winfo_screenwidth()*0.08), height=int(window.winfo_screenheight()*0.04), highlightthickness=2, borderwidth=0, highlightbackground="#05386B", highlightcolor="#05386B")
    form_box.place(x=centre2.winfo_screenwidth()*0.41, y=centre2.winfo_screenheight()*0.1)

    complaint_no_label=Label(form_box, text="Select a Complaint.", bg="#05386b", fg="red", font=("yu gothic ui bold", 20))
    complaint_no_label.place(x=form_box.winfo_screenwidth()*0.14, y=form_box.winfo_screenheight()*0.01)

    locality_title=Label(form_box, text="Locality:", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 17))
    locality_title.place(x=form_box.winfo_screenwidth()*0.03, y=form_box.winfo_screenheight()*0.075)
    locality_label=Label(form_box, text="", bg="#05386b", fg="white", font=("yu gothic ui", 17))
    locality_label.place(x=form_box.winfo_screenwidth()*0.1, y=form_box.winfo_screenheight()*0.075)

    street_title=Label(form_box, text="Street:", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 17))
    street_title.place(x=form_box.winfo_screenwidth()*0.27, y=form_box.winfo_screenheight()*0.075)
    street_label=Label(form_box, text="", bg="#05386b", fg="white", font=("yu gothic ui", 17))
    street_label.place(x=form_box.winfo_screenwidth()*0.335, y=form_box.winfo_screenheight()*0.075)

    problem_title=Label(form_box, text="Problem: ", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 17))
    problem_title.place(x=form_box.winfo_screenwidth()*0.03, y=form_box.winfo_screenheight()*0.175)
    problem_label=Label(form_box, text="", bg="#05386b", fg="white", font=("yu gothic ui", 17))
    problem_label.place(x=form_box.winfo_screenwidth()*0.1, y=form_box.winfo_screenheight()*0.175)

    reporting_date_text=Label(form_box, text="Reporting\nDate: ", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 15))
    reporting_date_text.place(x=form_box.winfo_screenwidth()*0.27, y=form_box.winfo_screenheight()*0.16)
    reporting_date_label=Label(form_box, text="", bg="#05386b", fg="white", font=("yu gothic ui", 15))
    reporting_date_label.place(x=form_box.winfo_screenwidth()*0.34, y=form_box.winfo_screenheight()*0.175)

    severity_options=["Mild","Moderate","Severe","Critical"]
    severity_selection=StringVar()
    severity_selection.set(severity_options[0])
    severity_title=Label(form_box, text="Severity: ", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 17))
    severity_title.place(x=form_box.winfo_screenwidth()*0.03, y=form_box.winfo_screenheight()*0.275)
    severity_menu=OptionMenu(form_box, severity_selection, *severity_options)
    severity_menu.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white", state='disabled')
    smenu=form_box.nametowidget(severity_menu.menuname)
    smenu.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
    severity_menu.place(x=form_box.winfo_screenwidth()*0.1, y=form_box.winfo_screenheight()*0.285, width=int(form_box.winfo_screenwidth()*0.1), height=35)


    traffic_options=["Extreme","Heavy","Medium","Light","Deserted"]
    traffic_selection=StringVar()
    traffic_selection.set(traffic_options[0])
    traffic_title=Label(form_box, text="Traffic\nLevel: ", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 15))
    traffic_title.place(x=form_box.winfo_screenwidth()*0.27, y=form_box.winfo_screenheight()*0.275)
    traffic_menu=OptionMenu(form_box, traffic_selection, *traffic_options)
    traffic_menu.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white", state='disabled')
    tmenu1=form_box.nametowidget(traffic_menu.menuname)
    tmenu1.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
    traffic_menu.place(x=form_box.winfo_screenwidth()*0.335, y=form_box.winfo_screenheight()*0.285, width=int(form_box.winfo_screenwidth()*0.1), height=35)  

    partition_frame=Frame(form_box, bg="white", width=int(form_box.winfo_screenwidth()*0.0015), height=int(form_box.winfo_screenheight()*0.3))
    partition_frame.place(x=form_box.winfo_screenwidth()*0.245, y=form_box.winfo_screenheight()*0.075)

    resource_req_title=Label(form_box, text="Resource Requirement: ", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 17))
    resource_req_title.place(x=form_box.winfo_screenwidth()*0.03, y=form_box.winfo_screenheight()*0.375)

    resource_name_list={
                "Raw Materials": ["Asphalt", "Bitumen", "Concrete"],
                "Machines": ["Bulldozer", "Road Roller", "Concrete Mixer", "Jackhammer"],
                "Personnel": ["Engineer", "Worker", "Machine Operator"]
            }

    def unlock_entry(value):
        resource_name_variable.set(value)
        nonlocal temp_dict
        name=resource_name_variable.get()
        resource_quantity_entry.config(state="normal")
        resource_quantity_variable.set(temp_dict[name])

    def set_resource_names(type):
        menu=resource_name_menu["menu"]
        menu.delete(0,"end")
        for string in resource_name_list[type]:
            # menu.add_command(label=string, command=lambda value=string: resource_name_variable.set(value))
            menu.add_command(label=string, command=partial(unlock_entry, string))
        resource_name_variable.set("[select]")
        resource_quantity_variable.set(0)
        resource_quantity_entry.config(state="disabled")

    resource_type_title=Label(form_box, text="Resource Type: ", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 15))
    resource_type_title.place(x=form_box.winfo_screenwidth()*0.03, y=form_box.winfo_screenheight()*0.43)
    resource_type_options=["Raw Materials", "Personnel", "Machines"]
    resource_type_variable = StringVar()
    resource_type_variable.set("[select]")
    resource_type_menu = OptionMenu(form_box, resource_type_variable, *resource_type_options, command=set_resource_names)
    resource_type_menu.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white", state='disabled')
    rtmenu=form_box.nametowidget(resource_type_menu.menuname)
    rtmenu.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
    resource_type_menu.place(x=form_box.winfo_screenwidth()*0.03, y=form_box.winfo_screenheight()*0.48, width=int(form_box.winfo_screenwidth()*0.125), height=35)

    resource_name_title=Label(form_box, text="Resource Name: ", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 15))
    resource_name_title.place(x=form_box.winfo_screenwidth()*0.17, y=form_box.winfo_screenheight()*0.43)


    resource_quantity_variable=StringVar()
    resource_quantity_variable.set("0")
    resource_quantity_entry=Entry(form_box, fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), highlightthickness=2, width=int(form_box.winfo_screenwidth()*0.01), highlightcolor="white", textvariable=resource_quantity_variable)
    resource_quantity_entry.place(x=form_box.winfo_screenwidth()*0.31, y=form_box.winfo_screenheight()*0.48)
    resource_quantity_entry.config(state="disabled")


    resource_name_variable = StringVar()
    resource_name_variable.set("[select]")
    resource_name_menu = OptionMenu(form_box, resource_name_variable, "[select]", command=unlock_entry)
    resource_name_menu.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white", state='disabled')
    rnmenu=form_box.nametowidget(resource_name_menu.menuname)
    rnmenu.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
    resource_name_menu.place(x=form_box.winfo_screenwidth()*0.17, y=form_box.winfo_screenheight()*0.48, width=int(form_box.winfo_screenwidth()*0.125), height=35)

    resource_quantity_title=Label(form_box, text="Req. Quantity: ", bg="#05386b", fg="#5cdb95", font=("yu gothic ui bold", 15))
    resource_quantity_title.place(x=form_box.winfo_screenwidth()*0.31, y=form_box.winfo_screenheight()*0.43)

            
    def set_quantity():
        nonlocal temp_dict
        name=resource_name_variable.get()
        temp_dict[name]=resource_quantity_variable.get()

    resource_quantity_button=Button(form_box, text="Set", bg="white", fg="#05386b", borderwidth=0, highlightthickness=0, activebackground="white", activeforeground="#05386b", font=("yu gothic ui", 12), width=int(form_box.winfo_screenwidth()*0.004), command=set_quantity)
    resource_quantity_button.place(x=form_box.winfo_screenwidth()*0.42, y=form_box.winfo_screenheight()*0.48)
    
    def submit():
        nonlocal complaints_df, new_complaints_df, current_complaint_no, temp_dict
        temp_dict_list=[temp_dict]
        temp_df=pd.DataFrame(temp_dict_list)
        complaints_df = pd.concat([complaints_df, temp_df], ignore_index=True)
        new_complaints_df.drop(current_complaint_no, inplace=True)
        new_complaints_df.reset_index(drop=True, inplace=True)
        severity_selection.set("[select]")
        traffic_selection.set("[select]")
        resource_name_variable.set("[select]")
        resource_type_variable.set("[select]")
        reload_sidebar()

    submit_button=Button(form_box, text="Submit", bg="white", fg="#05386B", font=("yu gothic ui bold", 17), cursor="hand2", activebackground="white", activeforeground="#05386B", borderwidth=0, width=int(form_box.winfo_screenwidth()*0.007), command=submit, state='disabled')
    submit_button.place(x=form_box.winfo_screenwidth()*0.19, y=form_box.winfo_screenheight()*0.55)

    show_frame(complaints_frame)
    reload_sidebar()