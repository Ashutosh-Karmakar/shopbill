import win32print
from tkinter import *
import xlwings as xw
import xlwings.constants

def selectPrinter():
    try:
        Printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 2)
        i = 0
        for printer in Printers:
            if(printer['pPrinterName'] == 'HP Ink Tank 310 series'):
                win32print.SetDefaultPrinter(Printers[i]['pPrinterName'])
            i+=1
            
        print("Setting Printer: " + win32print.GetDefaultPrinter())
        return  win32print.GetDefaultPrinter()
    except Exception as e:
        print("There is a exception in finding printer : {0}".format(e))

def printBill(filename):
    try:
        wb=xw.Book(filename)
        sh2=wb.sheets
        sh2.api.PrintOut(From=1, To=1, Copies=1)
    except FileNotFoundError:
        print("File not found")
    