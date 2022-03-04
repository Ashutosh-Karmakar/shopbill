from cgitb import text
from multiprocessing.spawn import old_main_modules
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
from turtle import bgcolor
from xml.etree.ElementPath import find
from database import findByNumber
from openpyxl.drawing.image import Image 
from billgenerator import generateBill
from database import findBillNumber
import datetime

import pyautogui

from baseIntialization import UiFields
from backend import enterOperation
  

u = UiFields()
u.gold_rate = 4500
window = tkinter.Tk()
window.attributes('-fullscreen', True)
window.configure(bg='#FFE6BC')
window.title("Giridhari Jewellery")

def enter(event):
    focused_tab = str(window.focus_get())
    print(focused_tab)
    enterOperation(focused_tab,u)   
    pyautogui.press("tab")
    
def exit_(event):
    if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
        window.withdraw()
        sys.exit() 





    
        
window.bind('<Escape>', exit_)
window.bind("<Return>",enter)


       

daten = datetime.datetime.now()

# ==================================creating the gui==================================
labelfont = 11
textfont = 11

u.mobile=Label(window, text='Mobile No.:', font=('times new rommon',labelfont),bg=u.bg_color)
u.mobile.grid(row=1,column=0,padx=10)
u.mobile_txt=Entry(window,width=20,font='arial '+str(textfont),bd=2,justify=CENTER)
u.mobile_txt.grid(row=1,column=1,pady=15)
u.mobile_txt.focus()

u.name=Label(window, text='Name and Address:', font=('times new rommon',labelfont),bg=u.bg_color)
u.name.grid(row=1,column=4,padx=10)
u.name_txt=Entry(window,width=30,font='arial '+str(textfont),bd=2,justify=LEFT)
u.name_txt.grid(row=1,column=5,pady=15)

u.address=Label(window, text='Address:', font=('times new rommon',labelfont),bg=u.bg_color)
u.address.grid(row=1,column=9)
u.address_txt=Entry(window,width=25,font='arial '+str(textfont),bd=2,justify=CENTER)
u.address_txt.grid(row=1,column=10)

u.addhar=Label(window, text='Addhar No.:', font=('times new rommon',labelfont),bg=u.bg_color)
u.addhar.grid(row=1,column=14)
u.addhar_txt=Entry(window,width=25,font='arial '+str(textfont),bd=2,justify=CENTER)
u.addhar_txt.grid(row=1,column=15)

u.bill=Label(window, text='Bill No.:', font=('times new rommon',labelfont),bg=u.bg_color)
u.bill.grid(row=1,column=20)
bill_txt = Label(window, text=str(findBillNumber())+"  \t", font='arial '+str(textfont), bg=u.bg_color)
bill_txt.grid(row=1,column=25,pady=15)
u.bill_txt = findBillNumber()

u.date_label=Label(window, text=daten.strftime("%d-%b-%y - (%A)"), font=('times new rommon',labelfont),bg=u.bg_color)
u.date_label.grid(row=1,column=30)



# ===========================================================================================

F2 = LabelFrame(window,bg= "#FFE6BC")
F2.place(x=5, y=80,width=1900,height=390)

u.siLabel = Label(F2,text="Sino.",font=('times new rommon',10),bg=u.bg_color)
u.siLabel.grid(column=0,row=0)
for i in range(1,10):
    txt=Label(F2,text=i,font=('times new rommon',10),bg=u.bg_color)
    txt.grid(row=i,column=0,padx=0,pady=5)
    u.si_txt.append(txt)


u.desLabel = Label(F2,text="Description",font=('times new rommon',10),bg=u.bg_color)
u.desLabel.grid(column=1,row=0)

# u.pcsLabel = Label(F2,text="Pcs",font=('times new rommon',10),bg=u.bg_color)
# u.pcsLabel.grid(column=2,row=0)

u.wtLabel = Label(F2,text="Weight",font=('times new rommon',10),bg=u.bg_color)
u.wtLabel.grid(column=3,row=0)


u.mcLabel = Label(F2,text="MC",font=('times new rommon',10),bg=u.bg_color)
u.mcLabel.grid(column=4,row=0)

u.unitLabel = Label(F2,text="Unit Price",font=('times new rommon',10),bg=u.bg_color)
u.unitLabel.grid(column=5,row=0)


u.cgstLabel = Label(F2,text="CGST(1.5%)",font=('times new rommon',10),bg=u.bg_color)
u.cgstLabel.grid(column=6,row=0)

u.sgstLabel = Label(F2,text="SGST(1.5%)",font=('times new rommon',10),bg=u.bg_color)
u.sgstLabel.grid(column=7,row=0)

u.gstAmtLabel = Label(F2,text="GstAmt",font=('times new rommon',10),bg=u.bg_color)
u.gstAmtLabel.grid(column=8,row=0)

u.netLabel = Label(F2,text="Net",font=('times new rommon',10),bg=u.bg_color)
u.netLabel.grid(column=9,row=0)

for i in range(1,10):
    txt1=Entry(F2,width=40,font='arial 15',bd=1,justify=CENTER)
    txt1.grid(row=i,column=1,padx=4,pady=3)
    u.des_txt.append(txt1)
    
    # txt2=Entry(F2,width=3,font='arial 15',bd=1,justify=CENTER)
    # txt2.grid(row=i,column=2,padx=4,pady=3)
    # txt2.insert(0,1)
    # u.append(txt2)
 
    txt3=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER)
    txt3.grid(row=i,column=3,padx=4,pady=3)
    u.wt_txt.append(txt3)

    
    txt4=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER)
    txt4.grid(row=i,column=4,padx=4,pady=3)
    u.mc_txt.append(txt4)
    
    
    txt5=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER)
    txt5.grid(row=i,column=5,padx=4,pady=3)
    txt5.insert(0,u.gold_rate)
    u.unit_txt.append(txt5)

    txt6=Entry(F2,width=10,font='arial 15',bd=1,justify=CENTER)
    txt6.grid(row=i,column=6,padx=4,pady=3)
    u.cgst_txt.append(txt6)

    txt7=Entry(F2,width=10,font='arial 15',bd=1,justify=CENTER)
    txt7.grid(row=i,column=7,padx=4,pady=3)
    u.sgst_txt.append(txt7)

    txt8=Entry(F2,width=10,font='arial 15',bd=1,justify=CENTER)
    txt8.grid(row=i,column=8,padx=4,pady=3)
    u.gstAmt_txt.append(txt8)


    txt9=Entry(F2,width=16,font='arial 15',bd=1,justify=CENTER)
    txt9.grid(row=i,column=9,padx=4,pady=3)
    u.net_txt.append(txt9)




# ======================================================================================================================

F3 = LabelFrame(window,bg= "#FFE6BC")
F3.place(x=5,y=480,width=13055,height=140)

u.oldSi = Label(F3,text="Si.",font=('times new rommon',10),bg=u.bg_color)
u.oldSi.grid(column=0,row=0)

u.oldDescL = Label(F3,text="Old jewels",font=('times new rommon',10),bg=u.bg_color)
u.oldDescL.grid(column=1,row=0)

u.oldweLabel = Label(F3,text="Weight",font=('times new rommon',10),bg=u.bg_color)
u.oldweLabel.grid(column=2,row=0)

u.oldunitLabel = Label(F3,text="Unit Price",font=('times new rommon',10),bg=u.bg_color)
u.oldunitLabel.grid(column=3,row=0)

u.oldtotalLabel = Label(F3,text="Amount",font=('times new rommon',10),bg=u.bg_color)
u.oldtotalLabel.grid(column=4,row=0)

for i in range(1,4): 
    txt10=Label(F3,text=i,font=('times new rommon',10),bg=u.bg_color)
    txt10.grid(row=i,column=0,padx=4,pady=2)
    u.oldSi_txt.append(txt10)
    
    txt11=Entry(F3,width=80,font='arial 12')
    txt11.grid(row=i,column=1,padx=4,pady=2)
    txt11.insert(0,'Old Gold')
    u.oldDesc_txt.append(txt11)

    txt12=Entry(F3,width=15,font='arial 10',bd=1,justify=CENTER)
    txt12.grid(row=i,column=2,padx=4,pady=2)
    u.oldwe_txt.append(txt12)

    txt13=Entry(F3,width=15,font='arial 12',bd=1,justify=CENTER)
    txt13.grid(row=i,column=3,padx=4,pady=2)
    txt13.insert(0,u.gold_rate-100)
    u.oldunit_txt.append(txt13)

    txt14=Entry(F3,width=15,font='arial 12',bd=1,justify=CENTER)
    txt14.grid(row=i,column=4,padx=4,pady=2)
    u.oldtotal_txt.append(txt14)


#=================================================================================================

F4 = LabelFrame(window,bg= "#FFE6BC")
F4.place(x=5,y=620,width=13055,height=140)

u.addSi = Label(F4,text="Si.",font=('times new rommon',10),bg=u.bg_color)
u.addSi.grid(column=0,row=0)

u.addDescL = Label(F4,text="Other Addition/Deduction",font=('times new rommon',10),bg=u.bg_color)
u.addDescL.grid(column=1,row=0)

u.addtotalLabel = Label(F4,text="Amount",font=('times new rommon',10),bg=u.bg_color)
u.addtotalLabel.grid(column=4,row=0)

for i in range(1,4):
    txt15=Label(F4,text=i,font=('times new rommon',10),bg=u.bg_color)
    txt15.grid(row=i,column=0,padx=4,pady=2)
    u.addSi_txt.append(txt15)
    
    txt16=Entry(F4,width=80,font='arial 12')
    txt16.grid(row=i,column=1,padx=4,pady=2)
    u.addDesc_txt.append(txt16)

    txt17=Entry(F4,width=15,font='arial 12',bd=1,justify=CENTER)
    txt17.grid(row=i,column=4,padx=4,pady=2)
    u.addtotal_txt.append(txt17)



#===========================================================
F5 = LabelFrame(window,bg= "#FFE6BC")
F5.place(x=0,y=750,width=1500,height=100)



u.mode_l = Label(F5,text="Mode Of Payment",font=('times new rommon',12),bg=u.bg_color)
u.mode_l.grid(column=3,row=0)
u.mode= Entry(F5,width=15,font='arial 14',bd=1,justify=CENTER)
u.mode.grid(row=0,column=4,padx=10,pady=5)

u.charge_l = Label(F5,text="Charges",font=('times new rommon',12),bg=u.bg_color)
u.charge_l.grid(column=10,row=0)
u.charge= Entry(F5,width=15,font='arial 14',bd=1,justify=CENTER)
u.charge.grid(row=0,column=13,padx=10,pady=5)

u.total_l = Label(F5,text="Total",font=('times new rommon',12),bg=u.bg_color)
u.total_l.grid(column=0,row=1)
u.total= Entry(F5,width=15,font='arial 14',bd=1,justify=CENTER)
u.total.grid(row=1,column=5,padx=10,pady=5)
u.total.insert(0,0)

#================================================================================================

# ==========================================enter key binding===========================================

# define a function to change the tab order
# def tab_order(event):
#     widget = [Name_txt,addhar_txt,mobile_txt,bill_txt]
#     for w in widget:
#         w.lift()

# def enter(event):
#     print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

# window.bind('<Return>', tab_order)





# ======================================function of the Code================================================


def prin():
    os.startfile('test.xlsx','print')

def opena():
    print("Hello")
    os.system('test.xlsx')
# =================================================================================================================



F6 = LabelFrame(window,bg= "#519259")
F6.place(x=5,y=900,width=1500,height=70)
# print(des_txt[0].get() == "")

# g = GenerateBill()

u.newBtn = Button(F6,text="New (Ctrl+N)",font=('times new rommon',13),bg=u.bg_color,bd=2)
u.newBtn.grid(column=0,row=0,padx=20,pady=10)

u.printBtn = Button(F6,text="Print (Ctrl+P)",font=('times new rommon',13),command=prin,bg=u.bg_color,bd=2)
u.printBtn.grid(column=1,row=0,padx=20,pady=10)

u.generateBtn = Button(F6,text="Generate Bill (Ctrl+G)",font=('times new rommon',13),command=lambda: generateBill(u),bg=u.bg_color,bd=2)
u.generateBtn.grid(column=2,row=0,padx=20,pady=10)

u.findBtn = Button(F6,text = "Find (Ctrl+F)",font=('times new rommon',13),command=open,bg=u.bg_color,bd=2)
u.findBtn.grid(column=3,row=0,padx=20,pady=10)



window.bind('<Control-G>', generateBill(u))
window.bind('<Control-p>', prin)
window.bind('<Control-slash>', opena)

# ========================================end of the code=========================================================================
window.mainloop()