from baseIntialization import UiFields
from database import findByNumber
import tkinter
from tkinter import *


def focusedTab(focused_tab):
    if(focused_tab == '.!entry'):
        return 'number'
    if(focused_tab == '.!labelframe.!entry4' or focused_tab == '.!labelframe.!entry13' or focused_tab == '.!labelframe.!entry22' or focused_tab == '.!labelframe.!entry31' or focused_tab == '.!labelframe.!entry40' or focused_tab == '.!labelframe.!entry49' or focused_tab == '.!labelframe.!entry58' or focused_tab == '.!labelframe.!entry67'):
        return 'mc'
    if(focused_tab == '.!labelframe.!entry' or focused_tab == '.!labelframe.!entry10' or focused_tab == '.!labelframe.!entry19' or focused_tab == '.!labelframe.!entry28' or focused_tab == '.!labelframe.!entry37' or focused_tab == '.!labelframe.!entry46' or focused_tab == '.!labelframe.!entry55' or focused_tab == '.!labelframe.!entry64' or focused_tab == '.!labelframe.!entry73'):
        return 'desc'
    if(focused_tab == '.!labelframe2.!entry2' or focused_tab == '.!labelframe2.!entry6' or focused_tab == '.!labelframe2.!entry10'):
        return 'oldWt'
    if(focused_tab == '.!labelframe2.!entry' or focused_tab == '.!labelframe2.!entry5' or focused_tab == '.!labelframe2.!entry9'):
        return 'oldDesc'
    if(focused_tab == '.!labelframe3.!entry' or focused_tab == '.!labelframe3.!entry3' or focused_tab == '.!labelframe3.!entry5'):
        return 'addDesc'
    if(focused_tab == '.!labelframe2.!entry4' or focused_tab == '.!labelframe2.!entry8' or focused_tab == '.!labelframe2.!entry12'):
        return 'oldAmt'
    if(focused_tab == '.!labelframe3.!entry2' or focused_tab == '.!labelframe3.!entry4' or focused_tab == '.!labelframe3.!entry6'):
        return 'addAmt'
    if(focusedTab == '.!labelframe4.!entry2'):
        return 'charges'
    if(focused_tab == '.!labelframe4.!entry3'):
        return 'total'
    
def tabNumber(focused_tab):
    #mc entry:
    if focused_tab == '.!labelframe.!entry4':
        return 0
    if focused_tab == '.!labelframe.!entry13':
        return 1
    if focused_tab == '.!labelframe.!entry22':
        return 2
    if focused_tab == '.!labelframe.!entry31':
        return 3
    if focused_tab == '.!labelframe.!entry40':
        return 4
    if focused_tab == '.!labelframe.!entry49':
        return 5
    if focused_tab == '.!labelframe.!entry58':
        return 6
    if focused_tab == '.!labelframe.!entry67':
        return 7
    if focused_tab == '.!labelframe.!entry76':
        return 8
    
    #desc entry:
    if focused_tab == '.!labelframe.!entry':
        return 0
    if focused_tab == '.!labelframe.!entry10':
        return 1
    if focused_tab == '.!labelframe.!entry19':
        return 2
    if focused_tab == '.!labelframe.!entry28':
        return 3
    if focused_tab == '.!labelframe.!entry37':
        return 4
    if focused_tab == '.!labelframe.!entry46':
        return 5
    if focused_tab == '.!labelframe.!entry55':
        return 6
    if focused_tab == '.!labelframe.!entry64':
        return 7
    if focused_tab == '.!labelframe.!entry73':
        return 8
    
    #old gold desc entry:
    if focused_tab == '.!labelframe2.!entry':
        return 0
    if focused_tab == '.!labelframe2.!entry5':
        return 1
    if focused_tab == '.!labelframe2.!entry9':
        return 2
    
    #old gold weight
    if focused_tab == '.!labelframe2.!entry2':
        return 0
    if focused_tab == '.!labelframe2.!entry6':
        return 1
    if focused_tab == '.!labelframe2.!entry10':
        return 2
    
    #old gold amt
    if(focused_tab == '.!labelframe2.!entry4'):
        return 0
    if(focused_tab == '.!labelframe2.!entry8'):
        return 1
    if(focused_tab == '.!labelframe2.!entry12'):
        return 2
    
    #add desc : 
    if focused_tab == '.!labelframe3.!entry':
        return 0
    if focused_tab == '.!labelframe3.!entry3':
        return 1
    if focused_tab == '.!labelframe3.!entry5':
        return 2
        
    
    

def setCustData(u:UiFields, data):
    print(data)
    u.name_txt.insert(0,data[1])
    u.address_txt.insert(0,data[3])
    u.addhar_txt.insert(0,data[4])
    u.bill_txt.focus_set()


def calculate(u:UiFields,focused_tab):
    i = tabNumber(focused_tab)
    qty = float(u.pcs_txt[i].get())
    wt = float(u.wt_txt[i].get())
    mc = float(u.mc_txt[i].get())
    gr = u.gold_rate
    cost = wt * (gr+mc) * qty
    cgst = (cost * 1.5)/100
    gstamt = cgst*2
    net_total = cost + gstamt
    u.cgst_txt[i].insert(0,cgst)
    u.sgst_txt[i].insert(0,cgst)
    u.gstAmt_txt[i].insert(0,gstamt)
    u.net_txt[i].insert(0,net_total)
    u.net_txt[i].focus_set()

def findAmt(amt):
    return float(amt.get())

def setTotal(u:UiFields,amt):
    u.total.delete(0,END)
    u.total.insert(0,(amt))


def enterOperation(focused_tab,u:UiFields):
    tab_name = focusedTab(focused_tab)
    i = tabNumber(focused_tab)
    if(tab_name == 'oldAmt'):
        u.oldDesc_txt[i+1].focus_set()
    if(tab_name == 'oldWt'):
        u.oldunit_txt[i].focus_set()
    if u.cnt > 0:
        u.cnt = 0
        if(u.old_tab_name == 'desc'):
            u.oldDesc_txt[0].focus_set()
        elif(u.old_tab_name == 'oldAmt'):
            u.oldtotal_txt[2].focus_set()
        elif(u.old_tab_name == 'addDesc'):
            u.addtotal_txt[2].focus_set()

    if(tab_name == 'desc' and u.des_txt[i].get() == '')\
    or (tab_name == 'oldAmt' and u.oldtotal_txt[i].get() == '')\
    or (tab_name == 'addDesc' and u.addDesc_txt[i].get() == ''):
        u.cnt = u.cnt+1
        u.old_tab_name = tab_name
        
    if tab_name == 'number' and u.mobile_txt.get()!='':
        data = findByNumber(u.mobile_txt.get())
        if data != 0:
            setCustData(u, data)
    
    if (tab_name == 'mc' and (u.des_txt[i].get() != '' and u.wt_txt[i].get() != '' and u.mc_txt[i].get() != '' and u.unit_txt[i].get() != '')):
        calculate(u, focused_tab)
        total = findAmt(u.total)
        amt = findAmt(u.net_txt[i])
        setTotal(u,amt+total)
        
    if (tab_name == 'oldAmt' and u.oldtotal_txt[i].get()!=''):
        total = findAmt(u.total)
        amt = findAmt(u.oldtotal_txt[i])
        if(amt < total):
            setTotal(u,total-amt)
        