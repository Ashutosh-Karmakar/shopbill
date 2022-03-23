#desktop Bill
from logging import getLoggerClass
import openpyxl
from openpyxl.styles import PatternFill,Border, Side
j = 3
wb = openpyxl.Workbook()
sh1 = wb.active
medium = Side(border_style='thin',color='FF000000')


def create(data):
    
    sh1.title = 'gst'
    
    i = 0
    global j
    sh1['A1'] = 'id'
    sh1['B1'] = 'Date'
    sh1['C1'] = 'Ornament'
    sh1['D1'] = 'Qty'
    sh1['E1'] = 'Weight'
    sh1['F1'] = 'GoldRate'
    sh1['G1'] = 'Taxable Amt'
    sh1['H1'] = 'CGST'
    sh1['I1'] = 'SGST'
    sh1['J1'] = 'Net Total'
    for k in range(1,11):
        sh1.cell(row = 1,column = k).border=Border(left=medium,bottom=medium,top=medium)
        sh1.cell(row = 2,column = k).border=Border(bottom=medium)
    sh1.cell(row=1,column=10).border=Border(right=medium,left=medium,bottom=medium,top=medium)
    for gst in data:
        for c in gst:
            if(i==9):
                sh1.cell(row = j,column = i+1).border=Border(left=medium,bottom=medium,right=medium)
            else:
                sh1.cell(row = j,column = i+1).border=Border(left=medium,bottom=medium)
            location = chr(65+i)+''+str(j)
            if(i == 1):
                sh1[location] = str(c)[0:10]
            # print(location)
            else:
                sh1[location] = c
            i+=1
        j+=1
        i = 0
        
    wb.save(filename='gst.xlsx')
    
def insertTotal(data):
    global j
    k = j
    for k in range(j,j+3):
        for i in range(6,10):
            sh1.cell(row = k,column = i+1).border=Border(left=medium,bottom=medium,right=medium,top=medium)
    
    j = j+1
    
    sh1['G'+str(j)]=data[0][0]
    sh1['H'+str(j)]=data[0][1]
    sh1['I'+str(j)]=data[0][2]
    sh1['J'+str(j)]=data[0][3]
    
    j+=1
    
    sh1['G'+str(j)]='Taxable Amt'
    sh1['H'+str(j)]='CGST'
    sh1['I'+str(j)]='SGST'
    sh1['J'+str(j)]='NetTotal'
    
    
    
    wb.save(filename='gst.xlsx')
    