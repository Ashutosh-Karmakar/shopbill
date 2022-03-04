from baseIntialization import UiFields

def focusedTab(focused_tab):
    if(focused_tab == '.!entry'):
        return 'number'
    if(focused_tab == '.!labelframe.!entry4' or focused_tab == '.!labelframe.!entry13' or focused_tab == '.!labelframe.!entry22' or focused_tab == '.!labelframe.!entry31' or focused_tab == '.!labelframe.!entry40' or focused_tab == '.!labelframe.!entry49' or focused_tab == '.!labelframe.!entry58' or focused_tab == '.!labelframe.!entry67'):
        return 'mc'
    if(focused_tab == '.!labelframe.!entry' or focused_tab == '.!labelframe.!entry10' or focused_tab == '.!labelframe.!entry19' or focused_tab == '.!labelframe.!entry28' or focused_tab == '.!labelframe.!entry37' or focused_tab == '.!labelframe.!entry46' or focused_tab == '.!labelframe.!entry55' or focused_tab == '.!labelframe.!entry64' or focused_tab == '.!labelframe.!entry73'):
        return 'desc'
    if(focused_tab == '.!labelframe2.!entry' or focused_tab == '.!labelframe2.!entry5' or focused_tab == '.!labelframe2.!entry9'):
        return 'oldDesc'
    if(focused_tab == '.!labelframe3.!entry' or focused_tab == '.!labelframe3.!entry3' or focused_tab == '.!labelframe3.!entry5'):
        return 'addDesc'
    
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
    
