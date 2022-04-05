from datetime import datetime
from tkinter import *
from tkcalendar import Calendar
from baseIntialization import UiFields
from database import findGRDate

def findGoldRateOnDate(u:UiFields):
    root = Tk()
    root.configure(bg=u.background_color)
    root.title("Gold Rate")
    root.geometry("400x600")
    cur_date = datetime.now()

    cal = Calendar(root, selectmode = 'day',
                year = cur_date.year, month = cur_date.month,
                day = cur_date.day)
    
    cal.pack(pady = 20)
    
    def grad_date():
        date.config(text = "Selected Date is: " + cal.get_date())
        datefind = ''
        result = cal.get_date()
        result = result.split('/')
            
        datefind = datefind + '20' + result[2] + '-'
        if(len(result[0]) == 1):
            result[0] = '0'+result[0]
        datefind = datefind + result[0] + '-'
        
        if(len(result[1]) == 1):
            result[1] = '0'+result[1]
        datefind = datefind + result[1]
        
        
        u.grFindDate = datefind
        print(u.grFindDate)
        u.grFindDate = datetime.strptime(cal.get_date(), '%m/%d/%y')
        i = findGRDate(u)
        
        goldRate.config(text = u.grRateOnDate)
        goldRate.config(font=("times new rommon", 11))
        
    Button(root, text = "Get Date",
        command = grad_date).pack(pady = 20)
    
    date = Label(root, text = "")
    date.pack(pady = 20)

    goldRate = Label(root, text = "")
    goldRate.pack(pady=20)
    
    root.mainloop()