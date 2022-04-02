import win32print
from tkinter import *
import tkinter
import xlwings as xw
import xlwings.constants

def selectPrinter():
    Printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 2)
    i = 0
    for printer in Printers:
        if(printer['pPrinterName'] == 'HP Ink Tank 310 series'):
            win32print.SetDefaultPrinter(Printers[i]['pPrinterName'])
        i+=1
        
    print("Setting Printer: " + win32print.GetDefaultPrinter())
    return  win32print.GetDefaultPrinter()

def printBill(filename):
    wb=xw.Book(filename)
    sh2=wb.sheets
    sh2.api.PrintOut(From=1, To=1, Copies=1)
    