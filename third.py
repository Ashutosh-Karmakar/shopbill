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

def exit_(event):
    if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
        window.withdraw()
        sys.exit() 
 

 

window.bind('<Escape>', exit_)

bg_color = "#FFE6BC"

# ==================================creating the gui================================================

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
F2.place(x=5, y=80,width=1355,height=370)

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

wtLabel = Label(F2,text="Weight",font=('times new rommon',10),bg=bg_color)
wtLabel.grid(column=2,row=0)
wt_txt = []

unitLabel = Label(F2,text="Unit Price",font=('times new rommon',10),bg=bg_color)
unitLabel.grid(column=3,row=0)
unitLabel_txt = []

cgstLabel = Label(F2,text="CGST(1.5%)",font=('times new rommon',10),bg=bg_color)
cgstLabel.grid(column=4,row=0)
cgstLabel_txt = []

sgstLabel = Label(F2,text="SGST(1.5%)",font=('times new rommon',10),bg=bg_color)
sgstLabel.grid(column=5,row=0)
sgstLabel_txt = []

toLabel = Label(F2,text="Net",font=('times new rommon',10),bg=bg_color)
toLabel.grid(column=6,row=0)
toLabel_txt = []

for i in range(1,10):
    txt1=Entry(F2,width=80,font='arial 12',bd=1,justify=CENTER)
    txt1.grid(row=i,column=1,padx=5,pady=5)
    des_txt.append(txt1)

    txt2=Entry(F2,width=9,font='arial 12',bd=1,justify=CENTER)
    txt2.grid(row=i,column=2,padx=5,pady=5)
    wt_txt.append(txt2)

    txt3=Entry(F2,width=9,font='arial 15',bd=1,justify=CENTER)
    txt3.grid(row=i,column=3,padx=5,pady=5)
    unitLabel_txt.append(txt3)

    txt4=Entry(F2,width=10,font='arial 12',bd=1,justify=CENTER)
    txt4.grid(row=i,column=4,padx=5,pady=5)
    cgstLabel_txt.append(txt4)

    txt5=Entry(F2,width=10,font='arial 12',bd=1,justify=CENTER)
    txt5.grid(row=i,column=5,padx=5,pady=5)
    sgstLabel_txt.append(txt5)

    txt6=Entry(F2,width=16,font='arial 12',bd=1,justify=CENTER)
    txt6.grid(row=i,column=6,padx=5,pady=5)
    toLabel_txt.append(txt6)




# ======================================================================================================================


F3 = LabelFrame(window,bg= "#FFE6BC")
F3.place(x=5,y=460,width=13055,height=100)

adrdeL = Label(F3,text="Old jewels",font=('times new rommon',10),bg=bg_color)
adrdeL.grid(column=0,row=0)
adrde_txt=Text(F3,width=100,height=3,font='arial 12')
adrde_txt.grid(row=1,column=0)

oldweLabel = Label(F3,text="Weight",font=('times new rommon',10),bg=bg_color)
oldweLabel.grid(column=1,row=0)
oldwe_txt=Entry(F3,width=15,font='arial 10',bd=1,justify=CENTER)
oldwe_txt.grid(row=1,column=1,padx=5,pady=5)

oldunitLabel = Label(F3,text="Unit Price",font=('times new rommon',10),bg=bg_color)
oldunitLabel.grid(column=2,row=0)
oldunit_txt=Entry(F3,width=15,font='arial 12',bd=1,justify=CENTER)
oldunit_txt.grid(row=1,column=2,padx=5,pady=5)


oldtotalLabel = Label(F3,text="Amount",font=('times new rommon',10),bg=bg_color)
oldtotalLabel.grid(column=3,row=0)
oldtotal_txt=Entry(F3,width=15,font='arial 12',bd=1,justify=CENTER)
oldtotal_txt.grid(row=1,column=3,padx=5,pady=5)

# =====================================================================================================================
F4 = LabelFrame(window,bg= "#FFE6BC")
F4.place(x=1100,y=570,width=250,height=80)

netotal_l = Label(F4,text="Total Paid",font=('times new rommon',12),bg=bg_color)
netotal_l.grid(column=3,row=0)
netotal= Entry(F4,width=15,font='arial 14',bd=1,justify=CENTER)
netotal.grid(row=0,column=4,padx=10,pady=5)



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
def generateBill():
    wb = openpyxl.Workbook()
    sh1 = wb.active
    sh1['E1'] = "GIRIDHARI JEWELLERY"
    sh1['E1'].font = Font(name='times new rommon',size=25,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')

    sh1['D2'] = "Badheibanka Chawk, Old Town, Bhubaneswar, Mob.: 9090280083,9861230757"
    sh1['D2'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='064635')


    sh1['F3'] = "916 GOLD AND SILVER ORNAMENT"
    sh1['F3'].font = Font(name='times new rommon',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')
    
    sh1['G4'] = "Invoice"
    sh1['G4'].font = Font(name='times new rommon',size=14,bold=True,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')

    # sh1['A3'] = "Name"
    thin_border = Border(bottom=Side(border_style='thin',color='FF000000')
                # ,right=Side(border_style='dashed',color='FF000000'),
                # top=Side(border_style='thin',color='FF000000'),
                # bottom=Side(border_style='thin',color='FF000000')
                )
                
    thick_border_left = Border(left=Side(border_style='medium',color='FF000000'))
    thick_border_right = Border(right=Side(border_style='medium',color='FF000000'))
    thick_border_top = Border(top=Side(border_style='medium',color='FF000000'))
    thick_border_bottom = Border(bottom=Side(border_style='medium',color='FF000000'))
                    
    Double_border = Border(left=Side(border_style='dashed',color='FF000000'),
                    right=Side(border_style='dashed',color='FF000000'),
                    top=Side(border_style='double',color='FF000000'),
                    bottom=Side(border_style='double',color='FF000000')
                    )
    fill_cell = PatternFill(fill_type=fills.FILL_SOLID,start_color='00FFFF00',end_color='00FFFF00')
    #define size of the table 
    row_num=34
    col_num=14
    #location of the Table 
    row_loc=4
    col_loc=0
    dis=2 # distance between the tables 
    for i in range (row_loc,row_loc+row_num):
        for j in range (col_num+col_loc):
            
            if(i==row_loc and j!=col_loc+col_num-1 and j!=col_loc):
                sh1.cell(row=i+1, column=j+1).border=thick_border_top
            if(i==row_loc+row_num-1 and j!=col_loc+col_num-1 and j!=col_loc):
                    sh1.cell(row=i+1, column=j+1).border=thick_border_bottom
            
            if(i!=row_loc+row_num-1 and j==col_loc+col_num-1 and i!=row_loc):
                sh1.cell(row=i+1, column=j+1).border=thick_border_right
            if(i!=row_loc and j==col_loc and i!=row_loc+row_num-1):
                sh1.cell(row=i+1, column=j+1).border=thick_border_left

    sh1.cell(row=row_loc+row_num,column=col_loc+col_num).border=Border(bottom=Side(border_style='medium',color='FF000000'),
    right=Side(border_style='medium',color='FF000000'))

    sh1.cell(row=row_loc+1,column=col_loc+1).border=Border(left=Side(border_style='medium',color='FF000000'),
    top=Side(border_style='medium',color='FF000000'))

    sh1.cell(row=row_loc+row_num,column=col_loc+1).border=Border(left=Side(border_style='medium',color='FF000000'),
    bottom=Side(border_style='medium',color='FF000000'))

    sh1.cell(row=row_loc+1,column=col_loc+col_num).border=Border(right=Side(border_style='medium',color='FF000000'),
    top=Side(border_style='medium',color='FF000000'))

    green = '064635'
    red = 'C85C5C'
    # row_loc= row_loc+row_num+dis 
    sh1['A5'] = 'GSTIN - 21AYRPK4931F1ZH'
    sh1['A5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')

    sh1['H5'] = "SI. No.: "
    sh1['H5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='064635')
    sh1['I5'] = bill_txt.get()
    sh1['I5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')

    sh1['K5'] = 'Date: '+ daten.strftime("%d-%b-%y - (%A)")
    sh1['K5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='064635')

    for i in range(1,col_num-1):
         sh1.cell(row=5, column=i+1).border=Border(top=Side(border_style='medium',color='FF000000'),
         bottom=Side(border_style='thin',color='FF000000'))
    
    sh1.cell(row=5, column=1).border=Border(top=Side(border_style='medium',color='FF000000'),
         bottom=Side(border_style='thin',color='FF000000'),left=Side(border_style='medium',color='FF000000'))
    
    sh1.cell(row=5, column=col_num).border=Border(top=Side(border_style='medium',color='FF000000'),
         bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='medium',color='FF000000'))

    sh1['A6'] = "Name: "
    sh1['A6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['B6'] = Name_txt.get()
    sh1['B6'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

    sh1['F6'] = 'Mobile No.'
    sh1['F6'].font = Font(name='times new rommon',size=11,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['G6'] = '  '+mobile_txt.get()
    sh1['G6'].font = Font(name='arial',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

    sh1['I6'] = 'Addhar No.'
    sh1['I6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['J6'] = addhar_txt.get()
    sh1['J6'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

    sh1['M6'] = 'Bill No.'
    sh1['M6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['N6'] = bill_txt.get()
    sh1['N6'].font = Font(name='arial',size=11,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

    
    sh1['A7'] = 'Si.no.'
    sh1['A7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['D7'] = 'Description Of Goods'
    sh1['D7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['H7'] = 'HSN SAC'
    sh1['H7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['I7'] = 'Weight'
    sh1['I7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['J7'] = 'Unit Price'
    sh1['J7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['K7'] = 'Total'
    sh1['K7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['L7'] = 'CGST(1.5)'
    sh1['L7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['M7'] = 'SGST(1.5)'
    sh1['M7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['N7'] = 'NetTotal'
    sh1['N7'].font = Font(name='times new romman',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)

    for i in range(1,10):
        if(des_txt[i-1] != ""):
            sh1['A'+str(i+7)] = i
            sh1['B'+str(i+7)] = des_txt[i-1].get()
            
    

    openpyxl.worksheet.worksheet.Worksheet.set_printer_settings(sh1, paper_size = 1, orientation='landscape')
    sh1.page_margins.top=.2
    sh1.page_margins.right=.2
    sh1.page_margins.bottom=.2



    wb.save(filename='test.xlsx')
    os.system('test.xlsx')


def prin(event):
    os.startfile('test.xlsx','print')

def opena():
    print("Hello")
    os.system('test.xlsx')
# =================================================================================================================

F5 = LabelFrame(window,bg= "#519259")
F5.place(x=5,y=570,width=600,height=120)
print(des_txt[0].get() == "")

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