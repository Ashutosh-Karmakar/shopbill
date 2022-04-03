import os
from tkinter import *
from baseIntialization import UiFields
from database import findBillNumber, findByNumber

def check_clicked_tab(u:UiFields):
    if u.entryCount == 0:
        u.mobile_txt.configure(highlightcolor= u.entry_wrong_color)
        u.mobile_txt.focus()
        return 1
    if u.entryCount==1:
        u.name_txt.configure(highlightcolor= u.entry_wrong_color)
        u.name_txt.focus()
        return 1
    if u.entryCount == 6 or u.entryCount == 9 or u.entryCount == 12 or u.entryCount == 15 or u.entryCount == 18 or u.entryCount == 21 or u.entryCount == 24 or u.entryCount == 27 or u.entryCount == 30:
        u.entry_list[u.entryCount].configure(highlightcolor= u.entry_wrong_color)
        u.entry_list[u.entryCount].focus()
        return 1
    if(u.entryCount == 32 or u.entryCount == 34 or u.entryCount == 36):
        u.entry_list[u.entryCount].configure(highlightcolor= u.entry_wrong_color)
        u.entry_list[u.entryCount].focus()
        return 1
    if(u.entryCount == 37 or u.entryCount == 38 or u.entryCount == 39):
        u.entry_list[u.entryCount].configure(highlightcolor= u.entry_wrong_color)
        u.entry_list[u.entryCount].focus()
        return 1

def clicked_tab(focused_top):
    if focused_top == '.!entry':
        return 0 
    if focused_top == '.!entry2':
        return 1 
    if focused_top == '.!entry3':
        return 2 
    if focused_top == '.!entry4':
        return 3 
    if focused_top == '.!labelframe.!entry':
        return 4 
    if focused_top == '.!labelframe.!entry2':
        return 5 
    if focused_top == '.!labelframe.!entry3':
        return 6 
    if focused_top == '.!labelframe.!entry9':
        return 7 
    if focused_top == '.!labelframe.!entry10':
        return 8 
    if focused_top == '.!labelframe.!entry11':
        return 9 
    if focused_top == '.!labelframe.!entry17':
        return 10 
    if focused_top == '.!labelframe.!entry18':
        return 11
    if focused_top == '.!labelframe.!entry19':
        return 12 
    if focused_top == '.!labelframe.!entry25':
        return 13 
    if focused_top == '.!labelframe.!entry26':
        return 14 
    if focused_top == '.!labelframe.!entry27':
        return 15 
    if focused_top == '.!labelframe.!entry33':
        return 16
    if focused_top == '.!labelframe.!entry34':
        return 17 
    if focused_top == '.!labelframe.!entry35':
        return 18
    if focused_top == '.!labelframe.!entry41':
        return 19
    if focused_top == '.!labelframe.!entry42':
        return 20
    if focused_top == '.!labelframe.!entry43':
        return 21
    if focused_top == '.!labelframe.!entry49':
        return 22
    if focused_top == '.!labelframe.!entry50':
        return 23
    if focused_top == '.!labelframe.!entry51':
        return 24
    if focused_top == '.!labelframe.!entry57':
        return 25
    if focused_top == '.!labelframe.!entry58':
        return 26 
    if focused_top == '.!labelframe.!entry59':
        return 27 
    if focused_top == '.!labelframe.!entry65':
        return 28 
    if focused_top == '.!labelframe.!entry66':
        return 29 
    if focused_top == '.!labelframe.!entry67':
        return 30 
    if focused_top == '.!labelframe2.!entry2':
        return 31 
    if focused_top == '.!labelframe2.!entry4':
        return 32
    if focused_top == '.!labelframe2.!entry6':
        return 33
    if focused_top == '.!labelframe2.!entry8':
        return 34
    if focused_top == '.!labelframe2.!entry10':
        return 35
    if focused_top == '.!labelframe2.!entry12':
        return 36
    if focused_top == '.!labelframe3.!entry2':
        return 37
    if focused_top == '.!labelframe3.!entry4':
        return 38
    if focused_top == '.!labelframe3.!entry6':
        return 39
    if focused_top == '.!labelframe4.!entry':
        return 40
    if focused_top == '.!labelframe4.!entry2':
        return 41

def focusedTab(focused_tab):
    if(focused_tab == '.!entry4'):
        return 'addhar'
    if(focused_tab == '.!entry'):
        return 'number'
    if(focused_tab == '.!entry2'):
        return 'name'
    if(focused_tab == '.!labelframe.!entry' or focused_tab == '.!labelframe.!entry9' or focused_tab == '.!labelframe.!entry17' or focused_tab == '.!labelframe.!entry25' or focused_tab == '.!labelframe.!entry33' or focused_tab == '.!labelframe.!entry41' or focused_tab == '.!labelframe.!entry49' or focused_tab == '.!labelframe.!entry57' or focused_tab == '.!labelframe.!entry65'):
        return 'desc'
    if(focused_tab == '.!labelframe.!entry2' or focused_tab == '.!labelframe.!entry10' or focused_tab == '.!labelframe.!entry18' or focused_tab == '.!labelframe.!entry26' or focused_tab == '.!labelframe.!entry34' or focused_tab == '.!labelframe.!entry42' or focused_tab == '.!labelframe.!entry50' or focused_tab == '.!labelframe.!entry58' or focused_tab == '.!labelframe.!entry66'):
        return 'wt'
    if focused_tab == '.!labelframe.!entry3' or focused_tab == '.!labelframe.!entry11' or focused_tab == '.!labelframe.!entry19' or focused_tab == '.!labelframe.!entry27' or focused_tab == '.!labelframe.!entry35' or focused_tab == '.!labelframe.!entry43' or focused_tab == '.!labelframe.!entry51' or focused_tab == '.!labelframe.!entry59' or focused_tab == '.!labelframe.!entry67':
        return 'newTotal'
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
    if(focused_tab == '.!labelframe4.!entry2'):
        return 'charges'
    if(focused_tab == '.!labelframe4.!entry3'):
        return 'total'
    
def tabNumber(focused_tab):
    #desc entry:
    if focused_tab == '.!labelframe.!entry':
        return 0
    if focused_tab == '.!labelframe.!entry9':
        return 1
    if focused_tab == '.!labelframe.!entry17':
        return 2
    if focused_tab == '.!labelframe.!entry25':
        return 3
    if focused_tab == '.!labelframe.!entry33':
        return 4
    if focused_tab == '.!labelframe.!entry41':
        return 5
    if focused_tab == '.!labelframe.!entry49':
        return 6
    if focused_tab == '.!labelframe.!entry57':
        return 7
    if focused_tab == '.!labelframe.!entry65':
        return 8
    
    #wt entry
    if focused_tab == '.!labelframe.!entry2':
        return 0
    if focused_tab == '.!labelframe.!entry10':
        return 1
    if focused_tab == '.!labelframe.!entry18':
        return 2
    if focused_tab == '.!labelframe.!entry26': 
        return 3
    if focused_tab == '.!labelframe.!entry34':
        return 4
    if focused_tab == '.!labelframe.!entry42':
        return 5
    if focused_tab == '.!labelframe.!entry50': 
        return 6
    if focused_tab == '.!labelframe.!entry58':
        return 7
    if focused_tab == '.!labelframe.!entry66':
        return 8
    
    # new total 
    if focused_tab == '.!labelframe.!entry3':
        return 0
    if focused_tab == '.!labelframe.!entry11':
        return 1
    if focused_tab == '.!labelframe.!entry19':
        return 2
    if focused_tab == '.!labelframe.!entry27':
        return 3
    if focused_tab == '.!labelframe.!entry35':
        return 4
    if focused_tab == '.!labelframe.!entry43':
        return 5
    if focused_tab == '.!labelframe.!entry51':
        return 6
    if focused_tab == '.!labelframe.!entry59':
        return 7
    if focused_tab == '.!labelframe.!entry67':
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
    
    #add amt : 
    if focused_tab == '.!labelframe3.!entry2':
        return 0
    if focused_tab == '.!labelframe3.!entry4':
        return 1
    if focused_tab == '.!labelframe3.!entry6':
        return 2


def setCustData(u:UiFields, data):
    print('cust Data',data)
    u.name_txt.delete(0,END)
    u.address_txt.delete(0,END)
    u.addhar_txt.delete(0,END)
    u.name_txt.insert(0,data[1])
    u.address_txt.insert(0,data[3])
    u.addhar_txt.insert(0,data[4])
    u.addhar_txt.focus_set()
    u.entryCount = 4


def calculate(u:UiFields, focused_tab):
    try:
        i = tabNumber(focused_tab)
        wt = float(u.wt_txt[i].get())
        amt = float(u.net_txt[i].get())
        gr = u.gold_rate
        cost = (amt)*(100/103)
        u.total_taxable_amt.append(cost)    
        if(cost < amt):
            cgst = amt - cost
        else:
            cgst = 0
        print('cost - ',cost)
        print('wt - ',wt)
    
    
        mc = (cost/wt)-gr
        mc = round(mc,2)
    
    
        cgst = round(cgst/2,2)
        gstamt = cgst*2
        
        
        
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
        
        if(mc < 0):
            print("There is a error in calculation mc")
            u.entryCount = 6+i*3
            u.wt_txt[i].focus()
            u.net_txt[i].configure(highlightcolor= u.entry_wrong_color)
            # u.total_before_charge = u.total_before_charge - float(u.net_txt[i].get())
            return 1
            print(i)
            # u.total.delete(0,END)
            # u.total.insert(0,0.0)
    except Exception:
        print("there is a error in calculation")
        u.des_txt[i].focus_set()
        

def set_total_after_charges(u:UiFields):
    try:
        if(u.total.get()!='' and u.charge.get()!=''):
            tot = float(u.total_before_charge)
            cha = float(u.charge_amt)
            tot = round(tot + tot*(cha/100),2)
            u.total.delete(0,END)
            u.total.insert(0,tot)
        elif(u.total.get()!=''):
            tot = float(u.total_before_charge)
            cha = float(u.charge_amt)
            tot = round(tot - tot*(cha/100),2)
            u.total.delete(0,END)
            u.total.insert(0,u.total_before_charge)
            u.charge_amt = 0.0
    except Exception as e:
        print("There is a exception : {0}".format(e))
    

def findAmt(amt):
    try:
        return float(amt.get())
    except Exception as e:
        print("There is a exception : {0}".format(e))
        return 0


def setTotal(u:UiFields,amt):
    try:
        if(u.charge.get()!=''):
            amt = round(amt + (amt*(float(u.charge_amt)/100)),2)
        u.total.delete(0,END)
        u.total.insert(0,(amt))
    except Exception as e:
        print("There is a exception : {0}".format(e))
    
    
def checkField(focused_tab,u:UiFields):
    tab_name = focusedTab(focused_tab)
    i = tabNumber(focused_tab)
    
    #name
    if(tab_name == 'name'):
        if(u.name_txt.get()==''):
            return True
        return False
    
    #number
    if(tab_name == 'number'):
        if(u.mobile_txt.get()==''):
            return True
        if(len(u.mobile_txt.get())!=10):
            return True
        for ch in u.mobile_txt.get():
            if ch == '.':
                return True
            elif ch.isnumeric()==False:
                return True 
        return False
       
    #wt field and net total:
    if(tab_name == 'wt'):
        if(u.wt_txt[i].get()!='' and (u.wt_txt[i].get()).isalpha()):
            return True
        if(len(u.wt_txt[i].get())==1 and (ord(str(u.wt_txt[i].get()))<48 or ord(str(u.wt_txt[i].get()))>57)):
            return True
        if(len(u.wt_txt[i].get()) > 1):
            ct = 0
            for ch in u.wt_txt[i].get():
                if ch == '.':
                    ct+=1
                elif ch!= '.' and ch.isnumeric()==False:
                    return True
                if(ct >= 2):
                    return True
        return False
        
    elif(tab_name == 'newTotal'):
        if(u.net_txt[i].get()!='' and (u.net_txt[i].get()).isalpha()):
            return True
        if(len(u.net_txt[i].get())==1 and (ord(str(u.net_txt[i].get()))<48 or ord(str(u.net_txt[i].get()))>57)):
            return True
        if(len(u.net_txt[i].get()) > 1):
            ct = 0
            for ch in u.net_txt[i].get():
                if(ct >= 2):
                    return True
                elif ch == '.':
                    ct+=1
                elif ch!= '.' and ch.isnumeric()==False:
                    return True
        return False
    
    elif(tab_name == 'oldWt'):
        if(u.oldwe_txt[i].get()!='' and (u.oldwe_txt[i].get()).isalpha()):
            return True
        if(len(u.oldwe_txt[i].get())==1 and (ord(str(u.oldwe_txt[i].get()))<48 or ord(str(u.oldwe_txt[i].get()))>57)):
            return True
        if(len(u.oldwe_txt[i].get()) > 1):
            ct = 0
            for ch in u.oldwe_txt[i].get():
                if(ct >= 2):
                    return True
                elif ch == '.':
                    ct+=1
                elif ch!= '.' and ch.isnumeric()==False:
                    return True
        return False
        
    elif(tab_name == 'oldAmt'):
        if(u.oldtotal_txt[i].get()!='' and (u.oldtotal_txt[i].get()).isalpha()):
            return True
        if(len(u.oldtotal_txt[i].get())==1 and (ord(str(u.oldtotal_txt[i].get()))<48 or ord(str(u.oldtotal_txt[i].get()))>57)):
            return True
        if(len(u.oldtotal_txt[i].get()) > 1):
            ct = 0
            for ch in u.oldtotal_txt[i].get():
                if(ct >= 2):
                    return True
                elif ch == '.':
                    ct+=1
                elif ch!= '.' and ch.isnumeric()==False:
                    return True
        return False
    
    elif(tab_name == 'addAmt'):
        if(u.addtotal_txt[i].get()!='' and (u.addtotal_txt[i].get()).isalpha()):
            return True
        if(len(u.addtotal_txt[i].get())==1 and (ord(str(u.addtotal_txt[i].get()))<48 or ord(str(u.addtotal_txt[i].get()))>57)):
            return True
        if(len(u.addtotal_txt[i].get()) > 1):
            ct = 0
            for ch in u.addtotal_txt[i].get():
                if(ct >= 2):
                    return True
                elif ch == '.':
                    ct+=1
                elif ch!= '.' and ch.isnumeric()==False:
                    return True
        return False
    
    elif(tab_name == 'addhar'):
        if(u.addhar_txt.get() !='' and (u.addhar_txt.get()).isnumeric()==False):
            return True
    
    
def enterOperation(focused_tab, u:UiFields):
    tab_name = focusedTab(focused_tab)
    i = tabNumber(focused_tab)
    
    if(checkField(focused_tab,u)):
        if(tab_name == 'name'):
            u.mobile_txt.focus_set()
            u.name_txt.configure(highlightcolor= u.entry_wrong_color)
            return 
        elif(tab_name == 'number'):
            u.mobile_txt.focus_set()
            u.mobile_txt.configure(highlightcolor= u.entry_wrong_color)
            return 1
        elif(tab_name == 'wt'):
            u.des_txt[i].focus_set()
            u.wt_txt[i].configure(highlightcolor= u.entry_wrong_color)
            return 
            
        elif(tab_name == 'newTotal'):
            u.wt_txt[i].focus_set()
            u.net_txt[i].configure(highlightcolor= u.entry_wrong_color)
            return
            
        elif(tab_name == 'oldWt'):
            u.oldDesc_txt[i].focus_set()
            u.oldwe_txt[i].configure(highlightcolor= u.entry_wrong_color)
            return 
            
        elif(tab_name == 'oldAmt'):
            u.oldwe_txt[i].focus_set()
            u.oldtotal_txt[i].configure(highlightcolor= u.entry_wrong_color)
            return 
            
        elif(tab_name == 'addAmt'):
            u.addDesc_txt[i].focus_set()
            u.addtotal_txt[i].configure(highlightcolor= u.entry_wrong_color)
            return 
            
        elif(tab_name == 'addhar'):
            u.address_txt.focus_set()
            u.addhar_txt.configure(highlightcolor= u.entry_wrong_color)
            return 
    
    u.entry_list[u.entryCount].configure(highlightcolor= u.entry_correct_color)
    if(u.entryCount>=42):
        u.entryCount=42
        print("hello")  
        u.entry_list[u.entryCount].focus()
        
    else:
        u.entryCount+=1
    
    print('Entry Count :-',u.entryCount)
    
    if(tab_name == 'name' and u.name_txt.get()!=''):
        name = u.name_txt.get()
        u.name_txt.delete(0,END)
        u.name_txt.insert(0,name.capitalize())
    
    if(tab_name == 'desc' and u.des_txt[i].get()!=''):
        des = u.des_txt[i].get()
        u.des_txt[i].delete(0,END)
        u.des_txt[i].insert(0,des.capitalize())
    
    
    
    
    if u.cnt > 0:
        u.cnt = 0
        if(u.old_tab_name == 'desc' and u.des_txt[i].get()==''):
            u.oldDesc_txt[0].focus_set()
            u.entryCount = 31

        if(u.old_tab_name == 'oldAmt'):
            u.oldtotal_txt[2].focus_set()
            u.entryCount = 38
        # elif(u.old_tab_name == 'addDesc'):
            # u.addtotal_txt[2].focus_set()
            # u.entryCount = 42

    if(tab_name == 'desc' and u.des_txt[i].get() == '')\
    or (tab_name == 'oldAmt' and u.oldtotal_txt[i].get() == '')\
    or (tab_name == 'addAmt' and u.addtotal_txt[i].get() == ''):
        u.cnt = u.cnt+1
        u.old_tab_name = tab_name
        
    if tab_name == 'number' and u.mobile_txt.get()!='':
        data = findByNumber(u.mobile_txt.get())
        if data != 0:
            setCustData(u, data)
    
    if (tab_name == 'newTotal' and (u.des_txt[i].get() != '' and u.wt_txt[i].get() != '' and  u.net_txt[i].get()!='')):
        try:
            chec = calculate(u, focused_tab)
            if(chec == 1):
                return
            total = float(u.total_before_charge)
            amt = float(u.net_txt[i].get())
            u.total_before_charge = amt+total
            if(u.old_net_total[i] == amt):
                u.total_before_charge = total
                return
            elif(u.old_net_total[i] != 0):
                u.total_before_charge = u.total_before_charge - u.old_net_total[i]
            
            setTotal(u,round(u.total_before_charge,2))
            u.old_net_total[i] = amt
        except Exception as e:
            print("There is a exception : {0}".format(e))
        
    if (tab_name == 'oldAmt' and u.oldtotal_txt[i].get()!='' and checkField(focused_tab,u)==False):
        total = u.total_before_charge
        amt = findAmt(u.oldtotal_txt[i])
        u.total_before_charge = total-amt
        if(u.old_old_total[i] == amt):
            u.total_before_charge = total
            return
        elif(u.old_old_total[i] != 0):
            u.total_before_charge = u.total_before_charge + u.old_old_total[i]
        
        setTotal(u,u.total_before_charge)
        u.old_old_total[i] = amt
            
    if (tab_name == 'addAmt' and u.addtotal_txt[i].get()!='' and checkField(focused_tab,u)==False):
        total = u.total_before_charge
        amt = findAmt(u.addtotal_txt[i])
        u.total_before_charge = total+amt
        if(u.old_add_total[i] == amt):
            u.total_before_charge = total
            return
        elif(u.old_add_total[i] != 0):
            print(u.old_add_total[i])
            u.total_before_charge = u.total_before_charge - u.old_add_total[i]
        setTotal(u,u.total_before_charge)
        u.old_add_total[i] = amt
            
            
            
            
            
            
            
            

        
EMPTY = ''
 
X = [EMPTY, 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ',
    'Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ',
    'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']

Y = [EMPTY, EMPTY, 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ',
    'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']

  
# Function to convert a single-digit or two-digit number into words
def convertToDigit(n, suffix):
 
    # if `n` is zero
    if n == 0:
        return EMPTY
 
    # split `n` if it is more than 19
    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix
 
 
# Function to convert a given number (max 9-digits) into words
def convert(n):
    # add digits at ten million and hundred million place
    result = convertToDigit((n // 1000000000) % 100, 'Billion, ')
 
    # add digits at ten million and hundred million place
    result += convertToDigit((n // 10000000) % 100, 'Crore, ')
 
    # add digits at hundred thousand and one million place
    result += convertToDigit(((n // 100000) % 100), 'Lakh, ')
 
    # add digits at thousand and tens thousand place
    result += convertToDigit(((n // 1000) % 100), 'Thousand, ')
 
    # add digit at hundred place
    result += convertToDigit(((n // 100) % 10), 'Hundred ')
 
    if n > 100 and n % 100:
        result += 'and '
 
    # add digits at ones and tens place
    result += convertToDigit((n % 100), '')
 
    return result.strip().rstrip(',').replace(', and', ' and')
     
     
     
def printBill():
    bill_no = findBillNumber()
    os.startfile('test.xlsx','print') 
     
     
     
     
     
def newBill(u:UiFields):
    u.bill_generated = False
    u.entryCount=0
    u.charge_amt = 0.0
    u.mobile_txt.delete(0,END)
    u.mobile_txt.configure(highlightcolor= u.entry_correct_color)
    u.mobile_txt.focus()

    u.name_txt.delete(0,END)
    u.name_txt.configure(highlightcolor= u.entry_correct_color)

    u.address_txt.delete(0,END)
    u.address_txt.configure(highlightcolor= u.entry_correct_color)

    u.addhar_txt.delete(0,END)
    u.addhar_txt.configure(highlightcolor= u.entry_correct_color)

    u.bill_txt = findBillNumber()
    u.bill_txt_entry.config(state='normal')
    u.bill_txt_entry.delete(0,END)
    u.bill_txt_entry.insert(0,u.bill_txt)
    u.bill_txt_entry.config(state=DISABLED)

    # u.date_label=Label(window, text=daten.strftime("%d-%b-%y - (%A)"), font=('times new rommon',labelfont),bg=u.bg_color)
    # u.date_label.grid(row=1,column=30)


    u.total_before_charge = 0.0
    u.old_net_total = [0,0,0,0,0,0,0,0,0]
    u.total_taxable_amt = []
    # ========================================new Gold==============================================

    for i in range(0,9):
        if(u.des_txt[i].get()!=''):
            u.des_txt[i].delete(0,END)
            u.des_txt[i].configure(highlightcolor= u.entry_correct_color)
            
            u.wt_txt[i].delete(0,END)
            u.wt_txt[i].configure(highlightcolor= u.entry_correct_color)

            u.net_txt[i].delete(0,END)
            u.net_txt[i].configure(highlightcolor= u.entry_correct_color)
            
            u.mc_txt[i].config(state='normal')
            u.mc_txt[i].delete(0,END)
            u.mc_txt[i].configure(highlightcolor= u.entry_correct_color)
            u.mc_txt[i].config(state=DISABLED)
            
            # u.unit_txt[i].config(state='normal')
            # u.unit_txt[i].delete(0,END)
            # u.unit_txt[i].configure(highlightcolor= u.entry_correct_color)
            # u.unit_txt[i].config(state=DISABLED)
            
            u.cgst_txt[i].config(state='normal')
            u.cgst_txt[i].delete(0,END)
            u.cgst_txt[i].configure(highlightcolor= u.entry_correct_color)
            u.cgst_txt[i].config(state=DISABLED)
            
            u.sgst_txt[i].config(state='normal')
            u.sgst_txt[i].delete(0,END)
            u.sgst_txt[i].configure(highlightcolor= u.entry_correct_color)
            u.sgst_txt[i].config(state=DISABLED)
            
            u.gstAmt_txt[i].config(state='normal')
            u.gstAmt_txt[i].delete(0,END)
            u.gstAmt_txt[i].configure(highlightcolor= u.entry_correct_color)
            u.gstAmt_txt[i].config(state=DISABLED)
            
    # ==================================old gold=====================================================

    for i in range(0,3): 
        
        u.oldDesc_txt[i].delete(0,END)
        u.oldDesc_txt[i].configure(highlightcolor= u.entry_correct_color)
        u.oldDesc_txt[i].insert(0,'Old Gold')
        
        u.oldwe_txt[i].delete(0,END)
        u.oldwe_txt[i].configure(highlightcolor= u.entry_correct_color)
        
        u.oldtotal_txt[i].delete(0,END)
        u.oldtotal_txt[i].configure(highlightcolor= u.entry_correct_color)


    #===========================================addition or deduction===============================
    for i in range(0,3):
        
        u.addDesc_txt[i].delete(0,END)
        u.addDesc_txt[i].configure(highlightcolor= u.entry_correct_color)

        u.addtotal_txt[i].delete(0,END)
        u.addtotal_txt[i].configure(highlightcolor= u.entry_correct_color)

    #=================================mode of payment and total==============================
    u.clicked.set('Cash')
    u.charge.delete(0,END)
    
    
    u.total.delete(0,END)
    u.total.configure(highlightcolor= u.entry_correct_color)
    u.total.insert(0,0)
