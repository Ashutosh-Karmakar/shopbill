from tkinter import *
from  tkinter import ttk

from tkinter import font
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from tkinter import *
from tkinter import messagebox
import openpyxl
import tempfile
import os
import sys
from openpyxl.styles import PatternFill,Border, Side, Alignment, Protection, Font,fills
window = tkinter.Tk()
  
import datetime
daten = datetime.datetime.now()



# setting attribute
window.attributes('-fullscreen', True)
window.configure(bg='#FFE6BC')

window.title("Giridhari Jewellery")
def enter(event):
    print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

def exit_(event):
    if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
        window.withdraw()
        sys.exit() 
 

 

window.bind('<Return>', enter)
window.bind('<Escape>', exit_)

bg_color = "#FFE6BC"

# creating text label to display on window screen
# ==================================================================================

Name=Label(window, text='Name and Address:', font=('times new rommon',10),bg=bg_color)
Name.grid(row=1,column=0,padx=10,pady=5)
Name_txt=Entry(window,width=30,font='arial 10',bd=2,justify=LEFT)
Name_txt.grid(row=1,column=1,pady=15)

mobile=Label(window, text='Mobile No.:', font=('times new rommon',10),bg=bg_color)
mobile.grid(row=1,column=4,padx=10,pady=5)
mobile_txt=Entry(window,width=20,font='arial 10',bd=2,justify=CENTER)
mobile_txt.grid(row=1,column=5,pady=15)

addhar=Label(window, text='Addhar No.:', font=('times new rommon',10),bg=bg_color)
addhar.grid(row=1,column=9,padx=20)
addhar_txt=Entry(window,width=25,font='arial 10',bd=2,justify=CENTER)
addhar_txt.grid(row=1,column=10)

bill=Label(window, text='Bill No.:', font=('times new rommon',10),bg=bg_color)
bill.grid(row=1,column=14,padx=10,pady=5)
bill_txt=Entry(window,width=15,font='arial 10',bd=2,justify=CENTER)
bill_txt.grid(row=1,column=15,pady=15)

date_label=Label(window, text=daten.strftime("%d-%b-%y - (%A)"), font=('times new rommon',10),bg=bg_color)
date_label.grid(row=1,column=20,padx=50,pady=5)


# ===========================================================================================================

F2 = LabelFrame(window,bg= "#FFE6BC")
F2.place(x=5, y=80,width=1355,height=425)

siLabel = Label(F2,text="Sino.",font=('times new rommon',10),bg=bg_color)
siLabel.grid(column=0,row=0)
si_txt = []
for i in range(1,11):
    txt=Entry(F2,width=3,font='arial 12',bd=1,justify=CENTER)
    txt.grid(row=i,column=0,padx=0,pady=5)
    si_txt.append(txt)

desLabel = Label(F2,text="Description",font=('times new rommon',10),bg=bg_color)
desLabel.grid(column=1,row=0)
des_txt = []
for i in range(1,11):
    txt=Entry(F2,width=70,font='arial 12',bd=1,justify=CENTER)
    txt.grid(row=i,column=1,padx=5,pady=5)
    des_txt.append(txt)

wtLabel = Label(F2,text="Weight",font=('times new rommon',10),bg=bg_color)
wtLabel.grid(column=2,row=0)
wt_txt = []
for i in range(1,11):
    txt=Entry(F2,width=9,font='arial 12',bd=1,justify=CENTER)
    txt.grid(row=i,column=2,padx=5,pady=5)
    wt_txt.append(txt)

unitLabel = Label(F2,text="Unit Price",font=('times new rommon',10),bg=bg_color)
unitLabel.grid(column=3,row=0)
unitLabel_txt = []
for i in range(1,11):
    txt=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER)
    txt.grid(row=i,column=3,padx=5,pady=5)
    unitLabel_txt.append(txt)

cgstLabel = Label(F2,text="CGST(1.5%)",font=('times new rommon',10),bg=bg_color)
cgstLabel.grid(column=4,row=0)
cgstLabel_txt = []
for i in range(1,11):
    txt=Entry(F2,width=10,font='arial 12',bd=1,justify=CENTER)
    txt.grid(row=i,column=4,padx=5,pady=5)
    cgstLabel_txt.append(txt)

sgstLabel = Label(F2,text="SGST(1.5%)",font=('times new rommon',10),bg=bg_color)
sgstLabel.grid(column=5,row=0)
sgstLabel_txt = []
for i in range(1,11):
    txt=Entry(F2,width=10,font='arial 15',bd=1,justify=CENTER)
    txt.grid(row=i,column=5,padx=5,pady=5)
    sgstLabel_txt.append(txt)

window.mainloop()