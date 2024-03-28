from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
import pandas as pd
from functools import partial

def mayor_page(window,Database,locality_options):
    logout_img=Image.open('Images/logout1.png')
    logout_pic=ImageTk.PhotoImage(logout_img)

    mayor_frame=Frame(window)
    mayor_frame.grid(row=0, column=0, sticky='nsew')

    header1=Listbox(mayor_frame, bg="#5cdb95", width=mayor_frame.winfo_screenwidth(), height=int(mayor_frame.winfo_screenheight()*0.01), borderwidth=0, highlightthickness=0)
    header1.place(x=0,y=0)

    title1=Label(header1, text="MAYOR", bg="#5cdb95", fg="#05386b", font=("yu gothic ui bold", 30))
    title1.place(x=header1.winfo_screenwidth()*0.4, y=header1.winfo_screenheight()*0.01)

    centre1=Listbox(mayor_frame, bg="white", width=mayor_frame.winfo_screenwidth(), height=int(mayor_frame.winfo_screenheight()), borderwidth=0, highlightthickness=0)
    centre1.place(x=0,y=mayor_frame.winfo_screenheight()*0.1)

    box1=Frame(centre1, bg="#05386B", borderwidth=0, highlightthickness=0, width=int(mayor_frame.winfo_screenwidth()*0.7), height=int(mayor_frame.winfo_screenheight()*0.7))
    box1.place(x=mayor_frame.winfo_screenwidth()*0.15, y=mayor_frame.winfo_screenheight()*0.1)

    report1=Frame(box1, bg="#05386b", width=box1.winfo_screenwidth(), height=int(box1.winfo_screenheight()*0.23), borderwidth=0, highlightthickness=0)
    report1.place(x=0,y=0)

    stat101=Label(report1, bg="#05386b", fg="white", text="No. of Repairs carried out from ", font=("yu gothic ui", 15))
    stat101.place(x=report1.winfo_screenwidth()*0.05, y=report1.winfo_screenheight()*0.05)

    def date1Active():
        stat103.config(text="(Dates in DD-MM-YYYY format)")
    def date1Inactive():
        stat103.config(text="")

    from_date1=Entry(report1, fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), highlightthickness=2, width=int(report1.winfo_screenwidth()*0.01), highlightcolor="white")
    from_date1.place(x=report1.winfo_screenwidth()*0.245, y=report1.winfo_screenheight()*0.051)

    from_date1.bind('<Enter>', lambda event: date1Active())
    from_date1.bind('<Leave>', lambda event: date1Inactive())

    stat102=Label(report1, bg="#05386b", fg="white", text=" to ", font=("yu gothic ui", 15))
    stat102.place(x=report1.winfo_screenwidth()*0.34, y=report1.winfo_screenheight()*0.05)

    to_date1=Entry(report1, fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), highlightthickness=2, width=int(report1.winfo_screenwidth()*0.01), highlightcolor="white")
    to_date1.place(x=report1.winfo_screenwidth()*0.365, y=report1.winfo_screenheight()*0.051)

    to_date1.bind('<Enter>', lambda event: date1Active())
    to_date1.bind('<Leave>', lambda event: date1Inactive())

    stat103=Label(report1, bg="#05386b", fg="white", text="", font=("yu gothic ui", 15))
    stat103.place(x=report1.winfo_screenwidth()*0.46, y=report1.winfo_screenheight()*0.05)

    stat104=Label(report1, bg="#05386b", fg="white", text="Locality: ", font=("yu gothic ui", 15))
    stat104.place(x=report1.winfo_screenwidth()*0.05, y=report1.winfo_screenheight()*0.125)

    locality_variable1 = StringVar()
    locality_variable1.set("All")
    locality_menu1 = OptionMenu(report1, locality_variable1, "All", *locality_options)
    locality_menu1.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white")
    lmenu1=report1.nametowidget(locality_menu1.menuname)
    lmenu1.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
    locality_menu1.place(x=report1.winfo_screenwidth()*0.115, y=report1.winfo_screenheight()*0.125, width=int(report1.winfo_screenwidth()*0.1), height=35)

    stat105=Label(report1, bg="#05386b", fg="white", text="Problem: ", font=("yu gothic ui", 15))
    stat105.place(x=report1.winfo_screenwidth()*0.25, y=report1.winfo_screenheight()*0.125)    

    problem_options=["Potholes", "Broken Footpath", "Cracking", "Waterlogging", "Ravelling", "Road rutting", "Uneven road"]
    problem_variable1 = StringVar()
    problem_variable1.set("Any")
    problem_menu1 = OptionMenu(report1, problem_variable1, "Any", *problem_options)
    problem_menu1.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white")
    pmenu1=report1.nametowidget(problem_menu1.menuname)
    pmenu1.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
    problem_menu1.place(x=report1.winfo_screenwidth()*0.325, y=report1.winfo_screenheight()*0.125, width=int(report1.winfo_screenwidth()*0.12), height=35)

    stat106=Label(report1, bg="#05386b", fg="#5cdb95", text="Result1", font=("yu gothic ui bold", 20))
    stat106.place(x=report1.winfo_screenwidth()*0.5, y=report1.winfo_screenheight()*0.125)   

    report2=Frame(box1, bg="#05386b", width=box1.winfo_screenwidth(), height=int(box1.winfo_screenheight()*0.23), borderwidth=0, highlightthickness=0)
    report2.place(x=0,y=box1.winfo_screenheight()*0.23)

    stat201=Label(report2, bg="#05386b", fg="white", text="No. of Resources utilised from ", font=("yu gothic ui", 15))
    stat201.place(x=report2.winfo_screenwidth()*0.05, y=report2.winfo_screenheight()*0.05)

    def date2Active():
        stat203.config(text="(Dates in DD-MM-YYYY format)")
    def date2Inactive():
        stat203.config(text="")

    from_date2=Entry(report2, fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), highlightthickness=2, width=int(report1.winfo_screenwidth()*0.01), highlightcolor="white")
    from_date2.place(x=report2.winfo_screenwidth()*0.245, y=report2.winfo_screenheight()*0.051)

    from_date2.bind('<Enter>', lambda event: date2Active())
    from_date2.bind('<Leave>', lambda event: date2Inactive())

    stat202=Label(report2, bg="#05386b", fg="white", text=" to ", font=("yu gothic ui", 15))
    stat202.place(x=report2.winfo_screenwidth()*0.34, y=report2.winfo_screenheight()*0.05)

    to_date2=Entry(report2, fg="white", bg="#05386B", font=("yu gothic ui semibold", 12), highlightthickness=2, width=int(report1.winfo_screenwidth()*0.01), highlightcolor="white")
    to_date2.place(x=report2.winfo_screenwidth()*0.365, y=report2.winfo_screenheight()*0.051)

    to_date2.bind('<Enter>', lambda event: date2Active())
    to_date2.bind('<Leave>', lambda event: date2Inactive())

    stat203=Label(report2, bg="#05386b", fg="white", text="", font=("yu gothic ui", 15))
    stat203.place(x=report2.winfo_screenwidth()*0.46, y=report2.winfo_screenheight()*0.05)

    name_list={
        "All": ["All"],
        "Raw Materials": ["Asphalt", "Bitumen", "Concrete"],
        "Machines": ["Bulldozer", "Road Roller", "Concrete Mixer", "Jackhammer"],
        "Personnel": ["Engineer", "Worker", "Machine Operator"]
    }
    def set_resource_names(type):
        menu = resource_name_menu1["menu"]
        menu.delete(0,"end")
        for string in name_list[type]:
            menu.add_command(label=string, command=lambda value=string: resource_name_variable1.set(value))
        resource_name_variable1.set("[select]")

    stat204=Label(report2, bg="#05386b", fg="white", text="Resource Type: ", font=("yu gothic ui", 15))
    stat204.place(x=report2.winfo_screenwidth()*0.05, y=report2.winfo_screenheight()*0.125)

    resource_type_options=["All", "Raw Materials", "Personnel", "Machines"]
    resource_type_variable1 = StringVar()
    resource_type_variable1.set("[select]")
    resource_type_menu1 = OptionMenu(report2, resource_type_variable1, *resource_type_options, command=set_resource_names)
    resource_type_menu1.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white")
    rtmenu1=report2.nametowidget(resource_type_menu1.menuname)
    rtmenu1.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
    resource_type_menu1.place(x=report2.winfo_screenwidth()*0.15, y=report2.winfo_screenheight()*0.125, width=int(report2.winfo_screenwidth()*0.1), height=35)

    stat205=Label(report2, bg="#05386b", fg="white", text="Resource Name: ", font=("yu gothic ui", 15))
    stat205.place(x=report2.winfo_screenwidth()*0.25, y=report2.winfo_screenheight()*0.125)    

    resource_name_variable1 = StringVar()
    resource_name_variable1.set("[select]")
    resource_name_menu1 = OptionMenu(report2, resource_name_variable1, "[select]")
    resource_name_menu1.config(highlightbackground="#05386B", highlightcolor="white", font=("yu gothic ui semibold", 12), fg="white", bg='#05386B', activebackground="#05386B", activeforeground="white")
    rnmenu1=report2.nametowidget(resource_name_menu1.menuname)
    rnmenu1.config(bg='#05386B', font=("yu gothic ui semibold", 12), fg="white", activebackground="black", activeforeground="white")
    resource_name_menu1.place(x=report2.winfo_screenwidth()*0.35, y=report2.winfo_screenheight()*0.125, width=int(report2.winfo_screenwidth()*0.12), height=35)

    stat205=Label(report2, bg="#05386b", fg="#5cdb95", text="Result2", font=("yu gothic ui bold", 20))
    stat205.place(x=report2.winfo_screenwidth()*0.5, y=report2.winfo_screenheight()*0.125)   


    report3=Frame(box1, bg="#05386b", width=box1.winfo_screenwidth(), height=int(box1.winfo_screenheight()*0.23), borderwidth=0, highlightthickness=0)
    report3.place(x=0,y=box1.winfo_screenheight()*0.46)

    stat301=Label(report3, bg="#05386b", fg="white", text="No. of currently outstanding Repairs: ", font=("yu gothic ui", 15))
    stat301.place(x=report3.winfo_screenwidth()*0.05, y=report3.winfo_screenheight()*0.05)

    stat302=Label(report3, bg="#05386b", fg="white", text="Pending: ", font=("yu gothic ui", 15))
    stat302.place(x=report3.winfo_screenwidth()*0.05, y=report3.winfo_screenheight()*0.125)

    stat303=Label(report3, bg="#05386b", fg="#5cdb95", text="Result3.1 ", font=("yu gothic ui bold", 20))
    stat303.place(x=report3.winfo_screenwidth()*0.15, y=report3.winfo_screenheight()*0.125)

    stat304=Label(report3, bg="#05386b", fg="white", text="In Progress: ", font=("yu gothic ui", 15))
    stat304.place(x=report3.winfo_screenwidth()*0.3, y=report3.winfo_screenheight()*0.125)    

    stat305=Label(report3, bg="#05386b", fg="#5cdb95", text="Result3.2 ", font=("yu gothic ui bold", 20))
    stat305.place(x=report3.winfo_screenwidth()*0.4, y=report3.winfo_screenheight()*0.125)

    def exit():
        mayor_frame.destroy()

    logout_button1=Button(header1, text="Log Out  ", image=logout_pic, bg="#5cdb95", fg="#05386b", font=("yu gothic ui", 15), borderwidth=0, highlightthickness=0, activebackground="#5cdb95", activeforeground="#05386b", cursor="hand2", compound="right", command=exit)
    logout_button1.image=logout_pic
    logout_button1.place(x=header1.winfo_screenwidth()*0.9, y=header1.winfo_screenheight()*0.01)