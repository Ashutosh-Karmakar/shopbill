import sys
import tkinter
from tkinter import *
from database import findGst
from baseIntialization import UiFields
u = UiFields()

def monthlyGst():
    window = tkinter.Tk()
    window.geometry('800x100')
    window.configure(bg=u.background_color)
    window.title("Monthly GST")
    def exit_(event):
        if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
            window.withdraw()
            sys.exit() 
        
    window.bind('<Escape>', exit_)
    
    u.gstDateFrom_label = Label(window, text='Billing Date:', font=('times new rommon',11),bg=u.bg_color)
    u.gstDateFrom_label.grid(row=0,column=0,padx=10)

    u.gstDateFrom = Entry(window,width=20,font='arial 11',bd=2,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    u.gstDateFrom.grid(row=0,column=1,padx=10)

    u.gstDateTo_label = Label(window, text='Billing Date:', font=('times new rommon',11),bg=u.bg_color)
    u.gstDateTo_label.grid(row=0,column=2,padx=10)


    u.gstDateTo = Entry(window,width=20,font='arial 11',bd=2,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    u.gstDateTo.grid(row=0,column=3,padx=10)

    u.gstFind = Button(window,text="Find" ,font=('times new rommon',13),command=lambda:findGst(u),bg=u.bg_color,bd=2)
    u.gstFind.grid(column=30,row=0,padx=20,pady=10)
    
    


    window.mainloop()
