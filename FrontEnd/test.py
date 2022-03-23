#desktop bill
from printer import printBill
import os
import xlwings as xw
import xlwings.constants
pp = os.getcwd()
pathh = os.path.join(pp,'test.xlsx')



wb=xw.Book(pathh)
sh2=wb.sheets
sh2.api.PrintOut(From=1, To=1, Copies=1)
# wb.save(r'C:\Users\User\Desktop\2.xlsx') #file to save changes
# os.system("start EXCEL.EXE test.xlsx")

# os.startfile('test.xlsx','print') 



# printBill('test.xlsx')

