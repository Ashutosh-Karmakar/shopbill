from tkinter import *
from tkinter.ttk import *
import tkinter
from tkinter import *
import os
import sys
import datetime
import pyautogui

from baseIntialization import UiFields
from backend import enterOperation, newBill, set_total_after_charges, clicked_tab, check_clicked_tab
from goldrate import changeGoldRate
from monthlyGST import monthlyGst
from findGoldrate import findGoldRateOnDate
from billgenerator import generateBill
from database import findBillNumber, findGoldRate, findConfigValue
from changeConfig import config


u = UiFields()
u.gold_rate = 4876
u.bg_color = findConfigValue('bg_color')
u.BASEDIR_BILL = findConfigValue('BASEDIR_BILL')
print(u.BASEDIR_GST)
u.background_color = u.bg_color
window = tkinter.Tk()
window.attributes('-fullscreen', True)
window.configure(bg=u.background_color)
window.title("Giridhari Jewellery")

def enter(event):
    focused_tab = str(window.focus_get())
    print(focused_tab)
    i = enterOperation(focused_tab,u)  
    if(i!=1):
        pyautogui.press("tab")
        
    
def exit_(event):
    if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
        window.withdraw()
        sys.exit() 
    

def backOp(event):
    if(u.entryCount <= 1):
        u.entryCount = 0
        # u.mobile_txt.focus
    else:
        u.entryCount-=1
    u.entry_list[u.entryCount].focus()

window.bind('<Escape>', exit_)
window.bind("<Return>",enter)
window.bind('<Left>', backOp)




def position(event):
    k = check_clicked_tab(u)
    if(k!=1):
        print(window.focus_get())
        u.entryCount = clicked_tab(str(window.focus_get()))
        print(u.entryCount)
window.bind('<Button-1>', position)
    

daten = datetime.datetime.now()

# ==================================customer detail==================================
labelfont = 10
textfont = 10

u.mobile=Label(window, text='Mobile No.:', font=('times new rommon',labelfont),bg=u.bg_color)
u.mobile.grid(row=1,column=0,padx=10)
u.mobile_txt=Entry(window,width=20,font='arial '+str(textfont),bd=2,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
u.mobile_txt.grid(row=1,column=1,pady=15)
u.mobile_txt.focus()
u.entry_list.append(u.mobile_txt)

u.name=Label(window, text='Name:', font=('times new rommon',labelfont),bg=u.bg_color)
u.name.grid(row=1,column=4,padx=10)
u.name_txt=Entry(window,width=30,font='arial '+str(textfont),bd=2,justify=LEFT,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
u.name_txt.grid(row=1,column=5,pady=15)
u.entry_list.append(u.name_txt)

u.address=Label(window, text='Address:', font=('times new rommon',labelfont),bg=u.bg_color)
u.address.grid(row=1,column=9)
u.address_txt=Entry(window,width=25,font='arial '+str(textfont),bd=2,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
u.address_txt.grid(row=1,column=10)
u.entry_list.append(u.address_txt)

u.addhar=Label(window, text='Addhar No.:', font=('times new rommon',labelfont),bg=u.bg_color)
u.addhar.grid(row=1,column=14)
u.addhar_txt=Entry(window,width=25,font='arial '+str(textfont),bd=2,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
u.addhar_txt.grid(row=1,column=15)
u.entry_list.append(u.addhar_txt)

u.bill_txt = findBillNumber()
u.bill=Label(window, text='Bill No.:', font=('times new rommon',labelfont),bg=u.bg_color)
u.bill.grid(row=1,column=20)
u.bill_txt_entry=Entry(window,width=25,font='arial '+str(textfont),bd=2,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
u.bill_txt_entry.grid(row=1,column=21)
u.bill_txt_entry.insert(0,u.bill_txt)
u.bill_txt_entry.config(state=DISABLED)

u.date_label=Label(window, text=daten.strftime("%d-%b-%y - (%A)"), font=('times new rommon',labelfont),bg=u.bg_color)
u.date_label.grid(row=1,column=30)



# ========================================new Gold==============================================

F2 = LabelFrame(window,bg= u.bg_color)
F2.place(x=5, y=55,width=1850,height=360)

u.siLabel = Label(F2,text="Sino.",font=('times new rommon',10),bg=u.bg_color)
u.siLabel.grid(column=0,row=0)
for i in range(1,10):
    txt=Label(F2,text=i,font=('times new rommon',10),bg=u.bg_color)
    txt.grid(row=i,column=0,padx=0,pady=5)
    u.si_txt.append(txt)


u.desLabel = Label(F2,text="Description",font=('times new rommon',10),bg=u.bg_color)
u.desLabel.grid(column=1,row=0)

u.wtLabel = Label(F2,text="Weight",font=('times new rommon',10),bg=u.bg_color)
u.wtLabel.grid(column=3,row=0)

u.netLabel = Label(F2,text="Net",font=('times new rommon',10),bg=u.bg_color)
u.netLabel.grid(column=4,row=0)

u.mcLabel = Label(F2,text="MC",font=('times new rommon',10),bg=u.bg_color)
u.mcLabel.grid(column=5,row=0)

u.unitLabel = Label(F2,text="Unit Price",font=('times new rommon',10),bg=u.bg_color)
u.unitLabel.grid(column=6,row=0)

u.cgstLabel = Label(F2,text="CGST(1.5%)",font=('times new rommon',10),bg=u.bg_color)
u.cgstLabel.grid(column=7,row=0)

u.sgstLabel = Label(F2,text="SGST(1.5%)",font=('times new rommon',10),bg=u.bg_color)
u.sgstLabel.grid(column=8,row=0)

u.gstAmtLabel = Label(F2,text="GstAmt",font=('times new rommon',10),bg=u.bg_color)
u.gstAmtLabel.grid(column=9,row=0)

findGoldRate(u)

for i in range(1,10):
    txt1=Entry(F2,width=30,font='arial 15',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt1.grid(row=i,column=1,padx=4,pady=3)
    u.entry_list.append(txt1)
    u.des_txt.append(txt1)

    txt2=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt2.grid(row=i,column=3,padx=4,pady=3)
    u.entry_list.append(txt2)
    u.wt_txt.append(txt2)

    txt3=Entry(F2,width=16,font='arial 15',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt3.grid(row=i,column=4,padx=4,pady=3)
    u.entry_list.append(txt3)
    u.net_txt.append(txt3)
    
    txt4=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt4.grid(row=i,column=5,padx=4,pady=3)
    txt4.config(state=DISABLED)
    u.mc_txt.append(txt4)
    
    txt5=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt5.grid(row=i,column=6,padx=4,pady=3)
    txt5.insert(0,u.gold_rate)
    txt5.config(state=DISABLED)
    u.unit_txt.append(txt5)

    txt6=Entry(F2,width=10,font='arial 15',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt6.grid(row=i,column=7,padx=4,pady=3)
    txt6.config(state=DISABLED)
    u.cgst_txt.append(txt6)

    txt7=Entry(F2,width=10,font='arial 15',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt7.grid(row=i,column=8,padx=4,pady=3)
    txt7.config(state=DISABLED)
    u.sgst_txt.append(txt7)

    txt8=Entry(F2,width=10,font='arial 15',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt8.grid(row=i,column=9,padx=4,pady=3)
    txt8.config(state=DISABLED)
    u.gstAmt_txt.append(txt8)


# ==================================old gold=====================================================

F3 = LabelFrame(window,bg= u.bg_color)
F3.place(x=5,y=415,width=13055,height=117)

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
    txt9=Label(F3,text=i,font=('times new rommon',10),bg=u.bg_color)
    txt9.grid(row=i,column=0,padx=4,pady=2)
    u.oldSi_txt.append(txt9)
    
    txt10=Entry(F3,width=80,font='arial 12',highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt10.grid(row=i,column=1,padx=4,pady=2)
    txt10.insert(0 ,'Old Ornament')
    txt10.config(state=DISABLED)
    u.oldDesc_txt.append(txt10)

    txt11=Entry(F3,width=15,font='arial 10',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt11.grid(row=i,column=2,padx=4,pady=2)
    u.entry_list.append(txt11)
    u.oldwe_txt.append(txt11)

    txt12=Entry(F3,width=15,font='arial 12',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt12.grid(row=i,column=3,padx=4,pady=2)
    txt12.insert(0,u.gold_rate-100)
    txt12.config(state = DISABLED)
    u.oldunit_txt.append(txt12)

    txt13=Entry(F3,width=15,font='arial 12',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt13.grid(row=i,column=4,padx=4,pady=2)
    u.entry_list.append(txt13)
    u.oldtotal_txt.append(txt13)


#===========================================addition or deduction===============================

F4 = LabelFrame(window,bg= u.bg_color)
F4.place(x=5,y=530,width=13055,height=120)

u.addSi = Label(F4,text="Si.",font=('times new rommon',10),bg=u.bg_color)
u.addSi.grid(column=0,row=0)

u.addDescL = Label(F4,text="Other Addition",font=('times new rommon',10),bg=u.bg_color)
u.addDescL.grid(column=1,row=0)

u.addtotalLabel = Label(F4,text="Amount",font=('times new rommon',10),bg=u.bg_color)
u.addtotalLabel.grid(column=4,row=0)

for i in range(1,4):
    txt14=Label(F4,text=i,font=('times new rommon',10),bg=u.bg_color)
    txt14.grid(row=i,column=0,padx=4,pady=2)
    u.addSi_txt.append(txt14)
    
    txt15=Entry(F4,width=80,font='arial 12',highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt15.grid(row=i,column=1,padx=4,pady=2)
    txt15.insert(0 ,'Others')
    txt15.config(state=DISABLED)
    u.addDesc_txt.append(txt15)

    txt16=Entry(F4,width=15,font='arial 12',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
    txt16.grid(row=i,column=4,padx=4,pady=2)
    u.entry_list.append(txt16)
    u.addtotal_txt.append(txt16)

#=================================mode of payment and total==============================
F5 = LabelFrame(window,bg= u.bg_color)
F5.place(x=0,y=650,width=1500,height=50)

def selected(event):
    if(u.clicked.get() == 'Debit Card'):
        u.charge.delete(0,END)
        u.charge.insert(0,'1.2%')
        u.charge_amt = 1.2
    elif(u.clicked.get() == 'Credit Card'):
        u.charge.delete(0,END)
        u.charge.insert(0,'2.1%')
        u.charge_amt = 2.1
    else:
        u.charge.delete(0,END)
    u.mode = u.clicked.get()
    set_total_after_charges(u)
        

options = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "UPI",
    "Bank"
]
  
u.clicked = StringVar()
u.clicked.set(options[0])
 
u.mode_l = OptionMenu( F5 , u.clicked , *options, command=selected)
u.mode_l.grid(column=3,row=0)
u.mode_l.config(font=('times new rommon',11))

u.charge_l = Label(F5,text="Charges",font=('times new rommon',12),bg=u.bg_color)
u.charge_l.grid(column=10,row=0)
u.charge= Entry(F5,width=15,font='arial 14',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
u.charge.grid(row=0,column=13,padx=10,pady=5)
u.entry_list.append(u.charge)


u.total_l = Label(F5,text="Total",font=('times new rommon',12),bg=u.bg_color)
u.total_l.grid(column=15,row=0)
u.total= Entry(F5,width=15,font='arial 14',bd=1,justify=CENTER,highlightthickness=u.border_size,highlightcolor= u.entry_correct_color)
u.total.grid(row=0,column=35,padx=10,pady=5)
u.total.insert(0,0)
u.entry_list.append(u.total)


# ======================================Buttons of the Code=========================


def findBill():
    os.system('python findBill.py')
    
F6 = LabelFrame(window,bg= "#519259")
F6.place(x=5,y=700,width=1500,height=50)

u.newBtn = Button(F6,text="New",font=('times new rommon',13),command=lambda: newBill(u),bg=u.bg_color,bd=2)
u.newBtn.grid(column=0,row=0,padx=20,pady=10)

u.generateBtn = Button(F6,text="Generate Bill",font=('times new rommon',13),command=lambda: generateBill(u),bg=u.bg_color,bd=2)
u.generateBtn.grid(column=1,row=0,padx=20,pady=10)

# u.findBtn = Button(F6,text = "Find (Ctrl+F)",font=('times new rommon',13),command=findBill,bg=u.bg_color,bd=2)
# u.findBtn.grid(column=3,row=0,padx=20,pady=10)

u.change_gold_rate = Button(F6,text="Gold Rate" ,font=('times new rommon',13),command=lambda: changeGoldRate(u),bg=u.bg_color,bd=2)
u.change_gold_rate.grid(column=2,row=0,padx=20,pady=10)

u.findgoldBtn = Button(F6,text="Find GR" ,font=('times new rommon',13),command=lambda:findGoldRateOnDate(u),bg=u.bg_color,bd=2)
u.findgoldBtn.grid(column=3,row=0,padx=20,pady=10)

u.gstBtn = Button(F6,text="Gst " ,font=('times new rommon',13),command=lambda:monthlyGst(u),bg=u.bg_color,bd=2)
u.gstBtn.grid(column=4,row=0,padx=20,pady=10)

u.config_btn = Button(F6,text="Config",font=('times new rommon',13),command=lambda: config(u),bg=u.bg_color,bd=2)
u.config_btn.grid(column=5,row=0,padx=20,pady=10)

# window.bind('<Control-G>', generateBill(u))
# window.bind('<Control-p>', prin)
# window.bind('<Control-slash>', opena)
window.mainloop()

# ========================================end of the code================================