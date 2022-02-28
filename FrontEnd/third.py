from cgitb import text
from tkinter import *
from  tkinter import ttk

from tkinter import font
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from tkinter import *
from tkinter import messagebox
import tempfile
import os
import sys
from openpyxl.drawing.image import Image 
window = tkinter.Tk()
  
import datetime
daten = datetime.datetime.now()

from backend import generateBill

# setting attribute
window.attributes('-fullscreen', True)
window.configure(bg='#FFE6BC')

window.title("Giridhari Jewellery")

def exit_(event):
    if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
        window.withdraw()
        sys.exit() 
 

 

window.bind('<Escape>', exit_)

bg_color = "#FFE6BC"

# ==================================creating the gui================================================
labelfont = 11
textfont = 11

mobile=Label(window, text='Mobile No.:', font=('times new rommon',labelfont),bg=bg_color)
mobile.grid(row=1,column=0,padx=10)
mobile_txt=Entry(window,width=20,font='arial '+str(textfont),bd=2,justify=CENTER)
mobile_txt.grid(row=1,column=1,pady=15)

Name=Label(window, text='Name and Address:', font=('times new rommon',labelfont),bg=bg_color)
Name.grid(row=1,column=4,padx=10)
Name_txt=Entry(window,width=30,font='arial '+str(textfont),bd=2,justify=LEFT)
Name_txt.grid(row=1,column=5,pady=15)

address=Label(window, text='Address:', font=('times new rommon',labelfont),bg=bg_color)
address.grid(row=1,column=9)
address_txt=Entry(window,width=25,font='arial '+str(textfont),bd=2,justify=CENTER)
address_txt.grid(row=1,column=10)

addhar=Label(window, text='Addhar No.:', font=('times new rommon',labelfont),bg=bg_color)
addhar.grid(row=1,column=14)
addhar_txt=Entry(window,width=25,font='arial '+str(textfont),bd=2,justify=CENTER)
addhar_txt.grid(row=1,column=15)

bill=Label(window, text='Bill No.:', font=('times new rommon',labelfont),bg=bg_color)
bill.grid(row=1,column=20)
bill_txt=Entry(window,width=15,font='arial '+str(textfont),bd=2,justify=CENTER)
bill_txt.grid(row=1,column=25,pady=15)

date_label=Label(window, text=daten.strftime("%d-%b-%y - (%A)"), font=('times new rommon',labelfont),bg=bg_color)
date_label.grid(row=1,column=30)


# ===========================================================================================================

F2 = LabelFrame(window,bg= "#FFE6BC")
F2.place(x=5, y=80,width=1500,height=370)

siLabel = Label(F2,text="Sino.",font=('times new rommon',10),bg=bg_color)
siLabel.grid(column=0,row=0)
si_txt = []
for i in range(1,10):
    txt=Label(F2,text=i,font=('times new rommon',10),bg=bg_color)
    txt.grid(row=i,column=0,padx=0,pady=5)
    si_txt.append(txt)


desLabel = Label(F2,text="Description",font=('times new rommon',10),bg=bg_color)
desLabel.grid(column=1,row=0)
des_txt = []

pcsLabel = Label(F2,text="Pcs",font=('times new rommon',10),bg=bg_color)
pcsLabel.grid(column=2,row=0)


wtLabel = Label(F2,text="Weight",font=('times new rommon',10),bg=bg_color)
wtLabel.grid(column=3,row=0)
wt_txt = []

unitLabel = Label(F2,text="Unit Price",font=('times new rommon',10),bg=bg_color)
unitLabel.grid(column=4,row=0)
unitLabel_txt = []


mcLabel = Label(F2,text="MC",font=('times new rommon',10),bg=bg_color)
mcLabel.grid(column=5,row=0)
mcLabel_txt = []

cgstLabel = Label(F2,text="CGST(1.5%)",font=('times new rommon',10),bg=bg_color)
cgstLabel.grid(column=6,row=0)
cgstLabel_txt = []

sgstLabel = Label(F2,text="SGST(1.5%)",font=('times new rommon',10),bg=bg_color)
sgstLabel.grid(column=7,row=0)
sgstLabel_txt = []


gstAmtLabel = Label(F2,text="GstAmt",font=('times new rommon',10),bg=bg_color)
gstAmtLabel.grid(column=8,row=0)
gstAmt_txt = []

toLabel = Label(F2,text="Net",font=('times new rommon',10),bg=bg_color)
toLabel.grid(column=9,row=0)
toLabel_txt = []

for i in range(1,10):
    txt1=Entry(F2,width=40,font='arial 12',bd=1,justify=CENTER)
    txt1.grid(row=i,column=1,padx=5,pady=5)
    des_txt.append(txt1)
    
    pcs=Entry(F2,width=3,font='arial 12',bd=1,justify=CENTER)
    pcs.grid(row=i,column=2,padx=5,pady=5)
    pcs.insert(0,1)
 
    txt2=Entry(F2,width=9,font='arial 12',bd=1,justify=CENTER)
    txt2.grid(row=i,column=3,padx=5,pady=5)
    wt_txt.append(txt2)

    txt3=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER)
    txt3.grid(row=i,column=4,padx=5,pady=5)
    unitLabel_txt.append(txt3)
    
    mc=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER)
    mc.grid(row=i,column=5,padx=5,pady=5)
    mcLabel_txt.append(txt3)

    txt4=Entry(F2,width=10,font='arial 12',bd=1,justify=CENTER)
    txt4.grid(row=i,column=6,padx=5,pady=5)
    cgstLabel_txt.append(txt4)

    txt5=Entry(F2,width=10,font='arial 12',bd=1,justify=CENTER)
    txt5.grid(row=i,column=7,padx=5,pady=5)
    sgstLabel_txt.append(txt5)

    gstAmt=Entry(F2,width=10,font='arial 12',bd=1,justify=CENTER)
    gstAmt.grid(row=i,column=8,padx=5,pady=5)
    gstAmt_txt.append(gstAmt)


    txt6=Entry(F2,width=16,font='arial 12',bd=1,justify=CENTER)
    txt6.grid(row=i,column=9,padx=5,pady=5)
    toLabel_txt.append(txt6)




# ======================================================================================================================


F3 = LabelFrame(window,bg= "#FFE6BC")
F3.place(x=5,y=460,width=13055,height=170)

si = Label(F3,text="Si.",font=('times new rommon',10),bg=bg_color)
si.grid(column=0,row=0)

adrdeL = Label(F3,text="Old jewels",font=('times new rommon',10),bg=bg_color)
adrdeL.grid(column=1,row=0)

oldweLabel = Label(F3,text="Weight",font=('times new rommon',10),bg=bg_color)
oldweLabel.grid(column=2,row=0)

oldunitLabel = Label(F3,text="Unit Price",font=('times new rommon',10),bg=bg_color)
oldunitLabel.grid(column=3,row=0)


oldtotalLabel = Label(F3,text="Amount",font=('times new rommon',10),bg=bg_color)
oldtotalLabel.grid(column=4,row=0)

for i in range(1,5):
    
    txt=Label(F3,text=i,font=('times new rommon',10),bg=bg_color)
    txt.grid(row=i,column=0,padx=0,pady=5)
    si_txt.append(txt)
    
    adrde_txt=Entry(F3,width=20,font='arial 12')
    adrde_txt.grid(row=i,column=1)

    oldwe_txt=Entry(F3,width=15,font='arial 10',bd=1,justify=CENTER)
    oldwe_txt.grid(row=i,column=2,padx=5,pady=5)

    oldunit_txt=Entry(F3,width=15,font='arial 12',bd=1,justify=CENTER)
    oldunit_txt.grid(row=i,column=3,padx=5,pady=5)

    oldtotal_txt=Entry(F3,width=15,font='arial 12',bd=1,justify=CENTER)
    oldtotal_txt.grid(row=i,column=4,padx=5,pady=5)


# =====================================================================================================================
F4 = LabelFrame(window,bg= "#FFE6BC")
F4.place(x=0,y=630,width=1500,height=80)



mode_l = Label(F4,text="Mode Of Payment",font=('times new rommon',12),bg=bg_color)
mode_l.grid(column=3,row=0)
mode= Entry(F4,width=15,font='arial 14',bd=1,justify=CENTER)
mode.grid(row=0,column=4,padx=10,pady=5)

 
charge_l = Label(F4,text="Charges",font=('times new rommon',12),bg=bg_color)
charge_l.grid(column=10,row=0)
charge_l= Entry(F4,width=15,font='arial 14',bd=1,justify=CENTER)
charge_l.grid(row=0,column=13,padx=10,pady=5)

total_l = Label(F4,text="Total",font=('times new rommon',12),bg=bg_color)
total_l.grid(column=0,row=1)
total_l= Entry(F4,width=15,font='arial 14',bd=1,justify=CENTER)
total_l.grid(row=1,column=5,padx=10,pady=5)


#================================================================================================

# ==========================================enter key binding===========================================
Name_txt.focus()

# define a function to change the tab order
# def tab_order(event):
#     widget = [Name_txt,addhar_txt,mobile_txt,bill_txt]
#     for w in widget:
#         w.lift()

# def enter(event):
#     print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

# window.bind('<Return>', tab_order)





# ======================================function of the Code================================================


def prin(event):
    os.startfile('test.xlsx','print')

def opena():
    print("Hello")
    os.system('test.xlsx')
# =================================================================================================================

F5 = LabelFrame(window,bg= "#519259")
F5.place(x=5,y=770,width=600,height=120)
# print(des_txt[0].get() == "")

newBtn = Button(F5,text="New (Ctrl+N)",font=('times new rommon',13),bg=bg_color,bd=2)
newBtn.grid(column=0,row=0,padx=20,pady=10)

printBtn = Button(F5,text="Print (Ctrl+P)",font=('times new rommon',13),command=prin,bg=bg_color,bd=2)
printBtn.grid(column=0,row=1,padx=20,pady=10)

generateBtn = Button(F5,text="Generate Bill (Ctrl+G)",font=('times new rommon',13),command=generateBill,bg=bg_color,bd=2)
generateBtn.grid(column=1,row=0,padx=20,pady=10)

findBtn = Button(F5,text = "Find (Ctrl+F)",font=('times new rommon',13),command=open,bg=bg_color,bd=2)
findBtn.grid(column=1,row=1,padx=20,pady=10)



window.bind('<Control-G>', generateBill)
window.bind('<Control-p>', prin)
window.bind('<Control-slash>', opena)

# ========================================end of the code=========================================================================
window.mainloop()