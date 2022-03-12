import tkinter as tk
from tkinter import simpledialog
from tkinter import *
from baseIntialization import UiFields

def changeGoldRate(u:UiFields):
    gr = tk.Tk()
    gr.withdraw()
    gold_rate = simpledialog.askstring(title="Gold Rate", prompt="Gold Rate?:")
    u.gold_rate = int(gold_rate)
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
    
        