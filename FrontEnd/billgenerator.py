from re import U
import openpyxl
from openpyxl.styles import PatternFill,Border, Side, Alignment, Protection, Font, borders,fills
import datetime
from database import saveBillLocation, saveCustomerData, saveGstData
from baseIntialization import UiFields
import os
from backend import convert, printBill

def generateBill(u : UiFields):
    wb = openpyxl.Workbook()
    sh1 = wb.active
    sh1.title = 'bill'
    daten = datetime.datetime.now()
# ====================================================shop details==================================================================
    sh1['E1'] = "GIRIDHARI JEWELLERY"
    sh1['E1'].font = Font(name='times new rommon',size=25,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')

    sh1['D2'] = "Badheibanka Chawk, Old Town, Bhubaneswar, Mob.: 9090280083,9861230757"
    sh1['D2'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='064635')

    sh1['F3'] = "916 GOLD AND SILVER ORNAMENT"
    sh1['F3'].font = Font(name='times new rommon',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')
    
    sh1['G4'] = "Invoice"
    sh1['G4'].font = Font(name='times new rommon',size=14,bold=True,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')

# ======================================================customer details==================================================
    
    sh1['A5'] = 'GSTIN - 21AYRPK4931F1ZH'
    sh1['A5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)

    sh1['H5'] = "SI. No.: "
    sh1['H5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['I5'] = u.bill_txt
    sh1['I5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)

    sh1['K5'] = 'Date: '+ daten.strftime("%d-%b-%y - (%A)")
    sh1['K5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)

    sh1['A6'] = "Name: "
    sh1['A6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['B6'] = u.name_txt.get()
    sh1['B6'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)

    sh1['F6'] = 'Mobile No.'
    sh1['F6'].font = Font(name='times new rommon',size=11,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['G6'] = '  '+ u.mobile_txt.get()
    sh1['G6'].font = Font(name='arial',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)

    sh1['I6'] = 'Addhar No.'
    sh1['I6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['J6'] = u.addhar_txt.get()
    sh1['J6'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)

    sh1['M6'] = 'Bill No.'
    sh1['M6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['N6'] = u.bill_txt
    sh1['N6'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)

    sh1['F7'] = "Gold Rate: "
    sh1['F7'].font = Font(name='times new rommon',size=15,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['H7'] = "45000"
    sh1['H7'].font = Font(name='arial',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)
    
    
# ===========================================product details======================================================================
    
    sh1['A8'] = 'Si.no.'
    sh1['A8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['B8'] = 'Description Of Goods'
    sh1['B8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['E8'] = 'HSN'
    sh1['E8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['E9'] = 'SAC'
    sh1['E9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    
    sh1['F8'] = 'Weight'
    sh1['F8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)

    sh1['G8'] = 'MC'
    sh1['G8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)

    sh1['H8'] = 'Unit'
    sh1['H8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['H9'] = 'Price'
    sh1['H9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)

    sh1['I8'] = 'CGST'
    sh1['I8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['I9'] = '1.5%'
    sh1['I9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)

    sh1['K8'] = 'SGST'
    sh1['K8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['K9'] = '1.5%'
    sh1['K9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)

    sh1['M8'] = 'Net'
    sh1['M8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)
    sh1['M9'] = 'Total'
    sh1['M9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.green)

    sh1['E10'] = '7113'
    sh1['E10'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

    for i in range(1,10):
        if(u.des_txt[i-1].get()!= ""):
            sh1['A'+str(i+9)] = i
            sh1['A'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

            sh1['B'+str(i+9)] = u.des_txt[i-1].get()
            sh1['B'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

            sh1['F'+str(i+9)] = float(u.wt_txt[i-1].get())
            sh1['F'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

            sh1['G'+str(i+9)] = float(u.mc_txt[i-1].get())
            sh1['G'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

            sh1['H'+str(i+9)] = float(u.unit_txt[i-1].get())
            sh1['H'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

            sh1['I'+str(i+9)] = float(u.cgst_txt[i-1].get())
            sh1['I'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

            sh1['K'+str(i+9)] = float(u.sgst_txt[i-1].get())
            sh1['K'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

            sh1['M'+str(i+9)] = float(u.net_txt[i-1].get())
            sh1['M'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
            if(u.wt_txt[i-1].get()!='' and u.net_txt[i-1].get()!=''):
                saveGstData(float(u.wt_txt[i-1].get()),u.des_txt[i-1].get(),4500,10000,float(u.cgst_txt[i-1].get()),float(u.sgst_txt[i-1].get()),float(u.net_txt[i-1].get()))

# ===========================================================old gold============================================================

        sh1['D19'] = "Old Jewellery"
        sh1['D19'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

        sh1['I19'] = "Weight"
        sh1['I19'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
        
        sh1['J19'] = "Unit Price"
        sh1['J19'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

        sh1['M19'] = "Total"
        sh1['M19'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
        for i in range(1,4):
            if u.oldtotal_txt[i-1].get()!="":
                sh1['A2'+str(i-1)] = i
                sh1['A2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
                
                sh1['B2'+str(i-1)] = u.oldDesc_txt[i-1].get()
                sh1['B2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
                
                sh1['I2'+str(i-1)] = float(u.oldwe_txt[i-1].get())
                sh1['I2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
                
                sh1['J2'+str(i-1)] = float(u.oldunit_txt[i-1].get())
                sh1['J2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
                
                sh1['M2'+str(i-1)] = float(u.oldtotal_txt[i-1].get())
                sh1['M2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
                
#====================================================ADDITION OR DEDUCTION================================================================================================================
        sh1['C24'] = "Other Addition Or Deduction"
        sh1['C24'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
        
        sh1['M24'] = "Amount"
        sh1['M24'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
        
        for i in range(1,4):
            if u.addtotal_txt[i-1].get()!="":
                sh1['A2'+str(i+4)] = i
                sh1['A2'+str(i+4)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
                
                sh1['B2'+str(i+4)] = u.addDesc_txt[i-1].get()
                sh1['B2'+str(i+4)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
                
                sh1['M2'+str(i+4)] = float(u.addtotal_txt[i-1].get())
                sh1['M2'+str(i+4)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
                
        
            

    # ===================================================mode of payment============================================


        sh1['E28'] = "Mode Of Payment"
        sh1['E28'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)

        sh1['I28'] = u.mode.get()
        sh1['I28'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

# =====================================================Total paid=======================================================

        sh1['A29'] = "Total in Words"
        sh1['A29'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)
        try:
            sh1['C29'] = convert(int(u.total.get()))
            sh1['C29'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
        except Exception:
            print("There is a error")

        sh1['J29'] = "Total Paid : "
        sh1['J29'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)
        sh1['L29'] = u.total.get()
        sh1['L29'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)
# =================================================Terms and conditions===================================================
        sh1['B30']="Terms and conditions"
        sh1['B30'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.red)

        sh1['A31'] = " 1. Before taking delivery Customer should check the ornaments by piece and weight. "
        sh1['A31'].font = Font(name='Times new romman',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

        sh1['A32'] = " 2. Exchange your ornaments within 7 days in good condition."
        sh1['A32'].font = Font(name='Times new romman',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

        sh1['A33'] = " 3. We are not responsible for any damage or brakage after delivery"
        sh1['A33'].font = Font(name='Times new romman',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=u.blue)

        # sh1['A34'] = " 4. We can repair the ornaments if possible"
        # sh1['A34'].font = Font(name='Times new romman',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

    thin = Side(border_style='thin',color='FF000000')
    medium = Side(border_style='medium',color='FF000000')
# ========================================================creating borders====================================================         

    fill_cell = PatternFill(fill_type=fills.FILL_SOLID,start_color='00FFFF00',end_color='00FFFF00')



   
    # ================================================== 5 =====================================================
    for i in range(2,14):
        sh1.cell(row=5, column=i).border=Border(top=medium,bottom=thin)
    sh1.cell(row=5,column=1).border=Border(left=medium,top=medium,bottom=thin)
    sh1.cell(row=5,column=14).border=Border(right=medium,top=medium,bottom=thin)
    
    # ==================================================== 6 =====================================================

    sh1.cell(row = 6,column = 1).border=Border(left=medium,top=thin)
    sh1.cell(row = 6,column = 14).border=Border(right=medium,top=thin)

    # ======================================================= 7 ====================================================

    sh1.cell(row = 7,column = 14).border=Border(right=medium,bottom=thin)
    sh1.cell(row = 7,column = 1).border=Border(left=medium,bottom=thin)


    # ======================================================= 8 =====================================================
    sh1.cell(row = 8,column = 1).border=Border(left=medium,top=thin)
    sh1.cell(row = 8,column = 2).border=Border(left=thin,top=thin)
    sh1.cell(row = 8,column = 3).border=Border(top=thin)
    sh1.cell(row = 8,column = 4).border=Border(right=thin,top=thin)
    sh1.cell(row = 8,column = 5).border=Border(right=thin,top=thin)

    sh1.cell(row = 8,column = 6).border=Border(left=thin,top=thin)
    sh1.cell(row = 8,column = 7).border=Border(left=thin,top=thin)
    sh1.cell(row = 8,column = 8).border=Border(left=thin,top=thin)
    sh1.cell(row = 8,column = 9).border=Border(left=thin,top=thin)
    sh1.cell(row = 8,column = 10).border=Border(right=thin,top=thin)

    sh1.cell(row = 8,column = 11).border=Border(left=thin,top=thin)
    sh1.cell(row = 8,column = 12).border=Border(right=thin,top=thin)
    sh1.cell(row = 8,column = 13).border=Border(top=thin)
    sh1.cell(row = 8,column = 14).border=Border(right=medium,top=thin)
    
    # ===================================================== 9 ======================================================
    
    sh1.cell(row = 9,column = 1).border=Border(left=medium,bottom=thin)
    sh1.cell(row = 9,column = 2).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 9,column = 3).border=Border(bottom=thin)
    sh1.cell(row = 9,column = 4).border=Border(bottom=thin,right=thin)
    sh1.cell(row = 9,column = 5).border=Border(bottom=thin,right=thin)
    sh1.cell(row = 9,column = 6).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 9,column = 7).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 9,column = 8).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 9,column = 9).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 9,column = 10).border=Border(right=thin,bottom=thin)
    sh1.cell(row = 9,column = 11).border=Border(left=thin,bottom=thin,)
    sh1.cell(row = 9,column = 12).border=Border(right=thin,bottom=thin)
    sh1.cell(row = 9,column = 13).border=Border(bottom=thin)
    sh1.cell(row = 9,column = 14).border=Border(right=medium,bottom=thin)


    # ========================================================== 10 =======================================================

    sh1.cell(row = 10,column = 1).border = Border(left=medium)
    for i in range(2,15):
        if(i!=3 and i!=4 and i!=5 and i!=10 and i!=12):
            sh1.cell(row = 10,column = i).border = Border(left=thin)
    sh1.cell(row = 10,column = 4).border=Border(right=thin,top=thin)

    # ============================================================= 10 to 18 ===================================================
    
    for i in range(10,18):
        sh1.cell(row = i,column = 14).border=Border(right=medium)

    for i in range(11,18):
        sh1.cell(row = i,column = 1).border = Border(left=medium)
        sh1.cell(row = i,column = 4).border = Border(right=thin)

    for j in range(1,15):
        if(j==2 or j==6 or j==7 or j==8 or j==9 or j==11 or j==13):  
            for i in range(11,18):
                sh1.cell(row = i,column = j).border = Border(left=thin)

    sh1.cell(row = 18,column = 1).border=Border(left=medium,bottom=thin,right=thin)

    sh1.cell(row = 18,column = 2).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 18,column = 3).border=Border(bottom=thin)
    sh1.cell(row = 18,column = 4).border=Border(bottom=thin,right=thin)
    sh1.cell(row = 18,column = 5).border=Border(bottom=thin,right=thin)
    sh1.cell(row = 18,column = 6).border=Border(left=thin,bottom=thin,right=thin)
    sh1.cell(row = 18,column = 7).border=Border(left=thin,bottom=thin,right=thin)
    sh1.cell(row = 18,column = 8).border=Border(left=thin,bottom=thin,right=thin)
    sh1.cell(row = 18,column = 9).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 18,column = 10).border=Border(bottom=thin,right=thin)
    sh1.cell(row = 18,column = 11).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 18,column = 12).border=Border(bottom=thin,right=thin)
    sh1.cell(row = 18,column = 13).border=Border(left=thin,bottom=thin)    
    sh1.cell(row = 18,column = 14).border=Border(right=medium,bottom=thin)    
    

    # ======================================================= 19 ==========================================================

    # sh1.cell(row = 19,column = 14).border=Border(right=medium,top=thin)
       
    sh1.cell(row = 19,column=8).border=Border(left=thin,top=thin,bottom=thin)
    sh1.cell(row = 19,column=9).border=Border(right=thin,top=thin,bottom=thin)
    sh1.cell(row = 19,column=7).border=Border(right=thin,top=thin,bottom=thin)
    sh1.cell(row = 19,column=2).border=Border(left=thin,top=thin,bottom=thin)
    for i in range(3,7):
        sh1.cell(row = 19,column=i).border=Border(top=thin,bottom=thin)
        
    sh1.cell(row = 19,column=1).border=Border(left=medium,top=thin,bottom=thin)
    
    sh1.cell(row = 19,column=10).border=Border(left=thin,top=thin,bottom=thin)
    sh1.cell(row = 19,column=11).border=Border(right=thin,top=thin,bottom=thin)
    
    
    sh1.cell(row = 19,column=12).border=Border(left=thin,top=thin,bottom=thin)
    sh1.cell(row = 19,column=13).border=Border(top=thin,bottom=thin)
    sh1.cell(row = 19,column=14).border=Border(right=medium,top=thin,bottom=thin)
    # ========================================================20 to 27 ==========================================
    sh1.cell(row = 25,column=1).border=Border(left=medium,top=thin,right=thin)
    sh1.cell(row = 26,column=1).border=Border(left=medium,right=thin)
    sh1.cell(row = 27,column=1).border=Border(left=medium,right=thin)
    sh1.cell(row = 28,column=1).border=Border(left=medium,bottom=thin,right=thin)
    
    
    sh1.cell(row = 25,column=12).border=Border(left=thin,top=thin)
    sh1.cell(row = 26,column=12).border=Border(left=thin)
    # sh1.cell(row = 27,column=12).border=Border(left=thin)
    sh1.cell(row = 27,column=12).border=Border(left=thin,bottom=thin)
    
    
    sh1.cell(row = 25,column=14).border=Border(right=medium,top=thin)
    sh1.cell(row = 26,column=14).border=Border(right=medium)
    # sh1.cell(row = 27,column=14).border=Border(right=medium)
    sh1.cell(row = 27,column=14).border=Border(right=medium,bottom=thin)
    
    


    for i in range(20,23):
        sh1.cell(row = i,column=1).border=Border(left=medium)
        sh1.cell(row = i,column=8).border=Border(left=thin)
        sh1.cell(row = i,column=10).border=Border(left=thin)
        sh1.cell(row = i,column=12).border=Border(left=thin)
        sh1.cell(row = i,column = 14).border=Border(right=medium)
    
    sh1.cell(row = 20,column=1).border=Border(right=thin,left=medium,top=thin)
    sh1.cell(row = 21,column=1).border=Border(right=thin,left=medium)
    sh1.cell(row = 22,column=1).border=Border(right=thin,left=medium)

    sh1.cell(row = 23,column=2).border=Border(left=thin,bottom=thin)
    for i in range(3,7):
        sh1.cell(row = 23,column=i).border=Border(bottom=thin)
    sh1.cell(row = 23,column=7).border=Border(right=thin,bottom=thin)
    sh1.cell(row = 23,column=9).border=Border(right=thin,bottom=thin)
    sh1.cell(row = 23,column=11).border=Border(right=thin,bottom=thin)
    sh1.cell(row = 23,column=13).border=Border(bottom=thin)
       
    sh1.cell(row = 23,column=8).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 23,column=10).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 23,column=12).border=Border(left=thin,bottom=thin)
    sh1.cell(row = 23,column=14).border=Border(right=medium,bottom=thin)

    sh1.cell(row = 23,column=1).border=Border(left=medium,bottom=thin)
    
    sh1.cell(row = 24,column=1).border=Border(left=medium,bottom=thin,top=thin)
    sh1.cell(row = 24,column=2).border=Border(left=thin,bottom=thin,top=thin)
    for i in range(3,12):
        sh1.cell(row = 24,column=i).border=Border(top=thin,bottom=thin)
    sh1.cell(row = 24,column=12).border=Border(left=thin,bottom=thin,top=thin)
    sh1.cell(row = 24,column=13).border=Border(bottom=thin,top=thin)
    sh1.cell(row = 24,column=14).border=Border(right=medium,bottom=thin,top=thin)
    
    # ============================================================= 29 =================================================

    sh1.cell(row = 28,column=14).border=Border(right=medium,bottom=thin,top=thin)
    for i in range(2,14):
        sh1.cell(row = 28,column=i).border=Border(bottom=thin,top=thin)
    
    sh1.cell(row = 28,column=1).border=Border(left=medium,top=thin,bottom=thin)

    # ======================================================= 30 =====================================================

    sh1.cell(row = 29,column=14).border=Border(right=medium,bottom=thin,top=thin)
    
    sh1.cell(row = 29,column=12).border=Border(left=thin,top=thin,bottom=thin)
    sh1.cell(row = 29,column=1).border=Border(left=medium,top=thin,bottom=thin)
    
    
    for i in range(2,14):
        sh1.cell(row = 29,column=i).border=Border(bottom=thin,top=thin)
    
    sh1.cell(row = 29,column=1).border=Border(left=medium,top=thin,bottom=thin)
    
    sh1.cell(row = 29,column=10).border=Border(left=thin,top=thin,bottom=thin)
    # =========================================================== 31 to 36 =======================================================

    sh1.cell(row = 30,column=1).border=Border(left=medium,top=thin)

    sh1.cell(row = 30,column=10).border=Border(left=thin,top=thin)

    for i in range(30,34):
        sh1.cell(row = i,column=14).border=Border(right=medium)
    
    sh1.cell(row = 33,column=14).border=Border(right=medium,bottom=medium)

    for i in range(31,34):
        sh1.cell(row = i,column=1).border=Border(left=medium)
        sh1.cell(row = i,column=10).border=Border(left=thin)

    for i in range(1,14):
        sh1.cell(row = 34,column=i).border=Border(top=medium)
    
# ====================================================Border Over=================================================            

            
    
    # sh1.set_print_scale(50)
    openpyxl.worksheet.worksheet.Worksheet.set_printer_settings(sh1, paper_size = 13, orientation='landscape')
    # sh1.page_setup.fitToWidth = 1
    # sh1.page_setup.fitToHeight = 0
    sh1.page_setup.fitToPage = True
    # sh1.set_print_scale(90)
    sh1.page_margins.top=0.0
    sh1.page_margins.right=0.0
    sh1.page_margins.left=0.5
    sh1.page_margins.bottom=0.0
    sh1.page_margins.footer = 0.0
    sh1.page_margins.header = 0.0

    foldername = 'D:\\Shop\Shop\\FrontEnd\\' + daten.strftime("%b_%y")
    if(os.path.isdir(foldername) == False):
        os.system('mkdir '+foldername)
    u.saveLocation = foldername+'/'+str(u.bill_txt)+'.xlsx'
    
    saveCustomerData(u,name=u.name_txt.get(),mobile=u.mobile_txt.get(),addhar_number=u.addhar_txt.get(),address=u.address_txt.get())
    saveBillLocation(u)
    # printBill()
    
    # wb.save(filename=u.saveLocation)

    wb.save(filename='test.xlsx')    