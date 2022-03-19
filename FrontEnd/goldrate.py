import tkinter as tk
from tkinter import simpledialog
from tkinter import *
from baseIntialization import UiFields
from tkinter import messagebox
from database import saveGoldRate




        
def calc(u:UiFields, i):
    wt = float(u.wt_txt[i].get())
    amt = float(u.net_txt[i].get())
    gr = u.gold_rate
    
    cost = (amt)*(100/103)
    if(cost < amt):
        cgst = amt - cost
    else:
        cgst = 0
    try:
        mc = (cost/wt)-gr
    except Exception:
        print("there is a error in calculation")
        u.wt_txt[i].focus_set()
    
    mc = round(mc,2)
    cgst = round(cgst/2,2)
    gstamt = cgst*2
    
    if(mc < 0):
        print("There is a error in calculation mc")
    
    u.cgst_txt[i].config(state='normal')
    u.sgst_txt[i].config(state='normal')
    u.gstAmt_txt[i].config(state='normal')
    u.mc_txt[i].config(state='normal')
    
    u.cgst_txt[i].delete(0,END)
    u.cgst_txt[i].insert(0,cgst)
    
    u.sgst_txt[i].delete(0,END)
    u.sgst_txt[i].insert(0,cgst)
    
    u.gstAmt_txt[i].delete(0,END)
    u.gstAmt_txt[i].insert(0,gstamt)
    
    u.mc_txt[i].delete(0,END)
    u.mc_txt[i].insert(0,mc)
    
    u.cgst_txt[i].config(state=DISABLED)
    u.sgst_txt[i].config(state=DISABLED)
    u.gstAmt_txt[i].config(state=DISABLED)
    u.mc_txt[i].config(state=DISABLED)
    
    u.gstAmt_txt[i].focus_set()
        
        
        
        

def changeGoldRate(u:UiFields):
    gr = tk.Tk()
    gr.withdraw()
    gold_rate = simpledialog.askstring(title="Gold Rate", prompt="Gold Rate?:")
    if(gold_rate.isnumeric()==False):
        messagebox.showerror("Error","Gold Rate can only be number")
        return
    if(len(gold_rate) > 4):
        tens = 10**(len(gold_rate)-4)
        u.gold_rate = int(gold_rate)//tens
    else:
        u.gold_rate = int(gold_rate)
    saveGoldRate(u)
    for i in range(0,9):
        u.unit_txt[i].config(state='normal')
        u.unit_txt[i].delete(0,END)
        u.unit_txt[i].insert(0,u.gold_rate)
        u.unit_txt[i].config(state=DISABLED)
        
    u.old_gold_rate = u.gold_rate - 100
    
    for i in range(0,3):
        u.oldunit_txt[i].config(state='normal')
        u.oldunit_txt[i].delete(0,END)
        u.oldunit_txt[i].insert(0,u.old_gold_rate)
        u.oldunit_txt[i].config(state=DISABLED)
        
    for i in range(0,10):
        if(u.des_txt[i].get()=='' or u.wt_txt[i].get()=='' or u.net_txt[i].get()==''):
            break
        calc(u,i)
        

    
        