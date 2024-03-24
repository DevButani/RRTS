from tkinter import *
import pandas as pd
from functools import partial

"""
    new_complaints_df=df for complaints registered by clerk
    complaints_df=df for pending/in progress complaints 
"""
def supervisor_page(window,Database,locality):
    new_complaints_df=pd.read_csv('https://drive.google.com/uc?id='+Database[2]["new "+locality])

    complaints_df=pd.read_csv('https://drive.google.com/uc?id='+Database[2][locality])

    display_df = complaints_df[(complaints_df['Status']=='In Progress')]
    complaints_df.drop(complaints_df[(complaints_df['Status']=='In Progress')].index, inplace=True)
    display_df.reset_index(inplace=True, drop=True)

    current_complaint_no=0

    loading_frame=Frame(window)
    welcome_frame=Frame(window)
    new_complaints_frame=Frame(window)
    schedule_report_frame=Frame(window)
    complaint_form_frame=Frame(window)
                    
    for frame in (welcome_frame, new_complaints_frame, schedule_report_frame, complaint_form_frame, loading_frame):
        frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(frame):
        frame.tkraise()

    def show_form(complaint_no):
        nonlocal current_complaint_no
        current_complaint_no=complaint_no
        show_frame(complaint_form_frame)
        street_label.config(text=new_complaints_df['Street'][complaint_no])
        problem_label.config(text=new_complaints_df['Problem'][complaint_no])
        reporting_date_label.config(text=new_complaints_df['Reporting Date'][complaint_no])


    #new complaints
    def show_new_complaints():
        # show_frame(loading_frame)
        nonlocal new_complaints_df
        header2=Listbox(new_complaints_frame, bg="red", width=window.winfo_screenwidth(), height=int(window.winfo_screenheight()*0.01))
        header2.place(x=0, y=0)

        title2=Label(header2, text="Supervisor", bg="red", fg="yellow")
        title2.place(x=window.winfo_screenwidth()/2, y=0)

        new_complaints_button2=Button(header2, text="New Complaints", bg="yellow", fg="red", command=show_new_complaints)
        new_complaints_button2.place(x=header2.winfo_screenwidth()/2-100, y=header2.winfo_screenheight()*0.075)

        schedule_report_button2=Button(header2, text="Schedule Report", bg="yellow", fg="red", command= lambda: show_frame(schedule_report_frame))
        schedule_report_button2.place(x=header2.winfo_screenwidth()/2+100, y=header2.winfo_screenheight()*0.075)

        list_frame=Frame(new_complaints_frame, bg="yellow", width=new_complaints_frame.winfo_screenwidth(), height=new_complaints_frame.winfo_screenheight())
        list_frame.place(x=0, y=140)
        no_of_complaints=len(new_complaints_df.index)
        if(no_of_complaints>0):
            new_complaints_canvas = Canvas(list_frame, width=500, bg="yellow")
            new_complaints_canvas.place(x=list_frame.winfo_screenwidth()*0.3, y=list_frame.winfo_screenheight()*0.1)

            y = 0
            for i in range(no_of_complaints):
                problem = Label(new_complaints_canvas, text=new_complaints_df['Problem'][i]+" at "+new_complaints_df['Street'][i], bg="yellow", fg="red")
                new_complaints_canvas.create_window(0, y, window=problem, anchor=NW)
                fill_form=Button(new_complaints_canvas, text="View", bg="red", fg="yellow", command=partial(show_form, i))
                new_complaints_canvas.create_window(150, y, window=fill_form, anchor=NW)
                y += 20

            scrollbar = Scrollbar(new_complaints_canvas, orient=VERTICAL, command=new_complaints_canvas.yview)
            scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
            new_complaints_canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))
        else:
            no_more_label=Label(new_complaints_frame, text="No More Complaints Remaining to be Reviewed.", bg="yellow", fg="red")
            no_more_label.place(x=new_complaints_frame.winfo_screenwidth()*0.4,y=new_complaints_frame.winfo_screenheight()*0.5)
        show_frame(new_complaints_frame)

    #loading
    header0=Listbox(loading_frame, bg="red", width=window.winfo_screenwidth(), height=int(window.winfo_screenheight()*0.01))
    header0.place(x=0, y=0)

    title0=Label(header0, text="Supervisor", bg="red", fg="yellow")
    title0.place(x=window.winfo_screenwidth()/2, y=0)

    new_complaints_button0=Button(header0, text="New Complaints", bg="yellow", fg="red", command= show_new_complaints)
    new_complaints_button0.place(x=header0.winfo_screenwidth()/2-100, y=header0.winfo_screenheight()*0.075)

    schedule_report_button0=Button(header0, text="Schedule Report", bg="yellow", fg="red", command= lambda: show_frame(schedule_report_frame))
    schedule_report_button0.place(x=header0.winfo_screenwidth()/2+100, y=header0.winfo_screenheight()*0.075)

    load_frame=Listbox(loading_frame, bg="yellow", width=loading_frame.winfo_screenwidth(), height=loading_frame.winfo_screenheight())
    load_frame.place(x=0, y=140)


    # form
    header3=Listbox(complaint_form_frame, bg="red", width=window.winfo_screenwidth(), height=int(window.winfo_screenheight()*0.01))
    header3.place(x=0, y=0)

    title3=Label(header3, text="Supervisor", bg="red", fg="yellow")
    title3.place(x=window.winfo_screenwidth()/2, y=0)

    new_complaints_button3=Button(header3, text="New Complaints", bg="yellow", fg="red", command=show_new_complaints)
    new_complaints_button3.place(x=header3.winfo_screenwidth()/2-100, y=header3.winfo_screenheight()*0.075)

    schedule_report_button3=Button(header3, text="Schedule Report", bg="yellow", fg="red", command= lambda: show_frame(schedule_report_frame))
    schedule_report_button3.place(x=header3.winfo_screenwidth()/2+100, y=header3.winfo_screenheight()*0.075)

    form_frame=Listbox(complaint_form_frame, bg="yellow", width=complaint_form_frame.winfo_screenwidth(), height=complaint_form_frame.winfo_screenheight())
    form_frame.place(x=0, y=140)

    locality_title=Label(form_frame, text="Locality: ", bg="yellow", fg="red")
    locality_title.place(x=form_frame.winfo_screenwidth()/2-100, y=10)
    locality_label=Label(form_frame, text=locality, bg="yellow", fg="red")
    locality_label.place(x=form_frame.winfo_screenwidth()/2-100, y=30)

    street_title=Label(form_frame, text="Street: ", bg="yellow", fg="red")
    street_title.place(x=form_frame.winfo_screenwidth()/2+100, y=10)
    street_label=Label(form_frame, text="", bg="yellow", fg="red")
    street_label.place(x=form_frame.winfo_screenwidth()/2+100, y=30)

    problem_title=Label(form_frame, text="Problem: ", bg="yellow", fg="red")
    problem_title.place(x=form_frame.winfo_screenwidth()/2-100, y=60)
    problem_label=Label(form_frame, text="", bg="yellow", fg="red")
    problem_label.place(x=form_frame.winfo_screenwidth()/2-100, y=80)

    reporting_date_text=Label(form_frame, text="Reporting Date: ", bg="yellow", fg="red")
    reporting_date_text.place(x=form_frame.winfo_screenwidth()/2+100, y=60)
    reporting_date_label=Label(form_frame, text="", bg="yellow", fg="red")
    reporting_date_label.place(x=form_frame.winfo_screenwidth()/2+100, y=80)

    severity_options=["Mild","Moderate","Severe","Critical"]
    severity_selection=StringVar()
    severity_title=Label(form_frame, text="Severity: ", bg="yellow", fg="red")
    severity_title.place(x=form_frame.winfo_screenwidth()/2-100, y=110)
    severity_menu=OptionMenu(form_frame, severity_selection, *severity_options)
    severity_menu.place(x=form_frame.winfo_screenwidth()/2-100, y=130)

    traffic_options=["Extreme","Heavy","Medium","Light","Deserted"]
    traffic_selection=StringVar()
    traffic_title=Label(form_frame, text="Traffic Level: ", bg="yellow", fg="red")
    traffic_title.place(x=form_frame.winfo_screenwidth()/2+100, y=110)
    traffic_menu=OptionMenu(form_frame, traffic_selection, *traffic_options)
    traffic_menu.place(x=form_frame.winfo_screenwidth()/2+100, y=130)

    #Raw materials: asphalt, bitumen, concrete
    raw_materials_title=Label(form_frame, text="Raw Materials Required: ", bg="yellow", fg="red")
    raw_materials_title.place(x=form_frame.winfo_screenwidth()/2-100, y=160)

    asphalt_quantity=IntVar()
    asphalt_title=Label(form_frame, text="Asphalt", bg="yellow", fg="red")
    asphalt_title.place(x=form_frame.winfo_screenwidth()/2+100, y=160)
    asphalt_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=asphalt_quantity, bg="yellow", fg="red")
    asphalt_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=180)

    bitumen_quantity=IntVar()
    bitumen_title=Label(form_frame, text="Bitumen", bg="yellow", fg="red")
    bitumen_title.place(x=form_frame.winfo_screenwidth()/2+100, y=210)
    bitumen_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=bitumen_quantity, bg="yellow", fg="red")
    bitumen_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=230)

    concrete_quantity=IntVar()
    concrete_title=Label(form_frame, text="Concrete", bg="yellow", fg="red")
    concrete_title.place(x=form_frame.winfo_screenwidth()/2+100, y=260)
    concrete_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=concrete_quantity, bg="yellow", fg="red")
    concrete_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=280)

    #Machines: Roadroller, bulldozer, concrete mixer, jack hammer

    machines_title=Label(form_frame, text="Machines Required: ", bg="yellow", fg="red")
    machines_title.place(x=form_frame.winfo_screenwidth()/2-100, y=310)

    roller_quantity=IntVar()
    roller_title=Label(form_frame, text="Road Roller", bg="yellow", fg="red")
    roller_title.place(x=form_frame.winfo_screenwidth()/2+100, y=310)
    roller_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=roller_quantity, bg="yellow", fg="red")
    roller_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=330)

    bulldozer_quantity=IntVar()
    bulldozer_title=Label(form_frame, text="Bulldozer", bg="yellow", fg="red")
    bulldozer_title.place(x=form_frame.winfo_screenwidth()/2+100, y=360)
    bulldozer_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=bulldozer_quantity, bg="yellow", fg="red")
    bulldozer_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=380)

    mixer_quantity=IntVar()
    mixer_title=Label(form_frame, text="Mixer", bg="yellow", fg="red")
    mixer_title.place(x=form_frame.winfo_screenwidth()/2+100, y=410)
    mixer_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=mixer_quantity, bg="yellow", fg="red")
    mixer_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=430)

    jackhammer_quantity=IntVar()
    jackhammer_title=Label(form_frame, text="Jackhammer", bg="yellow", fg="red")
    jackhammer_title.place(x=form_frame.winfo_screenwidth()/2+100, y=460)
    jackhammer_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=jackhammer_quantity, bg="yellow", fg="red")
    jackhammer_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=480)

    #personnel: engineer, worker, machine operator

    personnel_title=Label(form_frame, text="Personnel Required: ", bg="yellow", fg="red")
    personnel_title.place(x=form_frame.winfo_screenwidth()/2-100, y=510)

    engineer_quantity=IntVar()
    engineer_title=Label(form_frame, text="Engineer", bg="yellow", fg="red")
    engineer_title.place(x=form_frame.winfo_screenwidth()/2+100, y=540)
    engineer_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=engineer_quantity, bg="yellow", fg="red")
    engineer_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=560)

    worker_quantity=IntVar()
    worker_title=Label(form_frame, text="Worker", bg="yellow", fg="red")
    worker_title.place(x=form_frame.winfo_screenwidth()/2+100, y=590)
    worker_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=worker_quantity, bg="yellow", fg="red")
    worker_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=610)

    operator_quantity=IntVar()
    operator_title=Label(form_frame, text="Operator",  bg="yellow", fg="red")
    operator_title.place(x=form_frame.winfo_screenwidth()/2+100, y=640)
    operator_selection=Spinbox(form_frame, from_=0, to=9999, textvariable=operator_quantity, bg="yellow", fg="red")
    operator_selection.place(x=form_frame.winfo_screenwidth()/2+100, y=660)

    def submit():
        nonlocal complaints_df, new_complaints_df, current_complaint_no
        temp_dict=[{'Locality': locality, 'Street': new_complaints_df['Street'][current_complaint_no], 'Problem': new_complaints_df['Problem'][current_complaint_no], 'Reporting Date': new_complaints_df['Reporting Date'][current_complaint_no], 'Severity': severity_selection.get(), 'Traffic': traffic_selection.get(), 'Asphalt': asphalt_quantity.get(), 'Bitumen': bitumen_quantity.get(), 'Concrete': concrete_quantity.get(), 'Road Roller': roller_quantity.get(), 'Bulldozer': bulldozer_quantity.get(), 'Concrete Mixer': mixer_quantity.get(), 'Jackhammer': jackhammer_quantity.get(), 'Engineer': engineer_quantity.get(), 'Worker': worker_quantity.get(), 'Operator': operator_quantity.get(), 'Status': 'Pending', 'Completion Date': ""}]
        temp_df=pd.DataFrame(temp_dict)
        complaints_df = pd.concat([complaints_df, temp_df], ignore_index=True)
        new_complaints_df.drop(current_complaint_no, inplace=True)
        new_complaints_df.reset_index(drop=True, inplace=True)
        severity_selection.set("")
        traffic_selection.set("")
        asphalt_quantity.set(0)
        bitumen_quantity.set(0)
        concrete_quantity.set(0)
        roller_quantity.set(0)
        bulldozer_quantity.set(0)
        mixer_quantity.set(0)
        jackhammer_quantity.set(0)
        engineer_quantity.set(0)
        worker_quantity.set(0)
        operator_quantity.set(0)
        show_new_complaints()

    submit_button=Button(form_frame, text="Submit", bg="red", fg="yellow", command=submit)
    submit_button.place(x=form_frame.winfo_screenwidth()/2, y=690)



    # welcome frame
    show_frame(welcome_frame)

    header1=Listbox(welcome_frame, bg="red", width=window.winfo_screenwidth(), height=int(window.winfo_screenheight()*0.01))
    header1.place(x=0, y=0)

    title1=Label(header1, text="Supervisor", bg="red", fg="yellow")
    title1.place(x=window.winfo_screenwidth()/2, y=0)

    new_complaints_button1=Button(header1, text="New Complaints", bg="yellow", fg="red", command=show_new_complaints)
    new_complaints_button1.place(x=header1.winfo_screenwidth()/2-100, y=header1.winfo_screenheight()*0.075)

    schedule_report_button1=Button(header1, text="Schedule Report", bg="yellow", fg="red", command= lambda: show_frame(schedule_report_frame))
    schedule_report_button1.place(x=header1.winfo_screenwidth()/2+100, y=header1.winfo_screenheight()*0.075)

    welcome_listbox=Listbox(welcome_frame, bg="yellow", width=welcome_frame.winfo_screenwidth(), height=welcome_frame.winfo_screenheight())
    welcome_listbox.place(x=0, y=140)

    welcome_label=Label(welcome_listbox, text="WELCOME", fg="red", font=("Ariel", 40))
    welcome_label.place(x=welcome_listbox.winfo_screenwidth()*0.4, y=welcome_listbox.winfo_screenheight()/4)

    #schedule report

    header4=Listbox(schedule_report_frame, bg="red", width=window.winfo_screenwidth(), height=int(window.winfo_screenheight()*0.01))
    header4.place(x=0, y=0)

    title4=Label(header4, text="Supervisor", bg="red", fg="yellow")
    title4.place(x=window.winfo_screenwidth()/2, y=0)

    new_complaints_button4=Button(header4, text="New Complaints", bg="yellow", fg="red", command=show_new_complaints)
    new_complaints_button4.place(x=header4.winfo_screenwidth()/2-100, y=header4.winfo_screenheight()*0.075)

    schedule_report_button4=Button(header4, text="Schedule Report", bg="yellow", fg="red", command= lambda: show_frame(schedule_report_frame))
    schedule_report_button4.place(x=header4.winfo_screenwidth()/2+100, y=header4.winfo_screenheight()*0.075)

    schedule_frame=Frame(schedule_report_frame, bg="yellow", width=schedule_report_frame.winfo_screenwidth(), height=schedule_report_frame.winfo_screenheight())
    schedule_frame.place(x=0, y=140)

    status_canvas = Canvas(schedule_frame, width=500, bg="yellow")
    status_canvas.place(x=schedule_frame.winfo_screenwidth()*0.3, y=schedule_frame.winfo_screenheight()*0.1)

    problems = []

    def change_status(row):
        nonlocal display_df
        if(display_df['Status'][row]=="In Progress"): display_df.at[row, 'Status'] = "Completed"
        elif(display_df['Status'][row]=="Completed"): display_df.at[row, 'Status'] = "In Progress"
        problems[row].config(text=display_df['Problem'][row] + " at " + display_df['Street'][row] + " | " + display_df['Reporting Date'][row] + " | Status: " + display_df['Status'][row])
    y = 0
    row_count=len(display_df.index)
    for row in range(row_count):
        problems.append(Label(status_canvas, text=display_df['Problem'][row] + " at " + display_df['Street'][row] + " | " + display_df['Reporting Date'][row] + " | Status: " + display_df['Status'][row], bg="yellow", fg="red"))
        status_canvas.create_window(0, y, window=problems[row], anchor=NW)
        status_button=Button(status_canvas, text="Change Status", bg="red", fg="yellow",command=partial(change_status, row))
        status_canvas.create_window(350, y, window=status_button, anchor=NW)
        y += 20

    scrollbar = Scrollbar(status_canvas, orient=VERTICAL, command=status_canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
    status_canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))
    
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
        loading_frame.destroy()
        welcome_frame.destroy()
        new_complaints_frame.destroy()
        schedule_report_frame.destroy()
        complaint_form_frame.destroy()
    Button(window, text="Log Out", command=exit).place(x=0,y=0)