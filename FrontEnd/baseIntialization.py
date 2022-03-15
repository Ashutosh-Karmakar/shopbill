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
    bg_color = "#FFE6BC"
    gold_rate = 0.0
    cnt = 0
    old_tab_name = "old"
    saveLocation = 'test.xlsx'
    entry_correct_color = "#00C897"
    entry_wrong_color = "#FF1818"
    border_size = 2
    background_color = '#FFE6BC'
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
    BASEDIR = 'D:Shop\Shop\FrontEnd'
