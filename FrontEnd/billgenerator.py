import openpyxl
from openpyxl.styles import PatternFill,Border, Side, Alignment, Protection, Font, borders,fills
import datetime

def saveCustomerData(name,mobile,addhar_number,address,bill_no,billing_date):
    pass

def saveGstDetail(billing_date,ornament_name,qty,gold_rate,total_val,cgst,sgst,net_total):
    pass








def generateBill(bill_txt, mobile_txt, Name_txt, addhar_txt ,des_txt, wt_txt, unitLabel_txt, cgstLabel_txt, sgstLabel_txt, toLabel_txt, oldDesc_txt,oldwe_txt, oldunit_txt, oldtotal_txt, addSi_txt, addDesc_txt, addtotal_txt):
    wb = openpyxl.Workbook()
    sh1 = wb.active
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


    # logo = Image("hallLogo.png")
    # logo.height=100
    # logo.width=100
    # sh1.add_image(logo,'M1')

# ======================================================customer details==================================================

    green = '064635'
    red = 'C85C5C'
    blue = '041C32'
    # row_loc= row_loc+row_num+dis 
    sh1['A5'] = 'GSTIN - 21AYRPK4931F1ZH'
    sh1['A5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')

    sh1['H5'] = "SI. No.: "
    sh1['H5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='064635')
    sh1['I5'] = bill_txt.get()
    sh1['I5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='C85C5C')

    sh1['K5'] = 'Date: '+ daten.strftime("%d-%b-%y - (%A)")
    sh1['K5'].font = Font(name='times new rommon',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='064635')

    # for i in range(1,col_num-1):
    #      sh1.cell(row=5, column=i+1).border=Border(top=Side(border_style='medium',color='FF000000'),
    #      bottom=Side(border_style='thin',color='FF000000'))
    
    # sh1.cell(row=5, column=1).border=Border(top=Side(border_style='medium',color='FF000000'),
    #      bottom=Side(border_style='thin',color='FF000000'),left=Side(border_style='medium',color='FF000000'))
    
    # sh1.cell(row=5, column=col_num).border=Border(top=Side(border_style='medium',color='FF000000'),
    #      bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='medium',color='FF000000'))

    sh1['A6'] = "Name: "
    sh1['A6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['B6'] = Name_txt.get()
    sh1['B6'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

    sh1['F6'] = 'Mobile No.'
    sh1['F6'].font = Font(name='times new rommon',size=11,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['G6'] = '  '+mobile_txt.get()
    sh1['G6'].font = Font(name='arial',size=10,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

    sh1['I6'] = 'Addhar No.'
    sh1['I6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['J6'] = addhar_txt.get()
    sh1['J6'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

    sh1['M6'] = 'Bill No.'
    sh1['M6'].font = Font(name='times new rommon',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['N6'] = bill_txt.get()
    sh1['N6'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

    sh1['F7'] = "Gold Rate: "
    sh1['F7'].font = Font(name='times new rommon',size=15,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['H7'] = "45000"
    sh1['H7'].font = Font(name='arial',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)


# ===========================================product details======================================================================
    
    sh1['A8'] = 'Si.no.'
    sh1['A8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['B8'] = 'Description Of Goods'
    sh1['B8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['F8'] = 'HSN'
    sh1['F8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['F9'] = 'SAC'
    sh1['F9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    
    sh1['G8'] = 'Weight'
    sh1['G8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)

    sh1['H8'] = 'Unit'
    sh1['H8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['H9'] = 'Price'
    sh1['H9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)

    # sh1['J7'] = 'Taxable'
    # sh1['J7'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    # sh1['J7'] = 'Amount'
    # sh1['J7'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['I8'] = 'CGST'
    sh1['I8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['I9'] = '1.5%'
    sh1['I9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)

    sh1['K8'] = 'SGST'
    sh1['K8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['K9'] = '1.5%'
    sh1['K9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)

    sh1['M8'] = 'Net'
    sh1['M8'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)
    sh1['M9'] = 'Total'
    sh1['M9'].font = Font(name='times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)

    sh1['F10'] = '7113'
    sh1['F10'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

    for i in range(1,10):
        if(des_txt[i-1].get()!= ""):
            sh1['A'+str(i+9)] = i
            sh1['A'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

            sh1['B'+str(i+9)] = des_txt[i-1].get()
            sh1['B'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

            sh1['G'+str(i+9)] = wt_txt[i-1].get()
            sh1['G'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

            sh1['H'+str(i+9)] = unitLabel_txt[i-1].get()
            sh1['H'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

            # sh1['K'+str(i+8)] = [i-1].get()
            # sh1['N8'].font = Font(name='times new romman',size=13,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=green)

            sh1['I'+str(i+9)] = cgstLabel_txt[i-1].get()
            sh1['I'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

            sh1['K'+str(i+9)] = sgstLabel_txt[i-1].get()
            sh1['K'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

            sh1['M'+str(i+9)] = toLabel_txt[i-1].get()
            sh1['M'+str(i+9)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)


# ===========================================================old gold============================================================

        sh1['D19'] = "Old Jewellery"
        sh1['D19'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

        sh1['I19'] = "Weight"
        sh1['I19'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
        
        sh1['J19'] = "Unit Price"
        sh1['J19'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

        sh1['M19'] = "Total"
        sh1['M19'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
        for i in range(1,4):
            if oldDesc_txt[i-1].get!="":
                sh1['A2'+str(i-1)] = i
                sh1['A2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
                
                sh1['B2'+str(i-1)] = oldDesc_txt[i-1].get()
                sh1['B2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
                
                sh1['I2'+str(i-1)] = oldwe_txt[i-1].get()
                sh1['I2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
                
                sh1['J2'+str(i-1)] = oldunit_txt[i-1].get()
                sh1['J2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
                
                sh1['M2'+str(i-1)] = oldtotal_txt[i-1].get()
                sh1['M2'+str(i-1)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
                
#====================================================ADDITION OR DEDUCTION================================================================================================================
        sh1['D24'] = "Other Addition Or Deduction"
        sh1['D24'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
        
        sh1['M24'] = "Amount"
        sh1['M24'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
        
        for i in range(1,4):
            if addDesc_txt[i-1].get()!="":
                sh1['A2'+str(i+4)] = i
                sh1['A2'+str(i+4)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
                
                sh1['D2'+str(i+4)] = addDesc_txt[i-1].get()
                sh1['D2'+str(i+4)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
                
                sh1['M2'+str(i+4)] = addtotal_txt[i-1].get()
                sh1['M2'+str(i+4)].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
                
        
            

    # ===================================================mode of payment============================================


        sh1['E29'] = "Mode Of Payment"
        sh1['E29'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

        sh1['I29'] = "Cash"
        sh1['I29'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

# =====================================================Total paid=======================================================

        sh1['A30'] = "Total in Words"
        sh1['A30'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)
        sh1['C30'] = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        sh1['C30'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

        sh1['J30'] = "Total Paid : "
        sh1['J30'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)
        sh1['L30'] = '2000000'
        sh1['L30'].font = Font(name='arial',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)
# =================================================Terms and conditions===================================================
        sh1['B31']="Terms and conditions"
        sh1['B31'].font = Font(name='Times new romman',size=14,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=red)

        sh1['A32'] = " 1. Before taking delivery Customer should check the ornaments by piece and weight. "
        sh1['A32'].font = Font(name='Times new romman',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

        sh1['A33'] = " 2. Exchange your ornaments within 7 days in good condition."
        sh1['A33'].font = Font(name='Times new romman',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

        sh1['A34'] = " 3. We are not responsible for any damage or brakage after delivery"
        sh1['A34'].font = Font(name='Times new romman',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)

        sh1['A35'] = " 4. We can repair the ornaments if possible"
        sh1['A35'].font = Font(name='Times new romman',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color=blue)


# ========================================================creating borders=====================================================
    # sh1['A3'] = "Name"
    thin_border_bottom = Border(bottom=Side(border_style='thin',color='FF000000'))
    thin_border_right = Border(right=Side(border_style='dashed',color='FF000000'))
    thin_border_top   = Border(top=Side(border_style='thin',color='FF000000'))
    thin_border_left  = Border(left=Side(border_style='thin',color='FF000000'))
                
    thick_border_left = Border(left=Side(border_style='medium',color='FF000000'))
    thick_border_right = Border(right=Side(border_style='medium',color='FF000000'))
    thick_border_top = Border(top=Side(border_style='medium',color='FF000000'))
    thick_border_bottom = Border(bottom=Side(border_style='medium',color='FF000000'))
                    

    fill_cell = PatternFill(fill_type=fills.FILL_SOLID,start_color='00FFFF00',end_color='00FFFF00')

    # ================================================== 5 =====================================================
    for i in range(2,14):
        sh1.cell(row=5, column=i).border=Border(top=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row=5,column=1).border=Border(left=Side(border_style='medium',color='FF000000'),top=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row=5,column=14).border=Border(right=Side(border_style='medium',color='FF000000'),top=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    
    # ==================================================== 6 =====================================================

    sh1.cell(row = 6,column = 1).border=Border(left=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 6,column = 14).border=Border(right=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'))

    # ======================================================= 7 ====================================================

    sh1.cell(row = 7,column = 14).border=Border(right=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 7,column = 1).border=Border(left=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))


    # ======================================================= 8 =====================================================

    sh1.cell(row = 8,column = 1).border=Border(left=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 2).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 3).border=Border(top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 4).border=Border(top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 5).border=Border(right=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))

    sh1.cell(row = 8,column = 6).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 7).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 8).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 9).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 10).border=Border(right=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))

    sh1.cell(row = 8,column = 11).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 12).border=Border(right=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 13).border=Border(top=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 8,column = 14).border=Border(right=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    
    # ===================================================== 9 ======================================================
    
    sh1.cell(row = 9,column = 1).border=Border(left=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 2).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 3).border=Border(bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 4).border=Border(bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 5).border=Border(bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 6).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 7).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 8).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 9).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 10).border=Border(right=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 11).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'),)
    sh1.cell(row = 9,column = 12).border=Border(right=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 13).border=Border(bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 9,column = 14).border=Border(right=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))


    # ========================================================== 10 =======================================================

    sh1.cell(row = 10,column = 1).border = Border(left=Side(border_style='medium',color='FF000000'))
    for i in range(2,15):
        if(i!=3 and i!=4 and i!=5 and i!=10 and i!=12):
            sh1.cell(row = 10,column = i).border = Border(left=Side(border_style='thin',color='FF000000'))

    # ============================================================= 10 to 18 ===================================================
    
    for i in range(10,18):
        sh1.cell(row = i,column = 14).border=Border(right=Side(border_style='medium',color='FF000000'))

    for i in range(11,18):
        sh1.cell(row = i,column = 1).border = Border(left=Side(border_style='medium',color='FF000000'))

    for j in range(1,15):
        if(j==2 or j==6 or j==7 or j==8 or j==9 or j==11 or j==13):  
            for i in range(11,18):
                sh1.cell(row = i,column = j).border = Border(left=Side(border_style='thin',color='FF000000'))

    sh1.cell(row = 18,column = 1).border=Border(left=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='thin',color='FF000000'))

    sh1.cell(row = 18,column = 2).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 3).border=Border(bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 4).border=Border(bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 5).border=Border(bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 6).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 7).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 8).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 9).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 10).border=Border(bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 11).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 12).border=Border(bottom=Side(border_style='thin',color='FF000000'),right=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 18,column = 13).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))    
    sh1.cell(row = 18,column = 14).border=Border(right=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))    
    

    # ======================================================= 19 ==========================================================

    sh1.cell(row = 19,column = 14).border=Border(right=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'))    
    sh1.cell(row = 19,column=8).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))

    sh1.cell(row = 19,column=1).border=Border(left=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    
    sh1.cell(row = 19,column=10).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    
    sh1.cell(row = 19,column=12).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    # ========================================================20 to 27 ==========================================
    sh1.cell(row = 26,column=1).border=Border(left=Side(border_style='medium',color='FF000000'))


    for i in range(20,28):
        sh1.cell(row = i,column=1).border=Border(left=Side(border_style='medium',color='FF000000'))
        sh1.cell(row = i,column=8).border=Border(left=Side(border_style='thin',color='FF000000'))
        sh1.cell(row = i,column=10).border=Border(left=Side(border_style='thin',color='FF000000'))
        sh1.cell(row = i,column=12).border=Border(left=Side(border_style='thin',color='FF000000'))
        sh1.cell(row = i,column = 14).border=Border(right=Side(border_style='medium',color='FF000000'))

    
    sh1.cell(row = 28,column=8).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 28,column=10).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 28,column=12).border=Border(left=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 28,column=14).border=Border(right=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))

    sh1.cell(row = 28,column=1).border=Border(left=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    
    # ============================================================= 29 =================================================

    sh1.cell(row = 29,column=14).border=Border(right=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    for i in range(2,14):
        sh1.cell(row = 29,column=i).border=Border(bottom=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    
    sh1.cell(row = 29,column=1).border=Border(left=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))

    # ======================================================= 30 =====================================================

    sh1.cell(row = 30,column=14).border=Border(right=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    
    sh1.cell(row = 30,column=12).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    sh1.cell(row = 30,column=1).border=Border(left=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    
    
    for i in range(2,14):
        sh1.cell(row = 30,column=i).border=Border(bottom=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))
    
    sh1.cell(row = 30,column=1).border=Border(left=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    
    sh1.cell(row = 30,column=10).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'),bottom=Side(border_style='thin',color='FF000000'))
    # =========================================================== 31 to 36 =======================================================

    sh1.cell(row = 31,column=1).border=Border(left=Side(border_style='medium',color='FF000000'),top=Side(border_style='thin',color='FF000000'))

    sh1.cell(row = 31,column=10).border=Border(left=Side(border_style='thin',color='FF000000'),top=Side(border_style='thin',color='FF000000'))

    for i in range(31,35):
        sh1.cell(row = i,column=14).border=Border(right=Side(border_style='medium',color='FF000000'))
    
    sh1.cell(row = 35,column=14).border=Border(right=Side(border_style='medium',color='FF000000'),bottom=Side(border_style='medium',color='FF000000'))

    for i in range(32,36):
        sh1.cell(row = i,column=1).border=Border(left=Side(border_style='medium',color='FF000000'))
        sh1.cell(row = i,column=10).border=Border(left=Side(border_style='thin',color='FF000000'))

    for i in range(1,14):
        sh1.cell(row = 36,column=i).border=Border(top=Side(border_style='medium',color='FF000000'))
    
# ====================================================Border Over=================================================            

            
    

    openpyxl.worksheet.worksheet.Worksheet.set_printer_settings(sh1, paper_size = 1, orientation='landscape')
    sh1.page_margins.top=.2
    sh1.page_margins.right=.2
    sh1.page_margins.bottom=.2



    wb.save(filename='test.xlsx')
    # os.system('test.xlsx')
