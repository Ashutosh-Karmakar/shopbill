import os
import tkinter
import win32api
import win32print
from tkinter import *
import tkinter
import time

def selectPrinter():
    index = 0
    Printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 2)
    # print("[Print List]")
    # print("Current Printer Name: " + win32print.GetDefaultPrinter())
    # print("0. Close")
    # for Printer in Printers:   
        # index += 1              
        # print(str(index) + ". " + Printer['pPrinterName'])

    # number = input("Select Printer Number: ")
    # if len(Printers) >= int(number) and  int(number) > 0:  
    #     win32print.SetDefaultPrinter(Printers[int(number)-1]['pPrinterName'])
    i = 0
    for printer in Printers:
        if(printer['pPrinterName'] == 'HP Ink Tank 310 series'):
            win32print.SetDefaultPrinter(Printers[i]['pPrinterName'])
        i+=1
        
    print("Setting Printer: " + win32print.GetDefaultPrinter())
    return  win32print.GetDefaultPrinter()

def printBill(filename):
    printerName = selectPrinter()
    print("Hello")
    # filenames = os.listdir(dirname)
    # select = input("Are you sure that you want to print the whole Excel file ?(y or n): ")
    # if select == 'y' or select == 'Y':        
    # for filename in filenames:
    os.system("start EXCEL.EXE")# test.xlsx")
    time.sleep(1)
    # filename = 'test.xlsx'
    # filename = 'test.xlsx'#os.path.join(dirname, filename)
    
    # ext = os.path.splitext(full_filename)[-1]        
    # if ext == '.xlsm' or ext == '.xlsx':
    # print('"' + filename + '"' + " printin!")
    win32api.ShellExecute(0, 'printto', filename, '"' + printerName + '"', None,  0)
                         
# if __name__ == "__main__":    
#     printerName = selectPrinter()
#     os.system('cls')
   
#     search(os.getcwd(), printerName) 
#     os.system("Pause")



def printDialog():
    window2 = tkinter.Tk()
    p=Label(window2, text='Printing .....', font=('times new rommon',11),bg='yellow')
    p.pack()
    window2.after(6000,lambda:window2.destroy())
    window2.mainloop()
