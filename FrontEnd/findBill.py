import sys
from tkinter import *
import tkinter
from baseIntialization import UiFields
from database import findBillData
from billFindEntry import found
import pandas as pd
import os
# y = UiFields()
# #not completed yetp

def find(u:UiFields):
    result = findBillData(u)
    print(result)
    path = os.path.join(u.BASEDIR_BILL,'Apr_22\\71.xlsx')
    df = pd.read_excel (result[0], sheet_name='bill')
    # print (df)
    arr = df.to_numpy()
    found(u,arr)

    # window1 = tkinter.Tk()

    # def exit_(event):
    #     if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
    #         window.withdraw()
    #         sys.exit() 
        
    # window1.bind('<Escape>', exit_)

    # frame = Frame(window1)
    # frame.pack(fill=BOTH, expand = 1)

    # canvas = Canvas(frame)
    # canvas.pack(side=LEFT,fill=BOTH,expand=1)

    # scrollbar = tkinter.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    # scrollbar.pack(side=RIGHT, fill=Y)

    # canvas.configure(yscrollcommand=scrollbar.set)
    # canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

    # second_frame = Frame(canvas)
    # canvas.create_window((0,0), window=second_frame, anchor="nw")

    # for i in range(2,20):
    #     listi=Label(second_frame, text='Addhar No.:', font=('times new rommon',10))
    #     listi.grid(row=i,column=0)

    # window1.mainloop()
   

# window = tkinter.Tk()
# # window.attributes('-fullscreen', True)
# window.geometry('800x100')
# window.configure(bg=y.background_color)
# window.title("Find Bill")

# def exit_(event):
#     if(tkinter.messagebox.askokcancel('QUIT','Do You Want to Quit??')):
#         window.withdraw()
#         sys.exit() 
    
# window.bind('<Escape>', exit_)

# y.billing_ph_no_label=Label(window, text='Mobile:', font=('times new rommon',11),bg=y.bg_color)
# y.billing_ph_no_label.grid(row=1,column=0)
# y.billing_ph_no=Entry(window,width=20,font='arial 11',bd=2,justify=CENTER)
# y.billing_ph_no.grid(row=1,column=1)
# y.billing_ph_no.focus()

# y.billing_date_label=Label(window, text='Billing Date:', font=('times new rommon',11),bg=y.bg_color)
# y.billing_date_label.grid(row=1,column=2)
# y.billing_date=Entry(window,width=20,font='arial 11',bd=2,justify=CENTER)
# y.billing_date.grid(row=1,column=3)

# y.billing_no_label=Label(window, text='Bill number:', font=('times new rommon',11),bg=y.bg_color)
# y.billing_no_label.grid(row=1,column=4)
# y.billing_no=Entry(window,width=20,font='arial 11',bd=2,justify=CENTER)
# y.billing_no.grid(row=1,column=5)

# findBtn = Button(window,text="find",font=('times new rommon',13),command=find,bg='red',bd=2)
# findBtn.grid(column=3,row=2,padx=20,pady=10)


# window.mainloop()

 
    

