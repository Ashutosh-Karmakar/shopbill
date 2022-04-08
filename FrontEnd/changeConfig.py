from baseIntialization import UiFields
from database import findAllConfig, insertNewConfig, changeConfig
import tkinter
from tkinter import *
import sys
# c = UiFields()

i = 1

def add(c:UiFields):
    global i
    insertNewConfig(c)
    i = 0
    c.config_label = []
    c.config_entry = []
    c.newConfig_key.forget()
    c.newConfig_value.forget()
    c.addConfig_btn.forget()
    # c.newConfig_btn
    config(c)
    
# def newConfig():
#     global i
#     l = Label(window,text='Key',font=('times new rommon',11))
#     l.grid(row=i,column=1)
    
#     l = Label(window,text='Value',font=('times new rommon',11))
#     l.grid(row=i,column=2)
    
#     c.newConfig_key=Entry(window,width=30,font='arial 11',bd=2,justify=CENTER)
#     c.newConfig_key.grid(row=i+1,column=1,padx=10,pady=10)
    
#     c.newConfig_value=Entry(window,width=50,font='arial 11',bd=2,justify=CENTER)
#     c.newConfig_value.grid(row=i+1,column=2,padx=10,pady=10)
#     c.newConfig_btn.forget()

    
#     c.addConfig_btn = Button(window, text = "ADD", command= lambda:add(c),background='red')
#     c.addConfig_btn.grid(row=i+2,column=1)
    

def edit(c:UiFields,i):
    print(i)
    changeConfig(c.config_label[i-1]["text"], c.config_entry[i-1].get())

def config(c:UiFields):
    global i
    window = tkinter.Tk()
    # window.attributes('-fullscreen', True)
    window.geometry('1000x800')
    # window.configure(bg=u.background_color)
    window.title("Config")
    window.configure(bg=c.bg_color)

    
    configs = findAllConfig()
    print(configs)
    
    h1 = Label(window,text="Sino",font=('times new rommon',11),background=c.bg_color)
    h1.grid(row=0,column=0)
    
    h2 = Label(window,text="KEY",font=('times new rommon',11),width=30,background=c.bg_color)
    h2.grid(row=0,column=1)
    
    h3 = Label(window,text="CONFIG",font=('times new rommon',11),background=c.bg_color)
    h3.grid(row=0,column=2)
    
    for con in configs:
        
        s = Label(window,text=i,font=('times new rommon',11),background=c.bg_color)
        s.grid(row=i,column=0)
        l = Label(window,text=con[0],font=('times new rommon',11),background=c.bg_color)
        l.grid(row=i,column=1)
        e=Entry(window,width=50,font='arial 11',bd=2,justify=CENTER)
        e.grid(row=i,column=2,padx=10,pady=10)
        e.insert(0,con[1])
        
        btn = Button(window, text = "Edit", font='arial 12', command= lambda m=i:edit(c,m),background='#FF6B6B')
        btn.grid(row=i,column=3)


        c.config_label.append(l)
        c.config_entry.append(e)
        c.editBtn.append(btn)
        i+=1
    
    l = Label(window,text='Key',font=('times new rommon',11),background=c.bg_color)
    l.grid(row=i,column=1)
    
    l = Label(window,text='Value',font=('times new rommon',11),background=c.bg_color)
    l.grid(row=i,column=2)
    
    c.newConfig_key=Entry(window,width=30,font='arial 11',bd=2,justify=CENTER)
    c.newConfig_key.grid(row=i+1,column=1,padx=10,pady=10)
    
    c.newConfig_value=Entry(window,width=50,font='arial 11',bd=2,justify=CENTER)
    c.newConfig_value.grid(row=i+1,column=2,padx=10,pady=10)
  
    
    c.addConfig_btn = Button(window, text = "ADD", font='arial 15', command= lambda:add(c),background='#FF6B6B')
    c.addConfig_btn.grid(row=i+2,column=1)

    window.mainloop()

# config()
