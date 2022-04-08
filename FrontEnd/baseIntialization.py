from datetime import datetime
from tkinter import *

class UiFields:
    mobile:      Label
    mobile_txt:  Entry
    name:        Label
    name_txt:    Entry
    address:     Label
    address_txt: Entry
    addhar:      Label
    addhar_txt:  Entry
    bill:        Label
    bill_txt:    int
    date_label:  Label
    
    siLabel:     Label
    si_txt=      []
    desLabel:    Label
    des_txt =   []
    pcsLabel:    Label
    pcs_txt =   []
    wtLabel:     Label
    wt_txt =    []
    unitLabel:   Label
    unit_txt =  []
    mcLabel:     Label
    mc_txt =    []
    cgstLabel:   Label
    cgst_txt =  []
    sgstLabel:   Label
    sgst_txt =  []
    gstAmtLabel: Label
    gstAmt_txt= []
    netLabel:    Label
    net_txt  =  []
    
    oldSi:       Label
    oldSi_txt=  []
    oldDescL:    Label
    oldDesc_txt=[]
    oldweLabel:  Label
    oldwe_txt = []
    oldunitLabel:Label
    oldunit_txt=[]
    oldtotalLabel:Label
    oldtotal_txt=[]
    
    addSi :       Label
    addSi_txt =  []
    addDescL:     Label
    addDesc_txt =[]
    addtotalLabel:Label
    addtotal_txt=[]
    
    mode_l:       OptionMenu
    mode =       "cash"
    charge_l:     Label
    charge =     0.0
    
    total_l:      Label
    total =      0.0
    
    newBtn:       Button
    printBtn:     Button
    generateBtn:  Button
    findBtn:      Button
    # bg_color = "#FFE6BC"
    bg_color = "#CEAB93"
    background_color = bg_color
    gold_rate = 0
    cnt = 0
    old_tab_name = "old"
    saveLocation = 'test.xlsx'
    entry_correct_color = "#00C897"
    entry_wrong_color = "#FF1818"
    border_size = 2
    # green = '009966'#'064635'
    green = '064635'
    red = 'C85C5C'
    blue = '041C32'
    change_gold_rate:Button
    old_gold_rate = 0.0
    
    #find bill
    billing_date_label : Label
    billing_date : Entry
    
    billing_no_label:       Entry
    billing_no:       Entry
    
    billing_ph_no_label:    Entry
    billing_ph_no:    Entry
    customer_id = 0
    bill_txt_entry: Entry
    
    entry_list = []
    entryCount = 0

    gstDateFrom_label:Label
    gstDateTo_label : Label
    gstDateFrom:Entry    
    gstDateTo : Entry
    gstBtn:Button
    gstFind:Button

    clicked = ""
    total_before_charge = 0.0
    findgoldBtn : Button
    grFindDate:datetime
    grRateOnDate = 0.0
    # BASEDIR = 'D:Shop\\Shop\\'
    BASEDIR_BILL = ''
    BASEDIR_GST = ''
    charge_amt = 0.0
    #                0 1 2 3 4 5 6 7 8
    old_net_total = [0,0,0,0,0,0,0,0,0]
    old_old_total = [0,0,0]
    old_add_total = [0,0,0]
    total_taxable_amt = []
     
    cal1 = datetime.now()
    cal2 = datetime.now()

    email_from_address = ""
    email_to_address = ""
    email_from_pass = ""
    
    config_label = []
    config_entry = []
    editBtn = []
    
    newConfig_key: Entry
    newConfig_value:Entry
    newConfig_btn : Button
    addConfig_btn:Button
    config_btn : Button
    
    bill_generated = False
    credit_card_charge = 0.0
    debit_card_charge = 0.0
