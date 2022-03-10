from tkinter import *
import tkinter
from baseIntialization import UiFields
import sys
from tkinter import messagebox

y = UiFields()











window = tkinter.Tk()
# window.attributes('-fullscreen', True)
window.geometry('500x500')
window.configure(bg=y.background_color)
window.title("Find Bill")

def exit_(event):
    if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
        window.withdraw()
        sys.exit() 
    
window.bind('<Escape>', exit_)

y.billing_ph_no_label=Label(window, text='Billing Date:', font=('times new rommon',11),bg=y.bg_color)
y.billing_ph_no_label.grid(row=1,column=0)
y.billing_ph_no=Entry(window,width=20,font='arial 11',bd=2,justify=CENTER)
y.billing_ph_no.grid(row=1,column=1)
y.billing_ph_no.focus()

y.billing_date_label=Label(window, text='Billing Date:', font=('times new rommon',11),bg=y.bg_color)
y.billing_date_label.grid(row=1,column=2)
y.billing_date=Entry(window,width=20,font='arial 11',bd=2,justify=CENTER)
y.billing_date.grid(row=1,column=3)

y.billing_no_label=Label(window, text='Billing Date:', font=('times new rommon',11),bg=y.bg_color)
y.billing_no_label.grid(row=1,column=4)
y.billing_no=Entry(window,width=20,font='arial 11',bd=2,justify=CENTER)
y.billing_no.grid(row=1,column=5)



window.mainloop()
