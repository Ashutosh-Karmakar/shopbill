#desktop Bill
import sys
import tkinter
from datetime import datetime
from tkinter import *
from tkcalendar import Calendar

from database import findGst
from baseIntialization import UiFields
u = UiFields()

def monthlyGst():
    
    window = tkinter.Tk()
    # window.attributes('-fullscreen', True)
    window.geometry('1000x800')
    window.configure(bg=u.background_color)
    window.title("Monthly GST")
    def exit_(event):
        if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
            window.withdraw()
            sys.exit() 
        
    window.bind('<Escape>', exit_)
    
    
     # Add Calendar
    cur_date = datetime.now()

    llFrom = Label(window,text="FROM", font=('times new rommon',14),bg=u.bg_color).grid(row=0,column=0)
    u.gstDateFrom_label = Label(window, text='Billing Date:', font=('times new rommon',11),bg=u.bg_color)
    u.gstDateFrom_label.grid(row=1,column=0)

    
    calfrom = Calendar(window, selectmode = 'day',
                year = cur_date.year, month = cur_date.month,
                day = cur_date.day)
    
    calfrom.grid(row=2,column=0)
    
    u.gstDateFrom = Label(window,text="",font=('times new rommon',11),bg=u.bg_color)
    u.gstDateFrom.grid(row=1,column=1)
    
    llFrom = Label(window,text="TO", font=('times new rommon',14),bg=u.bg_color).grid(row=0,column=3)
    u.gstDateTo_label = Label(window, text='Billing Date:', font=('times new rommon',11),bg=u.bg_color)
    u.gstDateTo_label.grid(row=1,column=3)


    calto = Calendar(window, selectmode = 'day',
                year = cur_date.year, month = cur_date.month,
                day = cur_date.day)
    
    calto.grid(row=2,column=3)
    
    u.gstDateTo = Label(window,text="",font=('times new rommon',11),bg=u.bg_color)
    u.gstDateTo.grid(row=1,column=4)

    u.gstFind = Button(window,text="Find" ,font=('times new rommon',13),command=lambda:findGst(u),bg='red',bd=2)
    u.gstFind.grid(column=1,row=4)
    u.gstFind.grid_forget()
    
    llmsg = Label(window,text="FROM should be less than TO",font=('times new rommon',11),bg=u.bg_color)
    llmsg.grid(column=1,row=4)
    
    
    def grad_date(cal,n):
        datefind = ''
        result = cal.get_date()
        result = result.split('/')
            
        datefind = datefind + '20' + result[2] + '-'
        if(len(result[0]) == 1):
            result[0] = '0'+result[0]
        datefind = datefind + result[0] + '-'
        
        if(len(result[1]) == 1):
            result[1] = '0'+result[1]
        datefind = datefind + result[1]
        
        if(n == 1):
            u.gstDateFrom.config(text = datefind)
            u.cal1 = datetime.strptime(cal.get_date(), '%m/%d/%y')
            print(u.cal1)
        if(n == 2):
            u.gstDateTo.config(text = datefind)
            u.cal2 = datetime.strptime(cal.get_date(), '%m/%d/%y')
            print(u.cal2)
        
        if(u.gstDateFrom["text"] !="" and u.gstDateTo["text"] != ""):
            if(u.cal1 <= u.cal2):
                llmsg.grid_forget()
                u.gstFind.grid(column=1,row=4)
            else:
                u.gstFind.grid_forget()
                llmsg.grid(column=1,row=4)
 
    # Add Button and Label
    Button(window, text = "Get Date",
        command = lambda: grad_date(calfrom,1)).grid(row=3,column=0)
    Button(window, text = "Get Date",
        command =lambda: grad_date(calto,2)).grid(row=3,column=3)
    
    window.mainloop()
    
    
monthlyGst()